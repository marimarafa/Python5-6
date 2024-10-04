from flask import Flask, jsonify, request
from myjson import JsonDeserialize, JsonSerialize

api = Flask(__name__)


file_path = "anagrafe.json"
loginFile_path = "utenti.json"

cittadini = JsonDeserialize(file_path)
utenti = JsonDeserialize(loginFile_path)

@api.route("/login" , methods = ["POST"])
def GestisciLogin():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json

# utenti [1chiave][2chiave]-> stampa il valore del valore (il primo valore è un dizionario)

        username = jsonReq["username"]
        password = utenti[username]["password"]
        privilegi = utenti[username]["privilegi"]

        if username in utenti and password == jsonReq["password"]:
            return jsonify({"Esito": "000", "Msg": "Login effetuato con successo", "Privilegio":privilegi}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Utente non trovato"}) , 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200


cittadini = JsonDeserialize(file_path)
@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        if codice_fiscale in cittadini:
            return jsonify({"Esito": "001", "Msg": "Cittadino già esistente"}), 200
        else:
            cittadini[codice_fiscale] = jsonReq
            JsonSerialize(cittadini, file_path) 
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiunto con successo"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200

# < argomento > è lo stesso argomento passato nella funzione
@api.route('/read_cittadino/<codice_fiscale>', methods=['GET'])
def read_cittadino(codice_fiscale): # parametro passsato nella url
    cittadino = cittadini.get(codice_fiscale)
    if cittadino:
        return jsonify({"Esito": "000", "Msg": "Cittadino trovato", "Dati": cittadino}), 200
    else:
        return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200

@api.route('/update_cittadino', methods=['PUT'])
def update_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        if codice_fiscale in cittadini:
            cittadini[codice_fiscale] = jsonReq
            JsonSerialize(cittadini, file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiornato con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200


@api.route('/elimina_cittadino', methods=['DELETE'])
def elimina_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        cod = request.json.get('codFiscale')
        if cod in cittadini:
            del cittadini[cod]
            JsonSerialize(cittadini, file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino rimosso con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200

api.run(host="127.0.0.1", port=8080)

