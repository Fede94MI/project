"""Abbiamo la stringa:
nome_scuola = "Epicode"
Stampare ogni carattere della stringa, uno su ogni riga, utilizzando un costrutto
for."""

nome_scuola = "Epicode"

for elemento in nome_scuola:
    print("-", elemento)
    
"""Esercizio
Abbiamo una serie di simboli di elementi chimici (tutti da una sola lettera)
all'interno della variabile elementi:
elementi = "NPKOHC"
Stampare ogni elemento su una riga diversa."""

elementi = "NPKOHC"

for elemento in elementi:
    print(elemento)
    
    
"""Esercizio
Abbiamo una serie di simboli di elementi chimici (tutti da una sola lettera)
all'interno della variabile elementi:
elementi = "NPKOHC"
Stampare ogni elemento su una riga diversa, preceduto dalla scritta "elemento –".
"""

elementi = "NPKOHC"

for elemento in elementi:
    print("-", elemento)
    
    
"""Abbiamo una serie di simboli di elementi chimici (tutti da una sola lettera)
all'interno della variabile elementi:
elementi = "NPKOHC"
Stampare ogni elemento su una riga diversa, preceduto dalla scritta "elemento
– numero n" dove al posto di n scriveremo un numero progressivo che parte
da 1."""
elementi = "NPKOHC"

for i, elemento in enumerate(elementi, start=1):
    print(i, elemento)

"""Esercizio
Modificare la parola "marmalade" in modo sostituire le "e" con le "a" e
viceversa.
Salvare il risultato in una variabile e stamparla a video.
Fare diverse versioni:
• una con un ciclo for,
• una con un ciclo while,
• una con il metodo delle stringhe .replace()."""

#CON CICLO FOR


stringa = "marmalade"
nuova_stringa = list(stringa)

for i in range(len(nuova_stringa)):
    if nuova_stringa[i] == "e":
        nuova_stringa[i] = "a"
    elif nuova_stringa[i] == "a":
        nuova_stringa[i] = "e"

stringa="".join(nuova_stringa)
print(stringa)

#CICLO WHILE
   
index = 0

string = "marmalade"
lista_stringa = list(string)

i = 0

while i < len(lista_stringa):
    if lista_stringa[i] == "e":
        lista_stringa[i] = "a"
        i += 1
    elif lista_stringa[i] == "a":
        lista_stringa[i] = "e"
    i += 1

stringa = "".join(lista_stringa)
print(stringa)

#METODO STRINGHE

parola = "marmalade"

parola = parola.replace("e", "@").replace("a", "e").replace("@", "a")
print(parola)


"""Calcolare e stampare tutte le prime 10 potenze di 2 utilizzando un ciclo for.
Utilizzeremo:
• la funzione range(), e.g.:
for contatore in range(10):
pass # modificare qui
Calcolare (ma non stampare) le prime N potenze di 2; ognuna di esse andrà
memorizzata in coda a una lista.
Alla fine, stampare la lista risultante.
Realizzare due versioni:
• con un ciclo while,
• con un ciclo for."""

#LOOPING FOR INDEX
potenza_2=[]
n = 10

for contatore in range(n):
    potenza_2.append(2**contatore)
    
print(potenza_2)

#WHILE

potenza_2=[]
count = 0
n=0

while count < n:
    potenza_2.append(2**count)
    count += 1
    
print(potenza_2)



"""Esercizio
Calcolare (ma non stampare) le prime N potenze di 3; ognuna di esse andrà
memorizzata in coda a una lista.
Alla fine, stampare la lista risultante.
Realizzare due versioni:
• con un ciclo while,
• con un ciclo for."""

# LOOPING FOR INDEX
potenza_3=[]

for contatore in range(10):
    potenza_3.append(3**contatore)
    
print(potenza_3)


#WHILE

potenza_3=[]
count = 0
n=0

while count < n:
    potenza_3.append(3**count)
    count += 1
    
print(potenza_3)

