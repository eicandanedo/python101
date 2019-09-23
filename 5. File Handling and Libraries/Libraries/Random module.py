import random


#random library allows you to incorporate randomness into your programs

dice_roll = random.randint(1,6)
print(f"You rolled a {dice_roll}")


coin = random.choice(["heads", "tails"])
print(f"You coin landed on {coin}")

#Additional Resources
#https://docs.python.org/3/library/random.html
