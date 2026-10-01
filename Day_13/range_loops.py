# Range loops use for loops
# range() generates a sequence of numbers
# those numbers can be used as loop counters
# syntax
# range(start, stop, step)
# start is inclusive, stop is exclusive

# print 1 - 5
for number in range(1,6):
    print(number)

# calculate and print the cubes of numbers 0 to 4
for number in range(0,5):
    cube = number ** 3
    print(f"{number} cubed is {cube}")

# even numbers
for number in range(4,21,2):
    print(number)

# countdown
for number in range(5,0,-1):
    print(number)

# Strings are a list of characters
name = "Liam Rhode"
for letter in name:
    print(letter)