"""
Esercizio
Calcolare (ma non stampare) le prime N=esponente potenze di K=numero; ognuna di esse andrà
memorizzata in coda a una lista.
Alla fine, stampare la lista risultante.
Proviamo con diversi valori di K, oppure facciamola inserire all'utente.
Realizzare due versioni:
• con un ciclo while,
• con un ciclo for.
"""

#The range() function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and stops before a specified number.
# range(start, stop, step
#start	Optional. An integer number specifying at which position to start. Default is 0
#stop	Required. An integer number specifying at which position to stop (not included).
#step	Optional. An integer number specifying the incrementation. Default is 1

#LOOP è un blocco di codice che si ripete fintanto che la condizioni sia "soddisfatta"
#ESISTONO DUE TIPI DI LOOPS:
# FOR loops : si ripete per un numero specifico di elementi "PER QUANTI ELEMENTI" e spesso corrisponde
# alla lunghezza dela lista, tupla o altro elemento iterabile
#E' meglio utilizzarlo se si conosce quante volte il codice si ripete

k = int(input("Inserisci un numero: ")) # 6
n = int(input("Inserisci quante 'n' potenze vuoi calcolare: ")) #10
potenza=[]
# 6^0 , 6^1, 6^2, 6^3 ... 6^9


for i in range(n):
    potenza.append(k**i)

print(potenza)

#WHILE loops: itera fintanto che la condizione logica sia soddisfatta
#"FINTANTO CHE E' VERO"
#Si utilizza spesso quando non si conosce quante volte il blocco di codice dovrà essere iterato

k = int(input("Inserisci un numero: ")) 
n = int(input("Inserisci quante 'n' potenze vuoi calcolare: ")) 
potenza = []
contatore = 0

while contatore < n:
    potenza.append(k**contatore)
    contatore += 1
    
print(potenza)


#Calcolare,stampare e salvare tutte le potenze di 2 minori di 25000.

# 2**contatore < 25000 STAMPA, altrimenti no


#The append() method appends an element to the end of the list.
#SYNTAX :  list.append(elmnt)

lista= []

for i in range(1000):
    if 2**i < 25000:         #IF viene eseguito prima dell'append perché altrimenti restituisce "OUT OF RANGE LIST" in quanto lista vuota
         lista.append(2**i)
         
print(lista)
        
#WHILE LOOPS

lista = []
contatore = 0

while  2**contatore < 25000:
    lista.append(2**contatore)
    contatore += 1
    
print(lista)

#WHILE TRUE con BREAK


while True:
        if 2**contatore <= 25000:
            lista.append(2**contatore)
        else:
            break
        
print(lista)

#Calcolare e stampare tutte le potenze di 2 minori di un certo numero N.

lista= []
 
n= 5000

for i in range(n):
    if 2**i < n:            
         lista.append(2**i)

print(lista)


#13 Esercizio
#Calcolare e stampare tutte le prime 100 potenze di 2, ogni 3 (e.g. 2⁰, 2³, 2⁶, 2⁹,…).
#Oltre a stamparle, memorizzarle in coda a una lista e stamparla alla fine.
#Usate due metodi diversi:

#1. usare un costrutto for e range(100), e poi un costrutto if per visualizzare
#e memorizzare solo ogni 3
# %	Modulus will return the remainder of standard Euclidean division
#Be careful! Just like with the division operator (/), 
# Python will return a ZeroDivisionError if you try to use the modulo operator with a divisor of 0

lista=[]

for i in range(100):   #0,1,2,3,4  ... 99
    if i % 3 == 0:         
        lista.append(2**i)
        
print(lista)


#2. usare un costrutto for e range(0, 100, 3)

lista= []
for i in range(0,100,3):
    lista.append(2**i)
    
print(lista)


"""Abbiamo una lista con dei numeri:
numeri = [4, 9, 5, 1, 7, 10, 2, 3]
utilizzando un costrutto for, trovare il massimo di questa lista e stamparlo a
video."""



#LIST è un tipo di dato multi valore che può contenere duplicati, può essere modificato, cancellato e permette l'inserimento
#di nuovi dati. LIST = [], list = set()

#METODI lista

