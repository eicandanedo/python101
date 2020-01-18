#ask user for length of square and convert to integer

side = int(input("How long is the side of the square? "))

perimeter = side + side + side + side
p = side * 4
area  = side * side

print(f"The perimeter is {perimeter} feet")
print(f"The area is {area} feet)

input()
