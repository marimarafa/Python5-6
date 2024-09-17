from flask import Flask,render_template, request

api = Flask(__name__)

# Lista utenti con nome, password, genere e altro
utenti = [['mario', 'password01', 'M'], ['gianni', 'password02', 'M'], ['Anita', 'password03', 'F']]

@api.route('/loggati', methods = ['GET'])
def loggati():
    return ' Ciao Buongiorno'

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
    
    # Controlla se l'utente esiste e i dati corrispondono
    for utente in utenti:
        if (utente[0].lower() == nome.lower()) and (utente[1] == password) and (utente[2] == genere):
            return render_template('reg_ok.html')  # Accesso riuscito

    # Se non trova l'utente, reindirizza a "accesso negato"
    return render_template('reg_ko.html')

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8085)
