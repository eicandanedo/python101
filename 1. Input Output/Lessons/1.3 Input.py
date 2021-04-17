#using input function will take information from users and stores it to a variable as a string
name = input("What is your name? ")
hobby = input("What is your favorite hobby? ")

#inserting variables into a print statement. See lesson 1.2 for F-String review
print(f"Hi {name}, my name is Monty and i like {hobby} too!")


#since inputs are always stored as strings, remember to convert data types whenever necessary. See Lesson 1.0 for review
birth_year = input("What year were you born? ")
age = 2021 - int(birth_year)
print(f"Are you {age} years old")  
