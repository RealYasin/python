# Matplot 2D

import numpy as np
import matplotlib.pyplot as mt
data={"Name":["Yasin","xyz1","xyz2"],"Marks":[90,80,70]}
x=data["Name"]
y=data["Marks"]
col=["Red","Black","Green"]
mt.title("Students Marks")
mt.xlabel("Name")
mt.ylabel("Marks")
mt.bar(x,y,color=col)
mt.plot(x,y,color="Blue")
mt.show()
mt.close()
