with open("shakespeare.txt") as my_book:
    contents = my_book.read()

print(contents)


my_book.write("\nThree Witches")
