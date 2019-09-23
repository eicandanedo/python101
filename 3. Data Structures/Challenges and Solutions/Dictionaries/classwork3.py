#creating cart dictionary
cart = {
	'customer': 'Monty Python', 
	'store id': 101, 
	'item': [
		{'name': 'Chocolate', 'quantity': 5, 'price': 2},
		{'name': 'Pizza', 'quantity': 2, 'price': 10},
		{'name': 'Flowers', 'quantity': 1, 'price': 10}
	]
}



#Initializing total price as $0 and looping through each item in cart to calculate total price
total_price = 0
for x in cart['item']:
	total_price += x['price']*x['quantity']

#printing total price to console	
print(f'Your total price is ${total_price} plus tax')


input('press any key to quit')


