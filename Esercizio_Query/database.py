import dbclient as db
import sys

cur = db.connect()
#print(cur)
if cur is None:
	print("Errore connessione al DB")
	sys.exit()
     
print("\tCollegamento al Database....\n")
while True :
    op = print("\nScegliere operazione da eseguire:\n1)Aggiungere utente \n2)Cerca utente \n3)Aggiorna utente \n4)Elimina utente ")
    query = input("--> ")

    if query == "1":
        codice_fiscale = input("Inserisci codice fiscale: ")
        nome = input("Inserisci nome: ")
        cognome = input("Inserisci cognome: ")
        data_nascita = input("Inserisci data_nascita: ")

        Squery ="'"+ codice_fiscale +"','" + nome + "','" + cognome +"','" + data_nascita + "'"
        aggiungi_utente = "insert into utente (codice_fiscale, nome, cognome, data_nascita) VALUES (" + Squery + ")"
        iRet = db.write_in_db(cur,aggiungi_utente)

        if iRet == -2:
            print("Utente già esistente")
        elif iRet == 0:
            print("Utente aggiunto con successo")

    elif query == "2":
        codice_fiscale = input("Inserisci codice fiscale: ")
        sQuery1 = "select * from utente where codice_fiscale ='" + codice_fiscale + "';"
        iNumRow = db.read_in_db(cur,sQuery1)
        for _ in range(0,iNumRow):
            myrow = db.read_next_row(cur)
        if iNumRow == 1:
            print("Utente trovato: ", myrow[1])
        elif iNumRow == 0:
            print("Utente non trovato")

    elif query == "3":
        codice_fiscale = input("Inserisci codice fiscale: ")
        nome = input("Inserisci nome: ")
        cognome = input("Inserisci cognome: ")
        data_nascita = input("Inserisci data_nascita: ")

        Squery ="nome ='" + nome + "',cognome ='" + cognome +"',data_nascita='" + data_nascita + "'"
        aggiorna_utente = "update utente set "+ Squery +"where codice_fiscale = '" + codice_fiscale + "';"
        iRet = db.write_in_db(cur,aggiorna_utente)

        if iRet == -2:
            print("Utente già esistente")
        elif iRet == 0:
            print("Utente aggiornato con successo")

    elif query == "4":
        codice_fiscale = input("Inserisci codice fiscale: ")
        elimina_utente = "DELETE FROM utente where codice_fiscale = '" + codice_fiscale + "';"
        iRet = db.write_in_db(cur,elimina_utente)

        if iRet == -2:
            print("Utente non trovato")
        elif iRet == 0:
            print("Utente eliminato con successo")
    else:
        sys.exit()

