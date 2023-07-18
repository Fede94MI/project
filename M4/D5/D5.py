#Abbiamo una lista di numeri, creare una nuova lista i cui elementi sono gli stessi della lista di partenza
#incrementati di 10 mediante comprehension.

numeri = [4, 10, 50, 100, 128, 71, 46]

numeri_nuovi = [x+10 for x in numeri]

print(numeri)
print(numeri_nuovi)

#Creare una nuova lista i cui elementi siano gli stetti di NUMERI,
#ma raddoppiati mediante comprehension

numeri = [4, 10, 50, 100, 128, 71, 46]

numeri_nuovi= [numero*2 for numero in numeri]

print(numeri)
print(numeri_nuovi)

#Abbiamo una lista di nomi, creare una nuova lista i cui elementi siano le iniziali
#dei nomi, mediante comprehension

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]

studenti_iniziale = [iniziale[0] for iniziale in studenti]

print(studenti_iniziale)

#Abbiamo una lista di nomi, creare una nuova lista i cui elementi siano le iniziali dei nomi seguite da un punto
# mediante comprehension

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]

studenti_iniziale = [iniziale[0] + '.' for iniziale in studenti]

print(studenti_iniziale)

#Abbiamo una lista di CF, creare una lista che contenga solo i caratteri relativi al nome

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

cf_nome = [nome[:3] for nome in lista_cf]

print(cf_nome)

#Abbiamo una lista di CF, creare una lista che contenga solo i caratteri relativi al nome e un'altra lista solo i cognomi

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

cf_nome = [nome[:3] for nome in lista_cf]

cf_cognome = [cognome[3:6] for cognome in lista_cf]

print(cf_nome)
print(cf_cognome)

#Abbiamo una lista di CF, creare una lista che contenga solo i cf nati nel 95.

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

cf_filter = [cf for cf in lista_cf if '95' in cf]

print(cf_filter)


#Abbiamo una lista di CF, creare una lista che contenga solo i cf nati nel 95 e che contenga gli ultimi 5 caratteri.

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

cf_filter = [cf[-5:] for cf in lista_cf if '95' in cf]

print(cf_filter)

#Cambiare simbolo € in $

prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"]

prezzi = [prezzo.replace('€','$') for prezzo in prezzi]

print(prezzi)

