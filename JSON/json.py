# Reading JSON data in python

import pandas as pd
import pymongo as pm
data=pd.read_json("data.json")
fd=pd.DataFrame(data)
name=pd.Series(fd["Name"])
salary=pd.Series(fd["Salary"])
print(fd)
print(name)
print(salary)
