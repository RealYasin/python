# Calculate Net Salary

name=input("Enter Your Name= ")
s=int(input("Enter Your Salary= "))
tds=int(input("Enter Your T.D.S(in integer)= "))
pf=int(input("Enter Your P.F(in integer)= "))
net=s-tds-pf
print("")
print("Hello",name,"Your total salary is ",s)
print("With your T.D.S,P.F being",tds,"and",pf)
print("Now deducting your T.D.S and P.F then your Net Salary will be ",net)
