# setting variable 'my_name' equal to 'monty'
my_name = "Monty"

#we can join variables in a string in multiple ways
print("Hello I am " + my_name + " the Python Guru")
print("Hello I am", my_name, "the Python Guru")
print(f"Hello i am {my_name} the Python Guru")



#we can use escape sequences to print non-literally
#   \n  creates a new line
print("hello world \nMy name is Monty")

#   \t  creates a tab
print("hello world \t My name is Monty")

#   \" or \' allows quotations inside a string
print("My dog barked \"WOOF\" at the mailman")

#   \u prints unicode   
print("Copyright Symbol: \u00a9")
print("Smoothies are only 99 \U+20B5) 


#   %s acts acts as a placeholder for a string
print("I have %s dollars" %"five")
#   %d acts acts as a placeholder for a number
print("I have %d dollars" %5)
#   %.2f will print a number to 2 decimal places
print("I have %.2f dollars" %5)




#additional resources
#More escape sequences:  https://linuxconfig.org/list-of-python-escape-sequence-characters-with-examples
#Unicode characeters:    https://www.rapidtables.com/code/text/unicode-characters.html
