#you can convert data types using built-in Python functions

#use str to convert a value to a string
age = 10
age = str(age)

#use int to convert a value to a integer
age = int(age)

#use float to convert a value to a float
age = float(age)


#creating 2 lists
names = ["Chris", "Zoe", "Zoe", "Leo"]
job = ["Teacher", "Nurse", "Lawyer", "Actor"]


#use set to convert to a set
names = set(names)

#use dict and zip to convert a dictionary. Zip takes 2 arguments for key value pairs
names = dict(zip(names, job))

#use tuple to convert to a tuple
names = tuple(names)
print(names)

#use type to find the type an object is
print(type(names))
