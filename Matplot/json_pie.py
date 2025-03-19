# Data visualization from JSON File(Pie chart)

import pandas as pd
import matplotlib.pyplot as mt
data=pd.read_json("name.json")
name=pd.DataFrame(data)
#print(name)
x=pd.Series(data["name"])
y=pd.Series(data["Salary"])
mt.title("Basic Info")
mt.ylabel("Salary")
mt.pie(y,labels=y)
mt.legend(labels=x)
mt.show()
