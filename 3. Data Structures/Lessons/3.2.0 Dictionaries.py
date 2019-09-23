#creating a dictionary to store information about our yoga classes

yoga = {'Instructor' : 'Jane',
        'Location': 'Plum Center',
        'Price': 199,
        'Students' : ['Alex', 'Carl', 'Connie']
        }

#print dictionary
print(yoga)        

#Iterating over dictionaries like iterating over lists will output only key
for key in yoga:
    print(key)

#iterating over dictionary using for loop
for key, value in yoga.items():
    print(key,value)


#using in and not in to know if a key is defined
if 'Location' in yoga:
    print('Location Known')
else:
    print('Location Unknown')


#You can access values in dictionary in two ways 
print(yoga['Price'])   #will return key error if key does not exist
print(yoga.get('Price'))  #will return none if key does not exist

#Nesting dictionaries (dictionaries inside of dictionaries)
my_family = {
  "child1" : {
    "name" : "Emily",
    "year" : 2004
  },
  "child2" : {
    "name" : "Sam",
    "year" : 2007
  },
  "child3" : {
    "name" : "Pat",
    "year" : 2011
  }
}
#accessing values in nested dictionaries
print(my_family["child1"]['name'])


#additional resources
#https://www.tutorialspoint.com/python/python_dictionary.htm
#https://www.programiz.com/python-programming/dictionary
