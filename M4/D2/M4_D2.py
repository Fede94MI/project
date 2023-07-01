"""primo esercizio

stringa="Epicode"

print(stringa)"""

"""SECONDO ESERCIZO

nome_scuola="Epicode"

print(nome_scuola[0])"""

"""TERZO ESERCIZIO

print(nome_scuola[:3])"""

"""QUARTO ESERCIZIO
print(nome_scuola.upper())"""

"""QUINTO ESERCIZIO
x=10

x+=2
x*=3

print(x)

#metodo basic
x=10
x=x+2
x=x*3
print(x)"""

"""SESTOESERCIZIO

serbatoio = float(input("Inserisci quanti litri contiene il tuo serbatoio: "))
prezzo_benzina = float(input("Inserisci il costo al litro in euro della benzina ad oggi: "))
consumo = float(input("Inserisci il consumo di KM al litro: "))

litri100km = 100 / consumo


print("Per 100 km, consumerai: %.2f litri di benzina" % litri100km)

costobenzina=litri100km*prezzo_benzina
print("Per 100 km, spenderai: %.2f € " % costobenzina)"""

"""SETTIMO ESERCIZIO

stringa1=str(input("Inserisci una stringa: "))

stringaprimi=stringa1[0:3]
stringaultimi=stringa1[-3:]

print(stringaprimi+"..."+stringaultimi)"""

"""OTTAVO ESERCIZIO

checkword1="Excel"

checkword2="Windows"

checkword3="Excel"

checkword4="Powerpoint"

checkword5="Word"


print("Il numero di caratteri che compone la parola " + checkword1 +" è di: " , len(checkword1))
print("Il numero di caratteri che compone la parola " + checkword2 +" è di: " , len(checkword2))
print("Il numero di caratteri che compone la parola " + checkword3 +" è di: " , len(checkword3))
print("Il numero di caratteri che compone la parola " + checkword4 +" è di: " , len(checkword4))
print("Il numero di caratteri che compone la parola " + checkword5 +" è di: " , len(checkword5))
"""



"""ESERCIZIO 9

codici=["knt-S1","cba-G9","qtr-Z8"]

estraz1=codici[0][-3:]
estraz2=codici[1][-3:]
estraz3=codici[2][-3:]

print(estraz1)
print(estraz2)
print(estraz3)"""

"""esercizio 10

codici=["knt-S1","cba-G9","qtr-Z8"]
estraz1=codici[0][-3:]
estraz2=codici[1][-3:]
estraz3=codici[2][-3:]

lista=[estraz1,estraz2,estraz3]
print(lista)"""

#ULTIMO ESERCIZIO

growth = {"Tesla", "Shopify", "Block", "Etsy", "MercadoLibre", "Netflix", "Amazon", "Meta Platforms", "Salesforce", "Alphabet"}

value = {"Pfizer", "Johnson & Johnson", "JPMorgan Chase & Co.", "Wells Fargo & Co.", "Verizon Communications", "BP PLC", "LyondellBasell Industries", "MetLife", "Interactive Brokers Group", "Intel"}

tech = {"Apple", "Microsoft", "Alphabet", "Amazon", "NVIDIA", "Meta Platforms", "Tesla", "Alibaba", "Salesforce", "Advanced Micro Devices", "Intel", "PayPal", "Activision Blizzard", "Electronic Arts", "The Trade Desk", "Zillow Group", "Match Group", "Yelp"}

healthcare = {"UnitedHealth Group", "Johnson & Johnson", "Eli Lilly & Co.", "Novo Nordisk", "Merck & Co.", "Roche Holding", "Pfizer", "Thermo Fisher Scientific", "Abbott Laboratories"}



"""investment= set()
investment.update(growth)
investment.update(value)

print("Per diversificare i tuoi investimenti, ecco le aziende growth e value : " )
print(investment)

growthtech=set()
growthtech.update(tech)

print("Aziende tech growth: ")
print(growthtech.intersection(growth))

valuetech=set()
valuetech.update(tech)
print("Aziende Value tech: ")
print(valuetech.intersection(value))

#QUALII TITOLO HEALTHCARE NON SONO VALUE

novaluehealth=set()
novaluehealth.update(healthcare)

print("Healthcare non Value: ")
print(healthcare.difference(value))


mixset=set()

mixset.update(tech)

print(tech.intersection(healthcare))

"""

