#and is a logical operator where both conditions must be True

age = int(input('Enter age: '))
health = int(input('Enter health score: '))


if health > 7:
    print("You are healthy")
elif age <= 17 and health <= 7:
    print("Go to Pediatrician Pete")
elif age > 17 and health <=7:
    print("Go to Physician Pat")
else:
    print("Please wait for the receptionist")
            

#or is a logical operator where only one of the conditions must be True

if age > 60 or health > 8:
    print("Your insurance covered this visit at 100%")
else:
    print("Your bill is $75")




#Additional Resources
#https://www.tutorialspoint.com/python/python_basic_operators.htm
