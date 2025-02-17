# Calculate Net Salary using call by value

name=input("Enter Your Name= ")
s=int(input("Enter Your Salary= "))
def salary(s):
    tds=(s/100)*10
    pf=(s/100)*12
    net=s-(tds+pf)
    print("")
    print("Hello",name,"Your total salary is ",s)
    print("With your T.D.S,P.F being",tds,"and",pf)
    print("Now deducting your T.D.S and P.F then your Net Salary will be ",net)
salary(s)