numeri = [4, 9, 5, 1, 7, 10, 2, 3]
print(max(numeri))

#LOOPING OVER ITEMS
numeri = [4, 9, 5, 1, 7, 10, 2, 3]
max = numeri[0]

for numero in numeri:   
    if numero > max:
        max = numero

print(max)
        
    
#LOOPING OVER INDEX
numeri = [4, 9, 5, 1, 7, 10, 2, 3]

for i in range(len(numeri)):  # 0 ... i-1
    if numeri[i] > numeri[0]:  #2 iterazione [9, 9, 5, 1, 7, 10, 2, 3]  ... i-esima iterazione [10, 9, 5, 1, 7, 10, 2, 3]
        numeri[0] = numeri[i]
        
print(numeri[0])
                      
"""Esercizio
Abbiamo raccolto tutte le età degli studenti in una lista:
eta_studenti = [20, 30, 40, 50, 60]
utilizzando un ciclo for, calcolare la media delle età. Alla fine, stampa (a video)
il risultato."""

#AVG non esiste un metodo. La Media Aritmetica è la:  x1 + ... + xn / n  = sum(lista)/len(lista)

#METHOD list
eta_studenti = [20, 30, 40, 50, 60]

media_eta = sum(eta_studenti)/len(eta_studenti)
    
print(media_eta)

#FOR loops

#LOOPING FOR ITEMS

eta_studenti = [20, 30, 40, 50, 60]

eta_somma = 0

for eta in eta_studenti:
    eta_somma += eta
    
print(eta_somma/len(eta_studenti))
    
    
#LOOPING FOR INDEX

eta_studenti = [20, 30, 40, 50, 60]
somma_eta = 0

for i in range(len(eta_studenti)):
    somma_eta += eta_studenti[i]
    
print(somma_eta/len(eta_studenti))

"""Esercizio
Abbiamo una lista con i guadagni degli ultimi 12 mesi:
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]
usando un costrutto for, calcolare la media dei guadagni e stamparla a video."""

#METHOD list
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

media_guadagni = sum(guadagni)/len(guadagni)

print(media_guadagni)

#FOR loops

#LOOPING FOR INDEX

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]
sum_guadagni = 0

for i in range(len(guadagni)):
    sum_guadagni += guadagni[i]
    
print(sum_guadagni/len(guadagni))

"""Esercizio
Abbiamo una lista con i guadagni degli ultimi N mesi:
guadagni = [100, 90, 70, 40, 50, 80, 90, 120]
usando un costrutto for, calcolare la media dei guadagni e stamparla a video;
stampare anche il numero di mesi considerati."""

"""Esercizio
Abbiamo una lista con i guadagni degli ultimi N mesi:
guadagni = [100, 90, 70, 40, 50, 80, 90, 120]
usando un costrutto for, calcolare la media dei guadagni e stamparla a video;
stampare anche il numero di mesi considerati."""

guadagni = [100, 90, 70, 40, 50, 80, 90, 120]
mesi = [1,2,3,4,5,6,7,8,9,10,11,12]
start_range = int(input ("Inserisci il numero del mese iniziale da cui vuoi calcolare la media: "))
finish_range= int(input ("Inserisci il numero del mese finale da cui vuoi calcolare la media: "))


sum_guadagni = 0

if start_range and finish_range in mesi:
    for i in range(len(guadagni[start_range-1:finish_range])):
        sum_guadagni += guadagni[i]
        

media= sum_guadagni/(len(guadagni[start_range-1:finish_range]))     
print("La media dei primi ", finish_range, 'mesi è di: ', media)
        

"""Abbiamo una lista di studenti:
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace",
"Henry"]
utilizzare un ciclo for per stampare i nomi di tutti gli studenti con questa formattazione:
Studenti:
- Alex
- Bob
- Cindy
"""

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace","Henry"]

##LOOPING OVER INDICES
for i in range(len(studenti)):
    print("-", studenti[i])

##LOOPING OVER ITEMS  
for studente in studenti:
    print("-",studente)


