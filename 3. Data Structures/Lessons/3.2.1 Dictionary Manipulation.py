#making changes to our yoga dictionary
yoga = {'Instructor' : 'Jane',
        'Location': 'Plum Center',
        'Price': 199,
        'Students' : ['Alex', 'Carl', 'Connie']
        }

#updating a value
yoga["Instructor"] = "Derek"


#adding an item
yoga['room'] = '200B'


#removing an item
del yoga['Price']

#printing dictionary
print(yoga)

#additional resources
#https://www.tutorialspoint.com/python/python_dictionary.htm
#https://www.programiz.com/python-programming/dictionary
