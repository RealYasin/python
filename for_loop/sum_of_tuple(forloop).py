# Print the sum of the given tuple(x,y) using for loop

x=100,200,300,400,500
y=10,20,30,40,50

for i in range(len(x)):
    print(x[i]+y[i],end=" ")

             #OR

print("")
for a, b in zip(x, y):
    print(a + b, end=" ")
