from flask import Flask,json,request
from myJason import JsonSerialize,JsonDeserialize

sFileAnagrafe = "./anagrafe.json"
api = Flask(__name__)

@api.route('/add_cittadino', methods = ['POST'])
def GestisciAddCittadino():
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == "application/json":
        jRequest = request.json
        print(jRequest)
        jResponse = {"Error" : "000" , "Msg": "Ok"}
        return json.dumps(jResponse),200  #200 è il codice del http
    else:
        return "Errore , formato non riconosciuto",401 

    #controlla che il cittadino non è gia presente in anagrafe
    #rispondi

@api.route('/', methods = ['GET'])
def manageget():
    return "Ciao a tutti"

api.run(host = "127.0.0.1" , port = 8080)

