
# Utilizzeremo 

import requests, json, sys

# recupero un chiave API da google: (per crearla bisogna andare su Google API studio, richiderla e verrà generata)
# chiave API generata:
Google_API_KEY = 'AIzaSyAuSck01KyLt-2sdFgNtbOoWQdDYj4-PIg'
sModel = "gemini-1.5-pro-exp-0827" # scegliamo un modello di google gemini 
base_url = "https://generativelanguage.googleapis.com/v1beta/models/" + sModel + ":generateContent?key="  # creiamo la base dell'Url inserendo anche il modello 
api_url = base_url + Google_API_KEY 


print("Benvenuti su Google Gemini")

iFlag = 0
while iFlag==0:
    print("\nOperazioni disponibili:")
    print("1. Inserisci una domanda: ")
    print("2. inserisci una coppia (file, domanda): ")
    print("3. Esci")

    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue

    iOper = int(input("inserisci opzione: "))
    if iOper == 1:
        s_query =input("Cosa vui chiedere ?")
        jsonDataRequest = {"contents": [{"parts":[{"text": s_query}]}]} # questa è il tipo di domanda che google si aspetta 
        response = requests.post(api_url, json=jsonDataRequest, verify=True) # facciamo la richiesta (contenuta all'interno del Json)
        if response.status_code == 200: # verifichiamo che lo stato della risposta sia giusto (se è 200 di solito significa che la richiesta è stata ricevuta con successo e fornisce in risposta il contenuto richiesto)
            print(response.json())
        else:
            print("attezione risposta errata")  

    elif iOper == 2:
        print("servizio da gestire")

    elif iOper == 3:
        print("Buona giornata!")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprovare")