#Abbiamo una lista di studenti, voglia dividere una meta' in una lista e l'altra metà in un'altra.

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"]
squadrauno = [studenti[i] for i in range(len(studenti)//2)]
squadradue = [studenti[i] for i in range(len(studenti)//2, len(studenti))]

print(squadrauno)

print(squadradue)

#Squadre indice pari e indice dispari

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"]

squadrapari = [studenti[index] for index in range(len(studenti)) if index % 2 == 0]
squadradispari = [studenti[i] for i in range(len(studenti)) if i % 2 != 0]

print(squadrapari)
print(squadradispari)

#Confrontare

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

output = [('Mese ' + str(i+1) + ': ' + str(guadagni[i]) + '€') if i == 0 else ('Mese ' + str(i+1) + ': ' + str(guadagni[i]) + '€ (media precedente: ' + str(guadagni[i-1]) + '€)') for i in range(len(guadagni))]

for item in output:
    print(item)

#Confronto due
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

output = [('Mese ' + str(i+1) + ': ' + str(guadagni[i]) + '€ (maggiore della media precedente)') if i == 0 else ('Mese ' + str(i+1) + ': ' + str(guadagni[i]) + '€ (maggiore della media precedente)' if guadagni[i] > guadagni[i-1] else 'Mese ' + str(i+1) + ': ' + str(guadagni[i]) + '€ (minore della media precedente)') for i in range(len(guadagni))]

for item in output:
    print(item)
    
#Creare funzione MAX senza usare il metodo Max():

def Maggiore (x):
    if not x:
        return None
    
    maggiore = x[0]
    for elem in x:
        if elem > maggiore:
            maggiore = elem
            
    return maggiore
    
    
lista = [1, 2, 3, 4]
print(Maggiore(lista))

#Creare funzione che restituisce il Minimo e il Massimo

def MinMax(x):
    if not x:
        return None

    maggiore = x[0]
    minore = x[0]

    for elem in x:
        if elem > maggiore:
            maggiore = elem
        elif elem < minore:
            minore = elem

    return [maggiore, minore]


lista_numeri = [12, 45, 8, 23, 67, 9, 13]
risultato = MinMax(lista_numeri)
print("Il maggiore e il minore della lista sono:", risultato) 

#Creare funzione che restituisce i due numeri più grandi di una lista


def due_numeri_piu_grandi(lista):
    if len(lista) < 2:
        raise ValueError("La lista deve contenere almeno due elementi")

    primo_massimo = 0
    secondo_massimo = 0

    for numero in lista:
        if numero > primo_massimo:
            secondo_massimo = primo_massimo
            primo_massimo = numero
        elif numero > secondo_massimo:
            secondo_massimo = numero

    return primo_massimo, secondo_massimo

lista_numeri = [10, 5, 20, 30, 15]
risultato = due_numeri_piu_grandi(lista_numeri)
print("I due numeri più grandi sono:", risultato)

#Scrivere una funzione che in input acquisisce una lista di numeri e un numero K;
#in output dovrà restituire la media di tutti i numeri nella lista maggiori o uguali a K; se non ce ne dovesse essere nessuno
#dovrà stamapre a schermo un messaggio adeguato

def media_soglia (lista, soglia):
    numeri_validi = [elemento for elemento in lista if elemento >= soglia]
    if not numeri_validi:
        print(f"Non c'è nessun numero maggiore o uguale a {soglia}")
        
    media = sum(numeri_validi) / len(numeri_validi)
    
    return media
#----------------------------------------------------------


input_numeri = input("Inserisci una lista di numeri interi positivi separati da uno spazio: ")
lista_numeri = []
try:
    for elemento in input_numeri.split():
            numero = int(elemento)
            if numero >= 0:
                lista_numeri.append(numero)
            else:
                print("Attenzione: Hai inserito un numero negativo, verrà ignorato.")
except ValueError:
                print("Attenzione: Inserisci solo numeri interi separati da uno spazio.")
                
value = False

while value == False:
    try:
        k = int(input("Inserisci un numero intero non negativo: "))
        if k >= 0:
            value = True
        else:
            print("Errore: Devi inserire un numero intero non negativo.")
    except ValueError:
        print("Errore: L'input non è un numero intero valido. Riprova.")
        

avg = media_soglia(lista_numeri, k)

print("La lista numeri inserita è: ", lista_numeri)
print("Il valore soglia inserito è: ", k)

print(f"La media dei valori superiore al numero {k} è di {avg}")


#Creare una funzione che, data una lista di numeri, come output stamperà lo stesso numero di asterischi su righe
#diverse , ottenendo una semplice viz grafica

def aster(lista):
    for elemento in lista:
        print('*'*elemento)    
    

lista = [3, 5, 7, 8]

aster(lista)
    
#conteggio caratteri testo
def count_char(tex):

    conteggio_caratteri = {}

    for carattere in testo:
        if carattere != ' ':
            conteggio_caratteri[carattere] = conteggio_caratteri.get(carattere, 0) + 1
            
    return conteggio_caratteri



testo = """Lisetta va a passeggio in campagna; è felice di raccogliere i fiori che crescono sulle rive, 
ai bordi della strada. Ha già un bel mazzetto di ranuncoli e margherite."""


print(count_char(testo))        
        


#count senza caratteri speciali:

def count_char(tex):

    conteggio_caratteri = {}

    for carattere in testo:
        if carattere not in ( ' ', '\n' , ';',  ',' , '.'):
            conteggio_caratteri[carattere] = conteggio_caratteri.get(carattere, 0) + 1
            
    return conteggio_caratteri



testo = """Lisetta va a passeggio in campagna; è felice di raccogliere i fiori che crescono sulle rive, 
ai bordi della strada. Ha già un bel mazzetto di ranuncoli e margherite."""


print(count_char(testo))

#count senza distinzione maiusc e minusc

def count_char(tex):

    conteggio_caratteri = {}

    for carattere in tex.lower():
        if carattere not in ( ' ', '\n' , ';',  ',' , '.'):
            conteggio_caratteri[carattere] = conteggio_caratteri.get(carattere, 0) + 1
            
    return conteggio_caratteri



testo = """Lisetta va a passeggio in campagna; è felice di raccogliere i fiori che crescono sulle rive, 
ai bordi della strada. Ha già un bel mazzetto di ranuncoli e margherite."""


print(count_char(testo))


import json

filepath = 'pub.json'
file = open(filepath,'r', encoding='latin1')
pub =json.load(file)

file.close()

#print(len(pub)) Quanti elementi contiene

#metadato = pub[0]
#print(metadato.keys())  METADATI


#elemento = pub[0] print(elemento)  primo elemento
#elemento = pub[-1] print(elementi) ultimo elemento



"""lista_provincia = []

for prov in pub:
    if prov['cprovincia'] == 'VICENZA':
        lista_provincia.append(prov['cnome'])

print(len(lista_provincia))"""  #Quanti locali in provincia di Vicenza



"""lista_anni = []

for anni in pub:
    lista_anni.append(int(anni['canno_inserimento']))
    
print(sorted(set(lista_anni)))"""  #Anni inserimento

"""attiv_tot = []

for locali in pub:
    if locali['cregione'] == 'Lazio' or locali['cregione'] == 'Abruzzo':
        attiv_tot.append(locali['cregione'])
        
print(len(attiv_tot))"""  #totale locali abruzzo e lazio


"""locali_latlong = []

for locali in pub:
    if 9 >= float(locali['clongitudine']) <= 10 and 45 >= float(locali['clatitudine']) <= 46:
        locali_latlong.append(locali['cnome'])

print(len(locali_latlong))""" #locali presenti dentro un quadrante