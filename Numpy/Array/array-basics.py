# Array basics

import numpy as np
x=np.array(100)
y=np.array([100,200,300,400,500])
z=np.array([[10,20,30],[40,50,60]])
m=np.array([[[10,20,30],[40,50,60]],[[70,80,90],[100,110,120]]])

print(x)
print(y)
print(z)
print(m)

print(x.ndim," ",y.ndim," ",z.ndim," ",m.ndim)     # States the dimension of an array
print(x.shape," ",y.shape," ",z.shape," ",m.shape) # States the shape of an array
print(x.size," ",y.size," ",z.size," ",m.size)     # States the size of an array

print(y[0])
print(z[0,0])
print(z[0,1])
print(m[0,0,0])
print(m[0,0,1])
