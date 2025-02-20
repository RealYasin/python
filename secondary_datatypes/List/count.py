# Print the count of a number given by the user

x=[100,30,50,34,89,67,89,56,90,54,10,20,45]
num=int(input("Enter the number = "))
count=0
i=0
while i<=12:
    if x[i]==num:
        count=count+1
    i=i+1
print("Your Number count = ",count)
