from flask import Flask,render_template, request

api = Flask(__name__)

# Lista utenti con nome, password, genere e altro
utenti = [['mario', 'password01', 'Maschio', '0'], ['gianni', 'password02', 'Maschio', '0'], ['Anita', 'password03', 'Femmina', '0']]

@api.route('/', methods=['GET'])
def pagina1():
    return render_template("pagina1.html")

@api.route('/registra', methods=['GET'])
def registra():
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
def registrati():
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

    for utente in utenti:
        if utente[0]==nome and utente[1]==password and utente[3]=="1":
            genere = utente[2]
            return render_template('log_ok.html') # Accesso riuscito
    return render_template('log_ko.html') #utente non registrato


@api.route('/logok', methods=['GET'])
def logok():
    return render_template("log_ok.html")

@api.route('/logko', methods=['GET'])
def logko():
    return render_template("log_ko.html")

@api.route('/ordinipassati', methods=['GET'])
def ordinipassati():
    return render_template("ordini_passati.html")

@api.route('/ordiniincorso', methods=['GET'])
def ordiniincorso():
    return render_template("ordini_in_corso.html")


if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8085)
