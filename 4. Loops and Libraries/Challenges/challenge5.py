#challenge 4
#creates a program that asks user author of Romeo and Juliet
#if the user enters the correct answer, exit the loop
#if the user answers incorrectly, let them try again

while True:
    q1 = input("Who is the author of Romeo and Juliet: ")
    if q1=="Shakespeare":
        print("Correct")
        break
    else:
        print("Incorrect. Please try again \n")
        continue
    
