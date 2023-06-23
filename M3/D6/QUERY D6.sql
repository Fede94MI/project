--- PER OGNI STUDENTE:
---MATRICOLA, NOME, VOTO MASSIMO, VOTO MINIMO, VOTO MEDIO

SELECT s.IDStudente, s.Nome, MAX(e.voto) as MAXVOTO, MIN(e.voto) as MINVOTO, AVG(e.voto) as VOTOMEDIO
FROM Studente AS s
LEFT JOIN Esame AS e
ON e.IDStudente=s.IDStudente
GROUP BY s.IDStudente, s.Nome

-----------------------------
---PER OGNI STUDENTE CON MEDIA MAGGIORE DI 25 E che ha SOSTENUTO ESAMI ALMENO IN 10 DATE, VISUALIZZARE ID, VOTOMAX,VOTOMIN, AVGVOTO, ORDINARE
--PER VOTO
-- CON JOIN

SELECT s.IDStudente, s.Nome, MAX(e.voto) as MAXVOTO, MIN(e.voto) as MINVOTO, AVG(e.voto) as VOTOMEDIO, COUNT(DISTINCT(e.Data)) as CONTOESAMI
FROM Studente AS s
LEFT JOIN Esame AS e
ON e.IDStudente=s.IDStudente
GROUP BY s.IDStudente, s.Nome
HAVING AVG(e.voto)>25 AND count(DISTINCT(e.data))=10


--con select nidificate


SELECT s.IDStudente, s.Nome
FROM Studente AS s
WHERE s.IDStudente IN (  SELECT s.IDStudente
						FROM Studente AS s
						LEFT JOIN Esame AS e
						ON e.IDStudente=s.IDStudente
						GROUP BY s.IDStudente, s.Nome
						HAVING AVG(e.voto)>25 AND count(DISTINCT(e.data))=10
					  )
				













				


