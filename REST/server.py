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
        sCodiceFiscale = jRequest["codice fiscale"]
        print("Ricevuto " + sCodiceFiscale)
        #carichiamo l'anagrafe
        dAnagrafe = JsonDeserialize(sFileAnagrafe)
        #controlla che il cittadino non è gia presente in anagrafe
        if sCodiceFiscale not in dAnagrafe:
            dAnagrafe[sCodiceFiscale] = jRequest
            JsonSerialize(dAnagrafe,sFileAnagrafe)
            #rispondi
            jResponse = {"Error" : "000" , "Msg": "Cittadino aggiunto con successo"}
            return json.dumps(jResponse),200  #200 è il codice del http
        else:
            jResponse = {"Error" : "001" , "Msg": "codice fiscale già presente"}
            return json.dumps(jResponse),200  
    else:
        return "Errore , formato non riconosciuto",401 
    

@api.route("/richiedi_dati",methods = ['POST'])
def GestisciRichiestaDati():

    content_type = request.headers.get('Content-Type')
    
    if content_type == "application/json":

        jRequest = request.json
        sCodiceFiscale = jRequest["codice fiscale"]
        dAnagrafe = JsonDeserialize(sFileAnagrafe)

        if sCodiceFiscale in dAnagrafe:
            info =  dAnagrafe[sCodiceFiscale] 
        
            jResponse = {"Error" : "000" , "Msg": "Operazione terminata con successo", 'info': info}
            return json.dumps(jResponse),200  #200 è il codice del http
        else:
            jResponse = {"Error" : "001" , "Msg": "codice fiscale non trovato"}
            return json.dumps(jResponse),200  
        

@api.route("/modifica_dati",methods = ['POST'])
def GestisciModificaDati():
    content_type = request.headers.get('Content-Type')
    if content_type == "application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codice fiscale"]
        dAnagrafe = JsonDeserialize(sFileAnagrafe)
        
        if sCodiceFiscale in dAnagrafe:
            info =  dAnagrafe[sCodiceFiscale] 
        
            if "nome" in jRequest:
                info["nome"] = jRequest["nome"]
            if "cognome" in jRequest:
                info["cognome"] = jRequest["cognome"]
            if "data nascita" in jRequest:
                info["data nascita"] = jRequest["data nascita"]
                
            dAnagrafe[sCodiceFiscale] = info
            JsonSerialize(dAnagrafe, sFileAnagrafe)

            jResponse = {"Error": "000", "Msg": "Dati modificati con successo", 'info': info}
            return json.dumps(jResponse), 200
        else:
            jResponse = {"Error": "001", "Msg": "codice fiscale non trovato"}
            return json.dumps(jResponse), 200
    
    
@api.route("/elimina_cittadino",methods = ['POST'])
def GestireEliminazioneCittadino():
    content_type = request.headers.get('Content-Type')

    if content_type == "application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codice fiscale"]
        dAnagrafe = JsonDeserialize(sFileAnagrafe)

        if sCodiceFiscale in dAnagrafe:
            del dAnagrafe[sCodiceFiscale]
            JsonSerialize(dAnagrafe, sFileAnagrafe)
            
            jResponse = {"Error": "000", "Msg": "Cittadino eliminato con successo"}
            return json.dumps(jResponse), 200
        else:
            jResponse = {"Error": "001", "Msg": "Codice fiscale non trovato"}
            return json.dumps(jResponse), 200





@api.route('/', methods = ['GET'])
def manageget():
    return "Ciao a tutti"

api.run(host = "127.0.0.1" , port = 8080)