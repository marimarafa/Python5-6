import json,requests


base_url = "http://127.0.0.1:8080"


def CreaInterfaccia():
    print("\tOperazioni disponibili")
    print("1. Inserisci cittadino(es. atto di nascita)")
    print("2. Richiedi dati cittadino (es. cert. residenza)")
    print("3. Modifica dati cittadino")
    print("4. Elimina cittadino")
    print("5. Exit")

def RichiedidatiCittadino():
    nome = input("Inserisci nome cittadino: ")
    cognome = input("Inserisci cognome cittadino: ")
    dataNascita = input("inserisci data nascita: ")
    codFiscale = input("Inserisci codice fiscale: ")
    jRequest = {"nome": nome , "cognome" : cognome, "data nascita": dataNascita,"codice fiscale" :codFiscale}
    return jRequest

def RichiediDati():  
    codFiscale = input("Inserisci codice fiscale ")
    return {"codice fiscale" :codFiscale}

CreaInterfaccia()
sOper = input ("\nSeleziona operazione ")
while (sOper != "5"):
    if sOper == "1":
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = RichiedidatiCittadino()
        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)

        except:
            print("\nProblemi di comunicazione con il server.. \tRIPROVA PIU TARDI.")
 
    if sOper == "2":
        api_url = base_url + "/richiedi_dati"
        jsonDataRequest = RichiediDati()
        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            info = data1.pop('info')
            print(data1)
            print(info)

        except:
            print("\nProblemi di comunicazione con il server.. \tRIPROVA PIU TARDI.")


    CreaInterfaccia()
    sOper = input("\nSeleziona operazione ")

    


                                     