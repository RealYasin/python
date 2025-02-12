# Print Pyramid 4th pattern(55555 4444 333 22 1)

num=int(input("Enter the rows= "))
for i in range(num,0,-1):
    for j in range(i): 
        print(i,end="") 
    print("") 
