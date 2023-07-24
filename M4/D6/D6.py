"""Abbiamo una lista di liste

mat = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]]
#un'array monodimensionale

print(mat[1][4])"""

#Esercizio2
"""
import numpy as np

array = np.array([[0,1,2,3,4],
                  [5,6,7,8,9],
                  [10,11,12,13,14]])

print(array[1,4])
"""

"""Esercizio3

import numpy as np

linear_array = np.array([x for x in range(27)]) #genera un array monodimensionale

resh_array = linear_array.reshape((3,3,3))

print(linear_array)
print(resh_array)

#array 3dimensioni

print(resh_array.ndim)
print(resh_array[1,1,2])
"""

"""Esercizio4

import numpy as np

num_clienti_per_store = np.zeros(4, dtype=int)

lista_store=['UL','UR','LL','LR']

for i in range(len(num_clienti_per_store)):
    while True:
        try:
            clienti_serviti = int(input(f"Inserisci il numero di clienti serviti nello store {lista_store[i]}: "))
            break
        except ValueError:
            print("Inserisci un valore numerico valido.")

    num_clienti_per_store[i] = clienti_serviti

print("Conteggio clienti per store:", num_clienti_per_store)
"""

import numpy as np

# Inizializza la lista degli store con zeri
stores = [0, 0, 0, 0]

for _ in range(100):
    # Genera un numero casuale per determinare lo store (quadrante)
    store_index = np.random.randint(0, 4)

    # Incrementa il conteggio dei clienti per lo store scelto
    stores[store_index] += 1

# Stampa il numero di clienti serviti da ciascuno store
print("Numero di clienti serviti per ogni store:")
print("Store UR:", stores[0])
print("Store LR:", stores[1])
print("Store UL:", stores[2])
print("Store LL:", stores[3])

# Determina gli store con più di 25 clienti
stores_with_more_than_25_clients = [i for i, num_clients in enumerate(stores) if num_clients > 25]

# Stampa gli store con più di 25 clienti e il loro numero
print("Store con più di 25 clienti:", stores_with_more_than_25_clients)
print("Numero di store con più di 25 clienti:", len(stores_with_more_than_25_clients))

# Calcola e stampa la somma totale dei clienti serviti
total_clients = sum(stores)
print("Totale clienti serviti:", total_clients)


import numpy as np

# Inizializza la lista degli store con zeri
stores = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Ripetizione della simulazione per 200 iterazioni
for _ in range(200):
    # Genera un numero casuale per determinare lo store
    store_index = np.random.randint(0, 9)

    # Incrementa il conteggio dei clienti per lo store scelto
    stores[store_index] += 1

# Stampare il numero di clienti serviti da ciascuno store
print("Numero di clienti serviti per ogni store:")
for i, num_clients in enumerate(stores):
    print(f"Store {i+1}: {num_clients * 4}")  # Moltiplicare per 4 i valori per l'anno prossimo



import numpy as np

lunghezza_struttura = 28.75  # Lunghezza della struttura in cm
num_rivetti_intermedi = 13  # Numero di rivetti intermedi

# Calcola la distanza tra i rivetti intermedi
distanza_rivetti = lunghezza_struttura / (num_rivetti_intermedi + 1)

# Calcola i punti esatti in cui inserire i rivetti
punti_rivetti = np.arange(distanza_rivetti, lunghezza_struttura, distanza_rivetti)

# Aggiunge il primo e l'ultimo rivetto agli estremi della struttura
punti_rivetti = np.insert(punti_rivetti, 0, 0)
punti_rivetti = np.append(punti_rivetti, lunghezza_struttura)

# Stampa i punti esatti in cui inserire i rivetti
print("Punti esatti in cui inserire i rivetti:")
print(punti_rivetti)




import numpy as np

array = np.array([[1,1,1,1],[5,1,1,1],[20,-4,0,42]])

print(array.ndim)
####

import numpy as np

array = [10, 22, 21, 8, 9, 9, 42, 3, 18, 11, 5, 4, 30, 12, 29, 37, 31, 7, 26, 8, 6, 4, 33, 15]


min_value = np.min(array)


max_value = np.max(array)


result = (np.array(array).reshape(5, 5) - min_value) / (max_value - min_value)

print(result)
