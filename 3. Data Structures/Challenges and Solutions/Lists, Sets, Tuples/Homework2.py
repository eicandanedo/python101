vip = ['Jim Halpert', 'Amy Santiago', 'Ron Swanson']

name =  input("What is your name: ").title()

if name in vip:
       cost = 0
else:
       cost = 10

print(f"Ticket price is ${cost}")
       
