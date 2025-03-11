# Pandas

import matplotlib.pyplot as mt
import pandas as pd
empdata=pd.read_csv("E:\Excel\SalarySheet.csv")
#print(empdata)
x=pd.Series(empdata["Name"])
y=pd.Series(empdata["NetSalary"])
mt.title("SalarySheet")
mt.xlabel("Name")
mt.ylabel("Salary")
mt.plot(x,y,color="Red")
mt.grid(color="Green")
mt.show()
