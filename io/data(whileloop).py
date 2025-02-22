# Student Data using while loop

num=int(input("How many students data you wanna enter= "))
i=1
while i<=num:
    Name=input("Enter your name= ")
    Age=int(input("Enter your age= "))
    if Age<=18:
        print("Invalid Age")
    else:
        Age1=str(Age)
        data=open("Students.txt","a")
        data.write(Name)
        data.write(",")
        data.write(Age1)
        data.write("\n")
        data.close()
    i=i+1
