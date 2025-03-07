# Matplot 1D

import numpy as np
import matplotlib.pyplot as mt
name=np.array(["Yasin","xyz1","xyz2"])
marks=np.array([98,89,70])
mt.title("Students Marks")
mt.xlabel("Name")
mt.ylabel("Marks")
mt.plot(name,marks,"o",color="red")
mt.show()
mt.close()
