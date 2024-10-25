from flask import Flask, jsonify, request
import dbclient as db
import sys

api = Flask(__name__)

cur = db.connect()
if cur is None:
	print("Errore connessione al DB")
	sys.exit()


@api.route("/login" , methods = ["POST"])
def GestisciLogin():
    global cur 
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        print(jsonReq)
        username = jsonReq["username"]
        password = jsonReq["password"]

        sQuery = "select * from utenti where username =' " + username + "'" \
        + "and password = '" + password + "';"
        print(sQuery)

        inumRow = db.read_in_db(cur , sQuery)
        # read in db -> esegue la query -> restituisce il numero di righe
        #  myrow = db.read_next_row(cur) -> per leggere  le righe

        if inumRow == 1:
            lRow = db.read_next_row(cur)
            sPriv = lRow[1][2]

            return jsonify({"Esito": "000", "Msg": "Login effetuato con successo","Privilegi:": sPriv}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Utente non trovato"}) , 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200


@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    global cur
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json

        codice_fiscale = jsonReq.get('codFiscale')
        nome = jsonReq.get('nome')
        cognome = jsonReq.get('cognome')
        data_nascita = jsonReq.get('dataNascita')
        
        Squery ="'"+ codice_fiscale +"','" + nome + "','" + cognome +"','" + data_nascita + "'"
        sQuery = "insert into cittadini (codice_fiscale, nome, cognome, data_nascita) VALUES (" + Squery + ")"
        print(sQuery)
        iRet = db.write_in_db(cur,sQuery)
        
        if iRet == -2:
            return jsonify({"Esito": "001", "Msg": "Cittadino già esistente"}), 200
        elif iRet == 0:
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiunto con successo"}), 200
        else:
            return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200

# < argomento > è lo stesso argomento passato nella funzione
@api.route('/read_cittadino/<codice_fiscale>', methods=['GET'])
def read_cittadino(codice_fiscale): # parametro passsato nella url
    sQuery1 = "select * from cittadini where codice_fiscale ='" + codice_fiscale + "';"
    iNumRow = db.read_in_db(cur,sQuery1)
    for _ in range(0,iNumRow):
        myrow = db.read_next_row(cur)
    print(myrow)
    if iNumRow == 1:
        return jsonify({"Esito": "000", "Msg": "Cittadino trovato", "Dati":[myrow]}), 200
    else:
        return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200

@api.route('/update_cittadino', methods=['PUT'])
def update_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        nome = jsonReq.get('nome')
        cognome = jsonReq.get('cognome')
        data_nascita = jsonReq.get('dataNascita')

        Squery ="nome ='" + nome + "',cognome ='" + cognome +"',data_nascita='" + data_nascita + "'"
        sQuery = "update cittadini set "+ Squery +"where codice_fiscale = '" + codice_fiscale + "';"
        print(sQuery)
        iRet = db.write_in_db(cur,sQuery)
        
        if iRet == 0:
            return jsonify({"Esito": "001", "Msg": "Cittadino aggiornato con successo"}), 200
        elif iRet == -2:
            return jsonify({"Esito": "000", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200


# @api.route('/elimina_cittadino', methods=['DELETE'])
# def elimina_cittadino():
#     content_type = request.headers.get('Content-Type')
#     if content_type == 'application/json':
#         cod = request.json.get('codFiscale')
#         if cod in cittadini:
#             del cittadini[cod]
#             JsonSerialize(cittadini, file_path)  
#             return jsonify({"Esito": "000", "Msg": "Cittadino rimosso con successo"}), 200
#         else:
#             return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
#     else:
#         return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200

api.run(host="127.0.0.1", port=8080, ssl_context = "adhoc")

