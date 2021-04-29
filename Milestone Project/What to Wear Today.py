import time
#the time module allows you to work with dates and times.
#this program will tell you what to wear depending on the day of the week using the time module
#see python docs for time module directives https://docs.python.org/3/library/time.html

#storing day of week in variable today
today = time.strftime("%A")

#tells the user what day of the week it is
print("Today is " + today)

if today == "Saturday" or today == "Sunday":
    print("Dress Casual")
elif today == "Friday":
    print("Dress Business Casual")
else:
    print("Dress Business Professional")


input("press any key to quit")
