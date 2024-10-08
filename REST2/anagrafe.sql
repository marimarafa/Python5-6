
CREATE TABLE Cittadini(
    codice_fiscale VARCHAR(16) PRIMARY KEY,
    nome VARCHAR(20),
    cognome VARCHAR(20),
    data_nascita DATE;
)

CREATE TABLE Utenti (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(20),
    privilegi VARCHAR(5),
    note TEXT;
)

INSERT INTO Cittadini (codice_fiscale, nome, cognome, data_nascita)
VALUES 
('dctnst34b56h501u', 'Mario', 'de martino', '1980-05-21'),
('dctnst34b56h501a', 'Gianni', 'de martino', '1980-05-21'),
('dctnst34b56h502w', 'Silvia', 'de martino', '1980-05-21'),
('dtnst34b56h502w','Paolo', 'Rossi','1990-02-24');


INSERT INTO Utenti (username , password, privilegi, note)
VALUES 
('admincomune@comune.zagarolo.it', 'root_01', 'w', 'amministratore del sistema'),
('mariorossi@comune.zagarolo.it', 'mario01', 'w', 'sportello frazione 1'),
('gianni@gmail.com', 'gianni_123', 'r', 'sportello frazione 2');