"""Abbiamo tre liste (sono tutte della stessa lunghezza):
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace",
"Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend",
"Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]
stampare a video, usando print(), ogni studente che corso segue e di che edizione,
e.g.:
Alex segue Cybersecurity, edizione 1
Bob segue Data Analyst, edizione 2
...
facendo in modo che non ci sia uno spazio tra il corso e la virgola subito dopo"""

#ZIP() function creates an iterator that will aggregate elements from two or more iterables. 
# You can use zip to iterate over multiple objects at the same time. 
# Zip returns tuples that can be unpacked as you go over the loop.

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace","Henry"]

corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend","Data Analyst", "Backend", "Frontend", "Cybersecurity"]

edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

for student, course, ed in zip (studenti,corsi,edizioni):
    print(f"{student} segue {course}, edizione {ed}")
    
    
"""Abbiamo una lista di parole:
parole = ["Albergo", "Sedia", "Borgo", "Petalo",
"Belvedere", "Semestre", "Sosta", "Orpello", "Abete"]
stampiamo, per ogni parola, quante volte appare la lettera "e"."""

#The count() method returns the number of occurrences of a substring in the given string. It's case sensitive!!

##LOOPING OVER ITEMS
parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Belvedere", "Semestre", "Sosta", "Orpello", "Abete"]
letter="e"
for parola in parole:
    count = parola.count(letter)
    print((parola + ' ')*count)

#LOOPING OVER INDEX

parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Belvedere", "Semestre", "Sosta", "Orpello", "Abete"]
letter="e"
for i in range(len(parole)):
    count = parole[i].count(letter)
    print(str(parole[i]+ ' ') *count)

"""Esercizio
Abbiamo una lista di parole:
parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Eremo",
"Belvedere", "Semestre", "Esteta", "Sosta", "Orpello",
"Abete", "Orologio", "Cesta", "Ermellino"]
stampiamo, per ogni parola, quante volte appare la lettera "e"; facciamo
attenzione al fatto che appare sia maiuscola che minuscola."""

#LOOPING OVER ITEMS
for parola in parole:
    count = parola.lower().count('e')
    print((parola + ' ')*count)

#LOOPING OVER INDEX

for i in range(len(parole)):
    count=parole[i].lower().count('e')
    print(str(parole[i]+ ' ')*count)
    
"""Abbiamo una lista di codici fiscali:
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]
trovare i codici fiscali che contengono "95", metterli in una lista, e alla fine
stamparla. """

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]

#LOOPING OVER ITEMS
new_cf = []

for cf in lista_cf:
    if "95" in cf:
        new_cf.append(cf)
        
print(new_cf)

#LOOPING OVER INDICES
new_cf=[]

for i in range(len(lista_cf)):
    if lista_cf[i].find('95') != -1:    #METHOD string.find('valuestosearch' ) If not found, it returns -1.
        new_cf.append(lista_cf[i])
        
print(new_cf)


"""Abbiamo una lista di codici fiscali:
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]
Per ognuno di essi, stampare a video i caratteri relativi al nome e quelli relativi al
cognome."""

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]

 #LOOPING OVER ITEMS
for cf in lista_cf:
    print(cf[0:6])
    
  #LOOPING OVER INDEX   
for i in range(len(lista_cf)):
    print(lista_cf[i][0:6])
    
    
"""Esercizio
Abbiamo tre liste della stessa lunghezza:
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace",
"Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend",
"Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]
dove ogni elemento nella medesima posizione si riferisce ai dati dello stesso studente.
Stampare a video tutti e soli gli studenti che frequentano una prima edizione; utilizzare
solo i dati necessari."""

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace",
"Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend",
"Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

#ENUMERATE
for index, studente in enumerate(studenti):
    if edizioni[index] == 1:
     print(f"{studente} segue {corsi[index]}, edizione {edizioni[index]}")
 
 #ZIP 
