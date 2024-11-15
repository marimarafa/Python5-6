from flask import Flask,render_template, request
import requests

api = Flask(__name__)
base_url = "https://127.0.0.1:8080"
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

@api.route('/operazioni', methods=['GET'])
def login():
    return render_template("index2.html")

# Modifica: accettare il metodo POST per il form
@api.route('/registrati', methods=['GET'])
def registrati():
    nome = request.args.get("nome")
    password = request.args.get("password")
    dUser = {
        "username" : nome ,
        "password" : password 
    }
    try:
        api_url = base_url + "/login"
        response = requests.post(api_url,json= dUser,verify=False)
        if response.status_code == 200:
            jsonResponse = response.json()

            if jsonResponse["Esito"] == "000":
                print(111)

                #Privilegio = jsonResponse["Privilegi"]
                return render_template("reg_ok.html")
        return render_template("reg_ko.html")  
        
    except:
        print("Attenzione , problemi di comunicazione con il server, Riprova piu tardi.")
        return render_template("reg_ko.html")  
    
            
     

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


if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8085)
