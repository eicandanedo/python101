#the purpose of this program is to convert hours to minutes
hours = input("Enter number of hours: ")

#try to convert the inputted hours to a integer
try:
    hours = float(hours)
    minutes = hours*60
    print(minutes)

#if the conversion fails, print out error message
except:
    print("Sorry hours must be a number.")


input("press any key to quit")
