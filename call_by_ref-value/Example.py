# call by reference

def hello():
    print("Hello there!")

hello()
hello()
hello()

# call by value

def add(x,y):
    z=(x+y)
    print("Sum of both numbers= ",z)
add(200,300)
