CREATE TABLE Laureato (
MatricolaLaureato INT,
NomeLaureato VARCHAR (25),
AnnoLaurea DATE,
TitoloStudio VARCHAR (25),
VotoLaurea INT,
CONSTRAINT PK_MatricolaLaureato PRIMARY KEY (MatricolaLaureato));

CREATE TABLE Dipartimento (
CodiceDipartimento INT,
NomeDipartimento VARCHAR (25),
SettoreScientifico VARCHAR (25),
NumDocenti INT,
CONSTRAINT PK_CodiceDipartimento PRIMARY KEY (CodiceDipartimento));

CREATE TABLE ConcorsoMaster (
CodiceMaster INT,
CodiceDipartimento INT,
DataPubblicazione DATE,
DataScadenza DATE,
NumPostiDisponibili INT,
CONSTRAINT PK_CodiceMaster PRIMARY KEY (CodiceMaster),
CONSTRAINT FK_CodiceDipartimento FOREIGN KEY (CodiceDipartimento) REFERENCES Dipartimento(CodiceDipartimento));

CREATE TABLE Partecipanti (
CodiceDipartimento1 INT,
CodiceMaster INT,
MatricolaStudente INT,
DataInvioDomanda DATE,
CONSTRAINT FK_CodiceDipartimento1 FOREIGN KEY(CodiceDipartimento1) REFERENCES Dipartimento(CodiceDipartimento),
CONSTRAINT FK_CodiceMaster FOREIGN KEY(CodiceMaster) REFERENCES ConcorsoMaster(CodiceMaster),
CONSTRAINT FK_MatricolaStudente FOREIGN KEY(MatricolaStudente) REFERENCES Laureato(MatricolaLaureato));


INSERT INTO Laureato 
VALUES (1, 'Claudia Locci','2019','Economia aziendale',103), (2, 'Michele Rossi','2020','Ingegneria Gestionale',98),  (3, 'Daniele Bianchi','2020','Marketing',108),
(4, 'Rosa Viva','2021','Giurisprudenza',110),  (5, 'Gaia Peis','2019','Comunicazione Impresa',108);

INSERT INTO Dipartimento
VALUES (10,'ComunicazioneEconomia','SocietàCultura',20), (14,'Giurisprudenza','SocietàCultura',30),(11,'Economia','SocietàCultura',20);

INSERT INTO ConcorsoMaster
VALUES (1,10,'01/02/2023','30/06/2023',5),(2,10,'20/01/2023','15/04/2023',2),(3,14,'01/03/2022','06/06/2022',10),(4,14,'10/04/2023','05/06/2023',10)
,(5,11,'01/03/2023','01/04/2023',12),(6,11,'01/06/2023','31/07/2023',25);

INSERT INTO Partecipanti
VALUES (10,1,5,'20/04/2023'),(10,2,2,'12/02/2023'),(14,3,4,'30/05/2023'),(11,5,3,'15/03/2023');

/*Per ogni studente che ha partecipato a 3 concorsi di master, visualizza il nome dello studente e il settore scientifico
per cui ha partecipato a tutti i concorsi. ordina per nome dello studente*/

SELECT
		L.NomeLaureato
		, P.MatricolaStudente
		, COUNT(P.CodiceMaster) AS Concorsi
		,D.SettoreScientifico
FROM Laureato AS L
INNER JOIN Partecipanti AS P
ON L.MatricolaLaureato = P.MatricolaStudente
INNER JOIN Dipartimento AS D
ON P.CodiceDipartimento1 = D.CodiceDipartimento
GROUP BY P.MatricolaStudente, L.NomeLaureato, D.SettoreScientifico
HAVING COUNT (DISTINCT(P.CodiceMaster)) = 1
ORDER BY L.NomeLaureato ASC




/*Per i dipartimenti in cui sono stati effettuati solo concorsi di master aventi ciascuno un numero di posti disponibili
> 7, visualizzare il nome del dipartimento, il settore scientifico di afferenza e il n di concorsi di master. Ordina per nome
del dipartimento e settore scientifico*/

SELECT
	D.NomeDipartimento
	,D.SettoreScientifico
	,COUNT(M.CodiceMaster) AS NumConcorsi
FROM ConcorsoMaster AS M
INNER JOIN Dipartimento AS D
ON M.CodiceDipartimento = D.CodiceDipartimento
WHERE M.NumPostiDisponibili > 7
GROUP BY D.NomeDipartimento, D.SettoreScientifico 
ORDER BY d.NomeDipartimento ASC, D.SettoreScientifico ASC

/* LAUREATO (Matricola, NomeStudente, AnnoLaurea, TitoloStudio, VotoLaurea)
DIPARTIMENTO (CodiceDipartimento, NomeDipartimento, Settore-scientifico, NumDocenti)
CONCORSOMASTER (CodiceMaster, COdiceDipartimento, DataPubblicazione, DataScadenza, NumPostiDisponibili)
PARTECIPACONCORSOMASTER (CodiceDipartimento, CodiceMaster, MatricolaStudente, DataInvioDomanda)*/


/*Visualizza la matricola e il nome degli studenti che hanno conseguito un voto di laurea > 100 ed hanno partecipato
ad almeno due concorsi di master con la stessa data di pubblicazione*/

SELECT
	L.MatricolaLaureato
	,L.NomeLaureato
	,C.DataPubblicazione