for studente, corso, edizione in zip (studenti,corsi,edizioni):
    if edizione == 1:
         print(f"{studente} segue {corso}, edizione {edizione}")
 
 """E' come se avessimo 3 tabelle 
                              STUDENTI: IDStudente, NomeStudente
                              CORSI: IDCorso, DescrizioneCorse
                              EDIZIONI: IDStudente, IDCorso, IDEdizione
                              
ID Studente | Nome Studente
----------------------------
1           | Alex
2           | Bob
3           | Cindy
4           | Dan
5           | Emma
6           | Faith
7           | Grace
8           | Henry

ID Corso | Nome Corso
--------------------
1        | Cybersecurity
2        | Data Analyst
3        | Backend
4        | Frontend

ID Studente | ID Corso | Numero Edizione
--------------------------------------
1           | 1        | 1
2           | 2        | 2
3           | 3        | 3
4           | 2        | 2
5           | 2        | 2
6           | 1        | 1
7           | 3        | 3
8           | 3        | 3



Replichiamo SQL in Python


studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace",
"Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend",
"Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

findstudent='Alex'
indexstudent=studenti.index(findstudent)

course=corsi[indexstudent]

print(f"{findstudent} segue il corso {course}")

"""

"""Creiamo un dizionario che assegni ad ogni proprietario la sua auto, sapendo
che:
• Ada guida una Punto
• Ben guida una Multipla
• Charlie guida una Golf
• Debbie guida una 107 Poi stampiamo il dizionario per intero, e poi l'auto
associata a Debbie."""

#DICT Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

proprietari_auto = { 'Ada' : 'Punto',
                     'Ben' : 'Multipla',
                     'Charlie' : 'Golf',
                     'Debbie'   : '107'
                    }

print(proprietari_auto)
print(proprietari_auto['Debbie'])

"""Abbiamo un dizionario che assegni ad ogni proprietario la sua auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}
Aggiungere i proprietari Emily e Fred che posseggono rispettivamente una A1 e
una Octavia; eliminare i dati relativi a Ben.
Stampare il dizionario per controllare che sia tutto corretto."""

proprietari_auto = { 'Ada' : 'Punto',
                     'Ben' : 'Multipla',
                     'Charlie' : 'Golf',
                     'Debbie'   : '107'
                    }

proprietari_auto['Emily'] = 'A1'       #Aggiungere chiave : valore al dizionario
proprietari_auto['Fred'] = 'Octavia'
del proprietari_auto['Ben']            #Eliminare , tramite la chiave, il chiave:valore contenuto nel dizionario

print(proprietari_auto)


"""Abbiamo due dizionari che assegnano ad ogni proprietario la propria auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107", "Emily": "A1"}
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia",
"Grace": "Yaris", "Hugh": "Clio"}
Aggiornare il dizionario dizionario_auto con i dati contenuti in
nuovi_proprietari e stamparlo. Cosa è successo a Ben? E' STATO SOVRASCRITTO
"""

proprietari_auto = { 'Ada' : 'Punto',
                     'Ben' : 'Multipla',
                     'Charlie' : 'Golf',
                     'Debbie'   : '107'
                    }

proprietari_auto_new = ({'Ben': 'Polo', 'Fred': 'Octavia',
'Grace': 'Yaris', 'Hugh': 'Clio'})

proprietari_auto.update(proprietari_auto_new)    #Method DICT per aggiungere un dizionario ad un altro, sovrascrive qualora trova corrispondenza della chiave

print(proprietari_auto)

"""Abbiamo un dataset che assegna ad ogni proprietario la propria auto, in forma
di dizionario:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107", "Emily": "A1", "Fred":
"Octavia", "Grace": "Yaris", "Hugh": "Clio"}
Viene richiesto di ricercare in questo dataset i dati di Hugh, Ada, Emily e
Debbie, e visualizzare le auto relative."""

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107", "Emily": "A1", "Fred":
"Octavia", "Grace": "Yaris", "Hugh": "Clio"}

lista_proprietari = ['Hugh','Ada','Emily','Debbie']



for proprietario in lista_proprietari:
    if proprietario in dizionario_auto:
        print(proprietario , ' ', dizionario_auto[proprietario])
        
