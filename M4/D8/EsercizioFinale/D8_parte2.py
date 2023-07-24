import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotly import express as px

election = px.data.election()
total_vote=[election.Coderre.sum(),election.Bergeron.sum(),election.Joly.sum()]
major = ['Bergeron','Coderre','Jolly']
plt.bar(major,total_vote)
plt.show()

##########

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotly import express as px

election = px.data.election()

four_district = election[:4]

sum_total_vote =[four_district.Coderre.sum(),four_district.Bergeron.sum(),four_district.Joly.sum()]
major = ['Bergeron','Coderre','Jolly']
plt.bar(major,sum_total_vote)
plt.show()


####

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotly import express as px

election = px.data.election()

four_district = election[:4]

district = four_district['district']

coderre_votes = four_district['Coderre']
bergeron_votes = four_district['Bergeron']
joly_votes = four_district['Joly']

plt.bar(district, coderre_votes, label='Coderre')
plt.bar(district, bergeron_votes, bottom = coderre_votes, label='Bergeron')
plt.bar(district, joly_votes, bottom=coderre_votes + bergeron_votes, label='Joly' )
plt.legend()
plt.xticks(rotation=45)
plt.savefig('StackBar.png', dpi=300)

plt.show()