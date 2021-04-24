#creating a groceries dictionary where item name is key and price is value

groceries = { 'chocolate': 2,
              'pizza' : 10,
              'flowers' : 10,
              'chips': 1
    }

print(groceries)


#adanced printing method. will go over for loops in future lesson
for x,y in groceries.items():
    print(x,y)


input('Press any key to quit')