"""Abbiamo un dataset che assegna ad ogni proprietario la propria auto, in forma di
dizionario:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie":
"Golf", "Debbie": "107", "Emily": "A1", "Fred": "Octavia", "Grace":
"Yaris", "Hugh": "Clio"}
Viene richiesto di ricercare in questo dataset i dati di Ada, Emily, Jade, Ben, Hugh, Kelly e
Charlie, e visualizzare le auto relative.
Non tutti i dati potrebbero essere presenti nel dataset, quindi quando un nome non è
presente visualizzeremo un messaggio adeguato."""  

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie":
"Golf", "Debbie": "107", "Emily": "A1", "Fred": "Octavia", "Grace":
"Yaris", "Hugh": "Clio"}


lista_proprietari = ['Ada', 'Emily', 'Jade', 'Ben', 'Hugh','Kelly','Charlie']

for proprietario in lista_proprietari:
    if proprietario in dizionario_auto:
        print(proprietario , ' ', dizionario_auto[proprietario])
    else:
        print(proprietario, "non presente in memoria")
        
"""Abbiamo un dizionario:
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
utilizzando il metodo .keys(), stampiamone tutte le chiavi."""


diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}

print(diz.keys())   #METHOD KEY restituisce le chiavi del DICT

for key in diz.keys():  #LOOP FOR
    print(key)
    
"""Abbiamo un dizionario:
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
utilizzando il metodo .values(), stampiamone tutte i valori."""

diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}

print(diz.values())          #METHOD VALUES restituisce i valori del DICT

for values in diz.values():  #LOOP FOR
    print(values)
    
"""diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
utilizzando il metodo dei dizionari .items() stampate le coppie chiave-valore
presenti nel dizionario su righe diverse"""

diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}

for key, value in diz.items():    #Method dict.items() restituisce la coppia chiave-valore
    print(key, value)              #Se inserisco solo un valore nel FOR, restituisce una TUPLA, se inserisco entrambe, restituirà due STR
        
    

"""diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
utilizzando il metodo dei dizionari .values(), calcolare il valore massimo, il
valore minimo, la somma, e stampiamo i risultati.  """

diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}

print(sum(diz.values()))
print(max(diz.values()))
print(min(diz.values()))

"""Abbiamo un dizionario che assegna ad ogni proprietario la sua auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}
Con un ciclo for, e usando il metodo .items(), stampiamo ogni proprietario
e la sua auto, formattandolo come:
Ada guida una Punto
Ben guida una Multipla
...
"""

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}

for proprietario, auto in dizionario_auto.items():
    print(f"{proprietario} guida una {auto}")
    


"""Abbiamo un dizionario che assegna ad ogni proprietario la sua auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}
Con un ciclo, e usando il metodo .values(), stampiamo a video tutte le auto
che non sono una Multipla."""

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}

for car in dizionario_auto.values():
    if car != 'Multipla':
        print(car)


"""Abbiamo i seguenti dati riguardo dei collezionisti e le loro collezioni:
• Ada ha 10 Funko Pop, 5 action figures e 35 manga
• Ben ha 2 Funko Pop, 6 action figures, 40 manga e 2 graphic novels
• Charlie ha 31 action figures e 18 graphic novels
• Debbie ha 1 Funko Pop, 9 graphic novels, 25 manga e 2 action figures
Creare dei dizionari innestati che contengano questi dati, e quindi visualizzarli."""

#PRIMO APPROCCIO- DICT di DICT con LISTE
collezionisti = { 
                 'Collezionista': { 'Collezione' : ['Funko Pop', 'Action Figures', ' Manga', 'Graphic Novels'] },
                 'Ada': { 'Collezione' : [10, 5, 35, None] },
                 'Ben': { 'Collezione' : [2, 6, 40, 2] },
                 'Charlie' : { 'Collezione' : [31, None, None, 18] },
                 'Debbie' : { 'Collezione' : [1, 2, 25, 9] }
                }

print(str(collezionisti['Collezionista']))
print(str(collezionisti['Ada']))
print(str(collezionisti['Ben']))
print(str(collezionisti['Charlie']))
print(str(collezionisti['Debbie']))

