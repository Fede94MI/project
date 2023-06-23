SELECT Nome,Cognome,IDManager,DAY(DataAssunzione) as DAY,MONTH(DataAssunzione) as MONTH ,YEAR(DataAssunzione) as YEAR
FROM Dipendente
WHERE IDManager IN (
					SELECT IDManager
					FROM Dipartimento
					WHERE NomeDipartimento='Amministrazione'
					
				);
-----------------------------------------
SELECT Nome, Cognome
FROM Dipendente
WHERE MONTH(DataAssunzione)=6
----------------------------------------------
SELECT YEAR(DataAssunzione), COUNT(IDDipendente)
FROM Dipendente
GROUP BY DataAssunzione
HAVING COUNT(IDDipendente)>10
------------------------------------------------

SELECT *
FROM Dipendente AS DipE
INNER JOIN Dipartimento AS DipA
ON DipA.IDManager=DipE.IDManager

WHERE DipE.IDManager IN (  SELECT IDManager
							FROM Dipendente
							WHERE DATEDIFF(yy,DataAssunzione,GETDATE()) > 5
						)

