from flask import Flask, render_template, request

api = Flask(__name__)

# Lista utenti con nome, password, genere e altro
utenti = [['mario', 'password01', 'M', '0'], ['gianni', 'password02', 'M', '0'], ['Anita', 'password03', 'F', '0']]

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
@api.route('/registrati', methods=['POST'])
def registra():
    nome = request.form.get("nome")
    password = request.form.get("password")
    genere = request.form.get("genere")
    utente = [nome, password, genere, '0']

    # Controlla se l'utente esiste e i dati corrispondono
    for u in utenti:
        if u[0].lower() == nome.lower() and u[1] == password and u[2] == genere:
            if u[3] == '0':
                u[3] = '1'  # Aggiorna lo stato dell'utente a registrato
                return render_template('reg_ok.html')  # Accesso riuscito
            elif u[3] == '1':
                return render_template('index2.html')  # Utente già registrato

    return render_template('reg_ko.html')  # Accesso negato

@api.route('/loggati', methods=['POST'])
def loggati():
    nome = request.form.get("nome")
    password = request.form.get("password")
    genere = request.form.get("genere")

    # Cerca l'utente nella lista
    for u in utenti:
        if u[0].lower() == nome.lower() and u[1] == password and u[2] == genere:
            if u[3] == '1':
                return f'Ciao {nome}. Sei {genere}.' + render_template('log_ok.html')  # Accesso riuscito
            else:
                return render_template('log_ko.html')  # Utente non registrato

    return render_template('index.html')  # Accesso negato

@api.route('/logok', methods=['GET'])
def logok():
    return render_template("log_ok.html")

@api.route('/logko', methods=['GET'])
def logko():
    return render_template("log_ko.html")

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8085)
