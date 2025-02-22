# Student Data

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
