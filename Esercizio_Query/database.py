import dbclient as db
import sys

cur = db.connect()
#print(cur)
if cur is None:
	print("Errore connessione al DB")
	sys.exit()
     
print("\tCollegamento al Database....\n")
while True :
    op = print("\nScegliere operazione da eseguire:\n1)Aggiungere Cittadino \n2)Cerca Cittadino \n3)Aggiorna Cittadino \n4)Elimina Cittadino ")
    query = input("--> ")

    if query == "1":
        codice_fiscale = input("Inserisci codice fiscale: ")
        nome = input("Inserisci nome: ")
        cognome = input("Inserisci cognome: ")
        data_nascita = input("Inserisci data_nascita: ")

        Squery ="'"+ codice_fiscale +"','" + nome + "','" + cognome +"','" + data_nascita + "'"
        aggiungi_cittadino = "insert into cittadini (codice_fiscale, nome, cognome, data_nascita) VALUES (" + Squery + ")"
        iRet = db.write_in_db(cur,aggiungi_cittadino)

        if iRet == -2:
            print("Cittadino già esistente")
        elif iRet == 0:
            print("Cittadino aggiunto con successo")

    elif query == "2":
        codice_fiscale = input("Inserisci codice fiscale: ")
        sQuery1 = "select * from cittadini where codice_fiscale ='" + codice_fiscale + "';"
        iNumRow = db.read_in_db(cur,sQuery1)
        for _ in range(0,iNumRow):
            myrow = db.read_next_row(cur)
        if iNumRow == 1:
            print("Cittadino trovato: ", myrow[1])
        elif iNumRow == 0:
            print("Cittadino non trovato")

    elif query == "3":
        codice_fiscale = input("Inserisci codice fiscale: ")
        nome = input("Inserisci nome: ")
        cognome = input("Inserisci cognome: ")
        data_nascita = input("Inserisci data_nascita: ")

        Squery ="nome ='" + nome + "',cognome ='" + cognome +"',data_nascita='" + data_nascita + "'"
        aggiorna_cittadino = "update cittadini set "+ Squery +"where codice_fiscale = '" + codice_fiscale + "';"
        iRet = db.write_in_db(cur,aggiorna_cittadino)

        if iRet == -2:
            print("Cittadino già esistente")
        elif iRet == 0:
            print("Cittadino aggiornato con successo")

    elif query == "4":
        codice_fiscale = input("Inserisci codice fiscale: ")
        elimina_cittadino = "DELETE FROM cittadini where codice_fiscale = '" + codice_fiscale + "';"
        iRet = db.write_in_db(cur,elimina_cittadino)

        if iRet == -2:
            print("Cittadino non trovato")
        elif iRet == 0:
            print("Cittadino eliminato con successo")
    else:
        sys.exit()

