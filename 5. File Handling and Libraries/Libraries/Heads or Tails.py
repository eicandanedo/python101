import random
import os
import time

coin = ["heads", "tails"]
scoreboard = open("guess.txt","a+")

times_played = 0
times_correct = 0
while times_played <6:
    #flip coin and ask user to guess heads or tails
    flip = random.choice(coin)
    guess = input("Heads or tails? ".lower())

    #if they guess correctly, increment times_correct variable
    if flip == guess:
        times_correct +=1
        print("Correct!")
    else:
        print("Incorrect!")
    
    #regardless of whether they guess correctly or incorrectly, increment times played and print score
    times_played+=1
    score = round((times_correct/times_played)*100,1)
    print(f"Your accuracy is {score}%")


#save score to text file          
scoreboard.write(f"{os.getlogin()},{time.ctime()}, {score}%\n")
print(f"Your score was saved to {os.getcwd()} in guess.txt")            
scoreboard.close()
        



