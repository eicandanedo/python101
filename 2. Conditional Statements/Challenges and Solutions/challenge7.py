#asks user for subtotal and if they are eligible for prime
subtotal = int(input("What is your subtotal price: "))

prime = input("Are you a prime member? (y/n) ")


if prime == "y" or subtotal >= 50:
    shipping = 0
else:
    shipping = 8

total = subtotal + shipping
print(f"Your shipping fee is ${shipping}. Your total price is ${total}")



input('Press any key to quit')
