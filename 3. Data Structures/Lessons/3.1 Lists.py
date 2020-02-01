#a list is a sequence shown in comma separated values inside square brackets
#it can hold multiple items (sometimes caled elements)


#a list of strings
cars = ['Ford', 'BMW', 'Audi', 'Honda']

#a list of numbers
years = [1994, 1999, 2004]

#a list can contain a mix of data types and data structures
mix = ['Hello', 12, cars]

#a list can contain duplicate items
dupes = ['cat', 'cat', 'cat']

#a list can be empty
empty_list = []

#lists are indexed. this means you start counting from 0
#in the list cars, Ford if index 0, BMW, is index 1

#print first element (index 0) in list
print(cars[0])

#print last index in list
print(cars[-1])

#print a range from the list. Note the last number is excluded
print(cars[1:3])

#List membership in and not in. Outputs Boolean values
print('Ford' in cars)
print('Ford' not in cars)


#print number of items in list
print(len(cars))

