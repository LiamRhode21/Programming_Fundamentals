my_square = int(input("Enter your square: "))
my_square += 1
square_sum = 0

for number in range(1, my_square):
    square_sum += (number ** 2)

print(f"The sum of squares is {square_sum}")