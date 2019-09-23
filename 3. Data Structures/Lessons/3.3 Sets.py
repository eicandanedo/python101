#sets are a light-weight data structure
#They are unordered comma separated values that do not allow for duplicate entries
call_history = {"Mom", "Mom","Mom", "Mom","Dad", "Dad", "Pizza Hutt", "Free Vacation Scam"}
print(call_history)


#the len function will find the number of items in an object 
unique_calls = len(call_history)
print(unique_calls)



#i teach two classes and listed student names in a set
python = {"Jake", "Abby", "Leo", "Zoe"}
excel = {"Ava", "Zoe", "Carl", "Leo"}

#A union combines both sets and removes duplicates
all_students = python|excel
print(all_students)

#an intersection is where both sets share the same values.
students_in_both = python&excel
print(students_in_both)





