#ESERCIZIO 1

"""
nome_scuola="Epicode"
index=0

while index < len(nome_scuola):
      print(nome_scuola[index])
      index +=1
      """
      
#ESERCIZIO 2
"""
max=20
cont=0

while cont <= max:
    print(cont)
    cont += 1
"""

#ESERCIZIO 3


""""
esponente=0
fortwo=1
count=0

print("Le prime 10 potenze del 2")
while count < 10:
    print(f"2^{esponente} = {fortwo}")
    esponente += 1
    fortwo *= 2
    count += 1


"""

#ESERCIZIO 4


"""
N= int(input("Dimmi quante potenze base due vuoi visualizzare: "))



print("Le " + str(N)+" potenze del 2")

esponente=0
basedue=1

count=0

while count < N:
    print(f"2^{esponente} = {basedue}")
    esponente += 1
    basedue *= 2
    count += 1
    
"""
#ESERCIZIO 5
"""
studenti=["Alex","Bob","Cindy","Dan","Emma","Faith","Grace","Henry"]
corsi=["Cybersecurity","Data Analyst","Backend","Frontend","Data Analyst","Backend","Frontend"]

if len(studenti) == len(corsi):
      print("Contengono lo stesso numero di elementi")
else:
      print("Non contengono lo stesso numero di elementi")
"""

#ESERCIZIO6
"""
studenti=["Alex","Bob","Cindy","Dan","Emma","Faith","Grace","Henry"]
corsi=["Cybersecurity","Data Analyst","Backend","Frontend"]

index=0

while len(corsi)<len(studenti):

      if   studenti[index] == "Emma":
       corsi.append("Data Analyst")
      elif studenti[index]=="Faith":
       corsi.append("Beckend")
      elif studenti[index]=="Grace":
       corsi.append("Frontend")
      elif studenti[index]=="Henry":
       corsi.append("Cybersecurity")
      
      index += 1

print(corsi)
"""
        
        
      
#ESERCIZIO8
"""
numero = int(input("Inserisci un numero intero positivo: "))

if numero < 0:
    print("Non è possibile calcolare il fattoriale di un numero negativo")
elif numero == 0:
    print("Per convenzione, il fattoriale di 0! è 1")
else:
    fattoriale = 1
    while numero > 1:
        fattoriale *= numero
        numero -= 1
    print("Il fattoriale è", fattoriale)
    
"""
from sympy import symbols, simplify

numero = int(input("Inserisci un numero: "))

if numero == 1 or numero == 0:
      print("Non è un numero primo!")

else:
      numeroviz=numero
      divisore = 2
      fattori = []
    
      while divisore <= numero:
            if numero % divisore == 0:
                  fattori.append(divisore)
                  numero = numero // divisore
            else:
                  divisore += 1


      if len(fattori) == 1 and fattori[0] == numeroviz:
            print(numeroviz, "è un numero primo.")
      else:
            potenze = []
            fattori_set = set(fattori)

            
            while True:
                  if not fattori_set:
                        break
                  fattore = fattori_set.pop()
                  potenza = fattori.count(fattore)
                  espressione = symbols(str(fattore)) ** potenza
                  potenze.append(simplify(espressione))
                 
                  
      print(numeroviz, "non è un numero primo. I suoi fattori sono:", potenze)
     

"""Viene richiesto all'utente di inserire un numero tramite la funzione input(), e il valore inserito viene convertito in intero utilizzando int() e assegnato alla variabile numero.

Viene inizializzato il divisore a 2, poiché il primo fattore primo possibile è 2. La lista fattori viene inizializzata come una lista vuota.

Viene eseguito un ciclo while che continua finché il divisore è minore o uguale al numero da verificare.

All'interno del ciclo, viene verificato se il numero è divisibile per il divisore senza resto utilizzando l'operatore modulo %. Se il resto è zero, significa che il divisore è un fattore del numero.

Se il divisore è un fattore del numero, viene aggiunto alla lista fattori utilizzando il metodo append(). Successivamente, il numero viene ridotto dividendo per il divisore utilizzando l'operatore di divisione intera //.

Se il divisore non è un fattore del numero, viene incrementato di 1 in modo da passare al successivo possibile divisore.

Il ciclo while continua a iterare finché il divisore è minore o uguale al numero. Quando il divisore supera il valore del numero, il ciclo termina.

Infine, viene stampata la lista fattori, che contiene i fattori primi del numero inserito."""

        

#ESERCIZIOO9

"""
stringa1=str(input("Inserisci una stringa: "))


if len(stringa1) >= 6 :
      print(stringa1[0:3]+"..."+stringa1[-3:])
      
 
else:
      if len(stringa1) > 4 :
            print(stringa1[0:2]+"..."+stringa1[-3:])
      elif len(stringa1) == 3:
                  print(stringa1[0:1]+"..."+stringa1[-2:])
      else:
            print(stringa1)
            
"""  
      
 
      
    
      
      

