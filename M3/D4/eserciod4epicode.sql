/*ESERCIZIO EPICODE D4



1---

SELECT NumPiste,Citta
FROM AEROPORTO
WHERE NumPist IS null

2---

SELECT CittaPart, TipoAereo
FROM VOLO
WHERE CittaPart='Torino'

3----

SELECT CittaPart, CittaArr
FROM VOLO
WHERE CittaArr='Bologna'

4----

SELECT IDVolo, CittaPart, CittaArr
FROM VOLO
Where IDVolo="AZ274"

5---
SELECT TipoAereo, GiornoSett,OraPart, CittaPart, CittaArr
FROM VOLO
WHERE CittaPart LIKE 'B%O%' AND CittaArr 'A%E%'