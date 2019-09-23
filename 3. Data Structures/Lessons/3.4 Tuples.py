#a tuple is a sequence of immutable Objects

months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',  
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


#you can access values in months using indexing
print(months[0])


#since a tuple is immutable, you cannot add, delete, or change values in the tuple



try:
    months.append("Trecember")  #trying to add 13th month
    months[0] = "January"       #trying to rename Jan to January
except:
    print("Cannot make changes to a tuple")
    
    
#additional resources
#https://www.tutorialspoint.com/python/python_tuples.htm
