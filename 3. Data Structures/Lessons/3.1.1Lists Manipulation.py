#creating a list
heros = ['Captain America', 'Spiderman', 'Wonder Woman']

#adding items to a list
heros.append('Black Widow') #adds one item to end of list
heros.extend(['Iron Man', 'Batman']) #add multiple items
heros.insert(3,'Hulk') #inserts value to specified index

#removing items from a list
heros.pop(1) #removing by index number (removes Spiderman) and returns element removed
heros.remove('Hulk') #remove element by value

#sorting a list
heros.sort() #in numeric, order
heros.sort(reverse=True) #in reverse order
heros.reverse() #in reverse order

#printing a list
print(heros)



#additional resources
#https://www.w3schools.com/python/python_lists.asp
#https://www.tutorialspoint.com/python/python_lists.htm
