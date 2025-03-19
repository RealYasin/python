# Data visualization from JSON File

import pandas as pd
import matplotlib.pyplot as mt
data=pd.read_json("name.json")
name=pd.DataFrame(data)
#print(name)
x=pd.Series(data["name"])
y=pd.Series(data["Salary"])
mt.title("Basic Info")
mt.xlabel("Name")
mt.ylabel("Salary")
mt.grid(color="Black")
mt.plot(x,y,color="Red")
mt.show()
