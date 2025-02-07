# Sum of 2 numbers with using if and else

f = float(input("Enter first number: "))
o = input("Enter operator: ")
s = float(input("Enter second number: "))

if o == "+":
    print(f + s)
elif o == "-":
    print(f - s)
elif o == "/":
    print(f / s)
elif o == "*":
    print(f * s)
else:
    print("wrong operator please choose from add,sub,div,mul")
    print("oh if you're confused how multipication and division opertors looks here it is * and / ")
    print("Hope it helps :)")
