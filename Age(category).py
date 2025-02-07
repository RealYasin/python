# To categorize age

age=int(input("Please enter your age= "))
if age<=15:
    print("You're a Child :)")
elif age<=19:
    print("You're a Teenager.")
elif age<=40:
    print("You're a Youngster.")
elif age<=80:
    print("You're an adult.")
else:
    print("Since the average age of a human is 80, we don't have more data above it :(")
