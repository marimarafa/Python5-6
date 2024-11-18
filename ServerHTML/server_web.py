from flask import Flask,render_template, request
import requests

api = Flask(__name__)
base_url = "https://127.0.0.1:8080"

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

@api.route('/aggCittadino', methods=['GET'])
def agg_cittadino():
    return render_template("aggiungi_cittadino.html")

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

                return render_template("reg_ok.html")
        return render_template("reg_ko.html")  
        
    except:
        print("Attenzione , problemi di comunicazione con il server, Riprova piu tardi.")
        return render_template("reg_ko.html")  
    
@api.route('/addCittadino', methods=['GET'])
def add_cittadino():
    nome = request.args.get("nome")
    cognome =  request.args.get("cognome")
    dataN =  request.args.get("dataNascita")
    codF =  request.args.get("codFiscale")
    datiCittadino = {
        "nome": nome, 
        "cognome": cognome, 
        "dataNascita": dataN, 
        "codFiscale": codF
    }
    api_url = base_url + "/add_cittadino"
    jsonDataRequest = datiCittadino
    response = requests.post(api_url,jsonDataRequest,verify= False)
    print(response.status_code)
    if response.status_code == 200:
            return"""<html>
    <head>
        <title>
           Aggiunta Cittadino
        </title>
        <style>
            body, html {
                height: 100%;
                margin: 0;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                background-color: #f0f0f0;
            }
            h1 {
                text-align: center;
                font-size: 36px;
                color: #333;
                margin-bottom: 40px;
            }
            .button-container {
                display: flex;
                flex-direction: column;
                gap: 15px; /* Spazio tra i bottoni */
                width: 100%;
                max-width: 300px;
            }
            input[type="submit"] {
                padding: 15px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 18px;
                cursor: pointer;
                width: 100%;
            }
            input[type="submit"]:hover {
                background-color: #45a049;
            }
            .form-container {
                width: 100%;
                max-width: 300px;
            }
        </style>
    </head>
    <body>

        <h1>CITTADINO AGGIUNTO CON SUCCESSO </h1>
        <form action="/regok" method="get">
            <input type="submit" value="Ritorna alla pagina principale ">
        </form>
    </body>
</html>"""+ datiCittadino
    else:
        return render_template("reg_ko.html")
            
     

@api.route('/logok', methods=['GET'])
def logok():
    return render_template("log_ok.html")

@api.route('/logko', methods=['GET'])
def logko():
    return render_template("log_ko.html")


if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8085)
