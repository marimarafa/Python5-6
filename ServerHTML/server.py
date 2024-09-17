from flask import Flask,render_template, request

api = Flask(__name__)

# Lista utenti con nome, password, genere e altro
utenti = [['mario', 'password01', 'M', '0'], ['gianni', 'password02', 'M','0'], ['Anita', 'password03', 'F','0']]

@api.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@api.route('/regok', methods=['GET'])
def regok():
    return render_template("reg_ok.html")

@api.route('/regko', methods=['GET'])
def regko():
    return render_template("reg_ko.html")

# Modifica: accettare il metodo POST per il form
@api.route('/registrati', methods=['GET'])
def registra():
    nome = request.args.get("nome")
    password = request.args.get("password")
    genere = request.args.get("genere")
    utente = [nome, password,genere, '0']

    # Controlla se l'utente esiste e i dati corrispondono
    if utente in utenti:
        if (utente[0].lower() == nome.lower()) and (utente[1] == password) and (utente[2] == genere):
            if utente[3] == '0':
                return render_template('reg_ok.html')  # Accesso riuscito
            else:
                return render_template('index2.html') #utente gia registrato
            
    # Se non trova l'utente, reindirizza a "accesso negato"
    return render_template('reg_ko.html')

@api.route('/loggati', methods=['GET'])
def loggati():
    nome = request.args.get("nome")
    password = request.args.get("password")
    genere = request.args.get("genere")
    utente = [nome, password,genere, '1']

    if utente in utenti:
        if (utente[0].lower() == nome.lower()) and (utente[1] == password) and (utente[2] == genere):
            if utente[3] == '1':
                return f'Ciao {nome} . Sei {genere}' # Accesso riuscito
            else:
                return render_template('log_ko.html') #utente non registrato
            
    return render_template('index.html')

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8085)
