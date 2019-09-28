import random
#Random number game 

#generating random number between 1 and 10
secretNumber = random.randint(1,10)
guess = None


#while loop will repeat until player guesses correct number
while guess != secretNumber:
    #ask user to enter a number and convert to integer (strings or floats not allowed)
    #tell user if they guessed correctly or too high or too low
    try:
        guess = int(input("Enter your guess: "))
        if guess < secretNumber:
            print("Guess is too low")
        elif guess > secretNumber:
            print("Guess is too high")
        elif guess== secretNumber:
            print(f"{guess} is Correct!")
            break

    
    except:
        print('Not a valid number')


    
    

print("Game Over")