#DICT DI DICT DI DICT

collezionisti = {
    'Ada': {
        'Funko Pop': 10,
        'Action Figures': 5,
        'Manga': 35
    },
    'Ben': {
        'Funko Pop': 2,
        'Action Figures': 6,
        'Manga': 40,
        'Graphic Novels': 2
    },
    'Charlie': {
        'Action Figures': 31,
        'Graphic Novels': 18
    },
    'Debbie': {
        'Funko Pop': 1,
        'Graphic Novels': 9,
        'Manga': 25,
        'Action Figures': 2
    }
}

print(collezionisti)

"""Abbiamo i seguenti dati riguardo dei collezionisti e le loro collezioni:
• Ada ha 10 Funko Pop, 5 action figures e 35 manga
• Ben ha 2 Funko Pop, 6 action figures, 40 manga e 2 graphic novels (entrambe
della DC)
• Charlie ha 31 action figures e 18 graphic novels (di cui 10 della Marvel e 8
della DC)
• Debbie ha 1 Funko Pop, 9 graphic novels (di cui 4 della DC e 5 della Marvel),
25 manga e 2 action figures
Creare dei dizionari innestati che contengano questi dati, e quindi visualizzarli"""
"""Riguardo l'esercizio precedente, stampiamo le risposte a:
1. quanti Funko Pop ha Ada?
2. quanti manga ha Ben?
3. quante graphic novels della Marvel ha Debbie?
4. quanti Funko Pop hanno Ada e Ben in tutto?
5. quanti manga hanno in tutto i collezionisti?
6. quante graphic novel della DC hanno in tutto i collezionisti?
7. quante graphic novel hanno in tutto i collezionisti?"
"""

collezionisti = {
    'Ada': 
           {
        'Funko Pop': 10,
        'Action Figures': 5,
        'Manga': 35
           },
    'Ben': {
        'Funko Pop': 2,
        'Action Figures': 6,
        'Manga': 40,
        'Graphic Novels': {
                            'DC': 2
                          }
            },
    'Charlie': 
            {
        'Action Figures': 31,
        'Graphic Novels': {
                            'DC': 8,
                            'MARVEL': 10
                          }
            },
    'Debbie': 
        {
        'Funko Pop': 1,
        'Graphic Novels': {
                            'DC': 4,
                            'MARVEL': 5
                          },
        'Manga': 25,
        'Action Figures': 2
        }
                   }



 #1. quanti Funko Pop ha Ada?
 
print(collezionisti['Ada']['Funko Pop'])

#2. quanti manga ha Ben?

print(collezionisti['Ada']['Manga'])

#3. quante graphic novels della Marvel ha Debbie?

print(collezionisti['Debbie']['Graphic Novels']['MARVEL'])

#4. quanti Funko Pop hanno Ada e Ben in tutto?

#The get() method returns the value for the specified key if the key is in the dictionary.
tot_funkopop = collezionisti['Ada'].get('Funko Pop') + collezionisti['Ben'].get('Funko Pop')
print(tot_funkopop)


#5. quanti manga hanno in tutto i collezionisti?

tot_manga = 0

for collezionista in collezionisti.values():
    tot_manga += collezionista.get('Manga', 0)
    
print(tot_manga)



#6.quante graphic novel della DC hanno in tutto i collezionisti?

tot_grnov_dc = 0

for collezionista in collezionisti.values():
    graphnovels = collezionista.get('Graphic Novels', {})  #Se non trova valore, restituisce dict vuoto
    tot_grnov_dc += graphnovels.get('DC', 0)               #Se non trova valore, restituisce 0
    
print("Totale Graphic Novels DC: " , tot_grnov_dc )

#7. quante graphic novel hanno in tutto i collezionisti?"


tot_graphic = 0

for collezionista in collezionisti.values():
    graphic_novels = collezionista.get('Graphic Novels', {})
    tot_graphic += sum(graphic_novels.values())

print("Totale Graphic Novels:", tot_graphic)
