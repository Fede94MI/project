--idSTUDENTE, VOTO, NOMEDOCENTE


SELECT s.IDStudente,s.Nome,d.NomeDocente,d.IDDocente,e.Voto
FROM Esame AS e
LEFT JOIN Studente AS s
ON s.IDStudente=e.IDStudente
INNER JOIN Corso AS c
ON c.IDCorso=e.IDCorso
INNER JOIN Docente AS d
ON d.IDDocente=c.IDDocente
 
 WHERE e.voto>=28





-------- per ogni docente, nome + nome corso + settore scientifico
SELECT d.IDDocente,d.NomeDocente,c.NomeCorso,e.SettoreScientifico
FROM Corso as c
INNER JOIN Esame as e
ON e.IDCorso=c.IDCorso
INNER JOIN Docente as d
ON d.IDDocente=c.IDDocente
ORDER BY d.NomeDocente



