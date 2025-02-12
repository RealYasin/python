# Print Even Odd number with for loop

num=int(input("Enter the number= "))
for x in range (1,num):
    if x%2==0:
        print(x,"Even")
    elif x==1:
        print(x,"Neither Even nor odd")
    else:
        print(x,"Odd")
