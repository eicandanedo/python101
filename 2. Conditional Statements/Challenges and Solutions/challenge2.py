#this program will inform users if they can or cannot enter the casino

#ask user for their age
age = int(input("How old are you? "))

#tell user if they are allowed in the casino or not
if age >= 21:
    print("Welcome to Cassie's Casino")
else:
    print("Sorry you cannot enter")

#quit program
input("press any key to quit")
