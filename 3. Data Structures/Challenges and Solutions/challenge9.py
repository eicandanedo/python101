#programs purpose is to output the number of scabble points the word provided amounts to

#Request user input word
word = input("type a word to find its point value in Scrabble: ").lower()


#Using dictionary to pair letter with point value
points = {'a': 1, 'l': 1, 'w':4,
          'b': 3, 'm': 3, 'x': 8,
          'c': 3, 'n': 1, 'y':4,
          'd': 2, 'o': 1, 'z':10,
          'e': 1, 'p': 3,
          'f': 4, 'q': 10,
          'g': 2, 'r': 1,
          'h': 4, 's': 1,
          'i': 1, 't': 1,
          'j': 8, 'u': 1,
          'k': 5, 'v':1
          }

#Player starts with 0 points
score = 0

#Add the points of each letter in word using for loop
for letter in word:
     score+= points.get(letter)


print(f"{word} is {score} points")
input("press any key to quit")
