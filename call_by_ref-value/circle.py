# Find the Area and Circumference of Circle using call by value

r=int(input("Enter the radius= "))
def circle(r):
    a=3.14*r*r
    c=2*3.14*r
    print("Area and Circumfrence of circle= ",a,"&",c)

circle(r)
