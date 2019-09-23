#the purpose of this program is to convert a dogs age to human years
#if the user enters a non-numeric value, the error will be handled with a Try Except

#ask user to enter dogs age and convert age to an integer
try:
    dog_age = int(input("Enter your dogs age: "))
    human_age = dog_age * 7
    print(f"Your dog is {human_age} years old")

    
#if the conversion to float fails, print out error message
except:
    print("Sorry age must be a number.")

#the finally clause is optional. This will run regardless of whether an error occured or not
finally:
    input("press any key to exit")




#try typing a string "five" or "no" instead of a number to ensure the error is handled




#additional Resources
#https://www.programiz.com/python-programming/exception-handling
#https://www.youtube.com/watch?v=nlCKrKGHSSk
