from flask import Flask, render_template, request, redirect, url_for

api = Flask(__name__)

# Lista utenti con nome, password, genere e altro
utenti = [['mario', 'password01', 'M', '1'], ['gianni', 'password02', 'M', '1'], ['Anita', 'password03', 'F', '1']]

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

    # Controlla se l'utente è già registrato
    for u in utenti:
        if u[0].lower() == nome.lower() and u[1] == password and u[2] == genere:
            if u[3] == '1':  # Se l'utente è già registrato
                return redirect(url_for('loggati'))  # Reindirizza alla pagina di login

    # Se l'utente non esiste, aggiungilo alla lista utenti
    nuovo_utente = [nome, password, genere, '1']
    utenti.append(nuovo_utente)

    return render_template('reg_ok.html')  # Mostra pagina di registrazione riuscita

@api.route('/loggati', methods=['GET', 'POST'])
def loggati():
    if request.method == 'POST':
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

        return render_template('log_ko.html')  # Credenziali errate
    return render_template('index2.html')  # Mostra il form di login

@api.route('/logok', methods=['GET'])
def logok():
    return render_template("log_ok.html")

@api.route('/logko', methods=['GET'])
def logko():
    return render_template("log_ko.html")

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8085)
