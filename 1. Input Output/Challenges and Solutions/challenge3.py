#ask user for length of square and convert to integer
side = int(input("How long is the side of the square? "))

#caluclate perimeter and area
perimeter = side + side + side + side
area  = side * side

#output results to console and quit
print(f"The perimeter is {perimeter} feet")
print(f"The area is {area} feet squared")
input('press any key to quit')
