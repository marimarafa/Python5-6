from flask import Flask,render_template, request

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

@api.route('/login', methods=['GET'])
def login():
    return render_template("index2.html")

# Modifica: accettare il metodo POST per il form
@api.route('/registrati', methods=['GET'])
def registra():
    nome = request.args.get("nome")
    password = request.args.get("password")
    genere = request.args.get("genere")
    utente = [nome, password,genere, '0']

     # Controlla se l'utente esiste e i dati corrispondono
    if utente in utenti:
        ind: int = utenti.index(utente)
        utenti[ind][3] = "1"  
        return render_template('reg_ok.html') # Accesso riuscito 
    else:
        return render_template('reg_ko.html')  #utente gia registrato
            
     

@api.route('/loggati', methods=['GET'])
def loggati():
    nome = request.args.get("nome")
    password = request.args.get("password")
    genere = request.args.get("genere")
    utente = [nome, password, genere, '1']

    if utente in utenti:
        
        return render_template('log_ok.html') +f'CIAO {nome.capitalize()}, SEI {genere}' # Accesso riuscito
    else:
        return render_template('log_ko.html') #utente non registrato
 
@api.route('/logok', methods=['GET'])
def logok():
    return render_template("log_ok.html")

@api.route('/logko', methods=['GET'])
def logko():
    return render_template("log_ko.html")


if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8085)
