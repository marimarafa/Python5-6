from flask import Flask, render_template, request
import requests

api = Flask(__name__)
base_url = "https://127.0.0.1:8080"

utenti = [['mario','password1','M','0'], 
          ['gianni','password2','M','0'], 
          ['AnitaGaribaldi', 'pass3','F','0'] 
          ]


@api.route('/loggati', methods=['GET'])
def get_code():
    #prendi i dati della form
    nome = "mario"
    sResponsePage = "<html><body><h1>Buongiorno" + nome + " a tutti, il 17 settembre 2024</h1></body></html>"
    return sResponsePage

@api.route('/registrati', methods=['GET','POST'])
def registra_new():
    if request.method == 'POST':
       nome = request.form['nome'] + "DA POST"
       password = request.form['password']
    else:
        nome = request.args.get('nome') + " DA GET"
        password = request.args.get('password') 
    
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
                Privilegio = jsonResponse["Privilegi"]
                sResponsePage = "<html><body><h1>Registrazione effetuata con successo, Buongiorno " + nome + " </h1></body></html>"
                return sResponsePage
    except:
        print("Attenzione , problemi di comunicazione con il server, Riprova piu tardi.")
        sResponsePage = "<html><body><h1>Registrazione non effettuata .Riprovare </h1></body></html>"
        return sResponsePage

   


@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/regok', methods=['GET'])
def regOk():
    return render_template('reg_ok.html')


@api.route('/regko', methods=['GET'])
def regKo():
    return render_template('reg_ko.html')

@api.route('/registrati1', methods=['GET'])
def registra():

    nome = request.args.get("nome")
    print("Nome inserito:" + nome)
    password = request.args.get("cognome")

    if request.args.get("sesso")=="1":
        sesso="M"
    else:
        sesso = "F"

    utente = []
    utente.append(nome)
    utente.append(password)
    utente.append(sesso)
    utente.append("0")

    if utente in utenti:
        index = utenti.index(utente)
        utenti[index][3]="1"
        return render_template('reg_ok.html')

    #Devo prendere tutti i dati e verificare se la terna c'è nel vettore degli utenti
    return render_template('reg_ko.html')

api.run(host="0.0.0.0",port=8085)


