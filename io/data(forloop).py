# Student Data using forloop

num=int(input("How many student data you wanna enter= "))
for x in range(1,num):
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
