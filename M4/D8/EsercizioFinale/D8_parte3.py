import seaborn as sns
import matplotlib.pyplot as plt
from plotly import express as px

titanic = sns.load_dataset('titanic')

sns.countplot(data=titanic, x='deck')

plt.show()

n_ponti = titanic['deck'].nunique()
print("Sul Titanic erano presenti:", n_ponti, "ponti.")

##

import seaborn as sns
import matplotlib.pyplot as plt
from plotly import express as px

titanic = sns.load_dataset('titanic')

NaNdata = titanic.isnull().sum()

print(NaNdata)

#Tramite fillna o dropna


###

import seaborn as sns
import matplotlib.pyplot as plt
from plotly import express as px

titanic = sns.load_dataset('titanic')

joingraph = sns.jointplot(data=titanic, x=titanic['fare'], y=titanic['age'], kind='kde')
joingraph.set_axis_labels('costo biglietto','età')

plt.show()
###Vediamo la distribuzione dell'età in funzione della tariffa.
#####

import seaborn as sns
import matplotlib.pyplot as plt
from plotly import express as px

titanic = sns.load_dataset('titanic')



counforclass = titanic['pclass'].value_counts()

sns.countplot(data = titanic, x='pclass')
plt.xlabel('Classe')
plt.ylabel('Num_Pass')
plt.show()

####

import seaborn as sns
import matplotlib.pyplot as plt
from plotly import express as px

titanic = sns.load_dataset('titanic')




sns.countplot(data = titanic, x='alive')
plt.xlabel('Sopravissuto')
plt.ylabel('Num_Pass')

###

import seaborn as sns
import matplotlib.pyplot as plt
from plotly import express as px

titanic = sns.load_dataset('titanic')


sns.boxplot(data= titanic, x='pclass', y='age')
plt.title('Distribuzione età in relazione classe di imbarco(Boxplot)')

plt.show()

####

import seaborn as sns
import matplotlib.pyplot as plt
from plotly import express as px

titanic = sns.load_dataset('titanic')


sns.swarmplot(data= titanic, x='pclass', y='age')
plt.title('Distribuzione età in relazione classe di imbarco(Boxplot)')

plt.show()

######

import seaborn as sns
import matplotlib.pyplot as plt
from plotly import express as px

titanic = sns.load_dataset('titanic')




sns.boxplot(data = titanic, x='deck', y='fare')
plt.show()

#####

import seaborn as sns
import matplotlib.pyplot as plt
from plotly import express as px

titanic = sns.load_dataset('titanic')

sns.kdeplot(titanic.age)
plt.xlabel('Età')
plt.ylabel('Densità distribuzione età')

plt.show()


###

import seaborn as sns
import matplotlib.pyplot as plt
from plotly import express as px

titanic = sns.load_dataset('titanic')

sns.boxplot(data= titanic, x='survived', y='fare')
plt.show()

#I sopravvissuti avevano una tariffa più alta rispetto a quelli che hanno pagato la tariffa più bassa.

###

import seaborn as sns
import matplotlib.pyplot as plt
from plotly import express as px

titanic = sns.load_dataset('titanic')

sns.lmplot(data= titanic, x='survived', y='fare')
plt.show()

#I sopravvissuti avevano una tariffa più alta rispetto a quelli che hanno pagato la tariffa più bassa.

###
import seaborn as sns
import matplotlib.pyplot as plt
from plotly import express as px

titanic = sns.load_dataset('titanic')

grafico1 = px.scatter(data_frame=titanic,
                      x='age', y='deck',
                      color="survived",
                      size='fare',
                      symbol='sex',
                      category_orders={'deck':list("ABCDEFG") })

grafico1.show()