FROM Laureato AS L
INNER JOIN Partecipanti AS P
ON L.MatricolaLaureato = P.MatricolaStudente
INNER JOIN ConcorsoMaster AS C
ON P.CodiceMaster = C.CodiceMaster
WHERE L.VotoLaurea > 100 
GROUP BY L.MatricolaLaureato, L.NomeLaureato, C.DataPubblicazione
HAVING COUNT(C.CodiceMaster) >= 1
/* LAUREATO (Matricola, NomeStudente, AnnoLaurea, TitoloStudio, VotoLaurea)
DIPARTIMENTO (CodiceDipartimento, NomeDipartimento, Settore-scientifico, NumDocenti)
CONCORSOMASTER (CodiceMaster, COdiceDipartimento, DataPubblicazione, DataScadenza, NumPostiDisponibili)
PARTECIPACONCORSOMASTER (CodiceDipartimento, CodiceMaster, MatricolaStudente, DataInvioDomanda)*/
/*Visualizza la matricola e il nome degli studenti che hanno conseguito un voto di laurea > 100 ed hanno partecipato
ad almeno due concorsi di master con la stessa data di pubblicazione*/





SELECT L.MatricolaLaureato, L.NomeLaureato, l.VotoLaurea
FROM Laureato AS l
WHERE l.VotoLaurea >=100 AND L.MatricolaLaureato IN (
														SELECT p.MatricolaStudente
														FROM Partecipanti p
														INNER JOIN Partecipanti AS p2 
														ON p.MatricolaStudente = p2.MatricolaStudente
														INNER JOIN ConcorsoMaster AS c 
														ON p.CodiceMaster = c.CodiceMaster
														INNER JOIN ConcorsoMaster C2
														ON p2.CodiceMaster = c2.CodiceMaster
														WHERE c.DataPubblicazione = c2.DataPubblicazione
														GROUP BY p.MatricolaStudente
														HAVING COUNT(DISTINCT c.CodiceMaster) >= 1
													);



/*Questa query seleziona gli studenti dalla tabella Laureato che hanno partecipato ad almeno due concorsi di master con la stessa data di pubblicazione tra di loro. 
La subquery innestata unisce la tabella Partecipanti con se stessa per trovare le corrispondenze tra gli studenti che partecipano a più concorsi. 
Successivamente, vengono unite le tabelle ConcorsoMaster per confrontare le date di pubblicazione dei concorsi. 
La clausola WHERE CM1.DataPubblicazione = CM2.DataPubblicazione filtra solo i concorsi con la stessa data di pubblicazione. 
Infine, viene eseguito un raggruppamento per la matricola dello studente e la condizione HAVING COUNT(DISTINCT CM1.CodiceMaster) >= 2 
assicura che siano selezionati solo gli studenti che hanno partecipato ad almeno due concorsi con la stessa data di pubblicazione tra di loro.*/

SELECT l.MatricolaLaureato, l.NomeLaureato, l.VotoLaurea, l.TitoloStudio
FROM Laureato l
WHERE l.VotoLaurea >=100 AND l.MatricolaLaureato IN (
														SELECT p.MatricolaStudente
														FROM Partecipanti AS p
														INNER JOIN Partecipanti AS pbis
														ON p.CodiceMaster = pbis.CodiceMaster
														INNER JOIN ConcorsoMaster AS c  
														ON pbis.CodiceMaster = c.CodiceMaster
														WHERE p.MatricolaStudente <> pbis.MatricolaStudente
														GROUP BY p.MatricolaStudente, c.DataPubblicazione
														HAVING COUNT(DISTINCT c.CodiceMaster) >= 2
													);
/*Questa query seleziona gli studenti dalla tabella Laureato che hanno partecipato ad almeno due concorsi di master con la stessa data di pubblicazione tra di loro. 
La subquery innestata unisce la tabella Partecipanti con se stessa per trovare le corrispondenze tra gli studenti che partecipano a più concorsi. 
La condizione P1.MatricolaStudente <> P2.MatricolaStudente garantisce che gli studenti selezionati siano diversi tra loro. 
Vengono quindi unite le tabelle Partecipanti e ConcorsoMaster per confrontare le date di pubblicazione dei concorsi. 
La clausola GROUP BY P1.MatricolaStudente, CM.DataPubblicazione raggruppa i risultati per la matricola dello studente e la data di pubblicazione del concorso. 
Infine, la condizione HAVING COUNT(DISTINCT CM.CodiceMaster) >= 2 
assicura che siano selezionati solo gli studenti che hanno partecipato ad almeno due concorsi con la stessa data di pubblicazione tra di loro.*/


SELECT
    L.MatricolaLaureato
    ,L.NomeLaureato
    ,C.DataPubblicazione
    , COUNT(*) AS Conteggio
FROM Laureato AS L
INNER JOIN Partecipanti AS P
ON L.MatricolaLaureato = P.MatricolaStudente
INNER JOIN ConcorsoMaster AS C
ON P.CodiceMaster = C.CodiceMaster
WHERE L.VotoLaurea > 100 
GROUP BY L.MatricolaLaureato, L.NomeLaureato, C.DataPubblicazione
HAVING COUNT(C.DataPubblicazione) >= 2

-- in alternativa al (ma è ridondante)
SELECT
    L.MatricolaLaureato
    ,L.NomeLaureato
    ,C.DataPubblicazione

FROM Laureato AS L
INNER JOIN Partecipanti AS P
ON L.MatricolaLaureato = P.MatricolaStudente
INNER JOIN ConcorsoMaster AS C
ON P.CodiceMaster = C.CodiceMaster
WHERE L.VotoLaurea > 100 
AND L.MatricolaLaureato IN ( 
                                SELECT P.MatricolaStudente
                                FROM ConcorsoMaster AS C
                                INNER JOIN Partecipanti AS P
                                ON C.CodiceMaster = P.CodiceMaster
                                GROUP BY  P.MatricolaStudente, C.DataPubblicazione
                                HAVING COUNT(C.DataPubblicazione) > 1)
GROUP BY L.MatricolaLaureato, L.NomeLaureato, C.DataPubblicazione