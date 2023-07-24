import pandas as pd
import matplotlib.pyplot as plt
from plotly import express as px


stocks = px.data.stocks()

goog_head = stocks.head(6)['GOOG']
date_head = stocks.head(6)['date']

goog_tail = stocks.tail(6)['GOOG']
date_tail = stocks.tail(6)['date']

print(goog_head)
print(date_head)

print(goog_tail)
print(date_tail)

plt.plot(date_head, goog_head, 'g')
plt.title('Andamento azioni Google prime 5 righe', color="blue")
plt.xlabel('Data')
plt.ylabel('Valori')
plt.grid(False)
plt.show()

plt.plot(date_tail, goog_tail, 'g')
plt.title('Andamento azioni Google ultime 5 righe', color="blue")
plt.xlabel('Data')
plt.ylabel('Valori')
plt.grid(False)
plt.show()



#AAPPL

import pandas as pd
import matplotlib.pyplot as plt
from plotly import express as px


stocks = px.data.stocks()

twenty_aapl = stocks.head(20)['AAPL']
data = stocks.head(20)['date']

plt.plot(data,twenty_aapl, color='r', linestyle= '--', marker='o', markerfacecolor='black', linewidth=2)
plt.title('Azioni Apple')
plt.xlabel('Data')
plt.ylabel('Azioni')
plt.xticks(rotation=90)
plt.grid(False)
plt.show()

#tutte le azioni

import pandas as pd
import matplotlib.pyplot as plt
from plotly import express as px

stocks = px.data.stocks()
dataframe_stocks = pd.DataFrame(stocks)

date = dataframe_stocks['date']
goog = dataframe_stocks['GOOG']
aapl = dataframe_stocks['AAPL']
amzn = dataframe_stocks['AMZN']
fb = dataframe_stocks['FB']
nflx = dataframe_stocks['NFLX']
msft = dataframe_stocks['MSFT']

plt.plot(date, goog, label='GOOG')
plt.plot(date, aapl, label='AAPL')
plt.plot(date, amzn, label='AMZN')
plt.plot(date, fb, label='FB')
plt.plot(date, nflx, label='NFLX')
plt.plot(date, msft, label='MSFT')

plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

plt.legend(loc='lower right')
plt.xticks(rotation=45) 
plt.tight_layout()      
plt.show()