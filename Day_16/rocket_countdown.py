counter = 1
valid = True

while counter != 0:
    if valid == True:
        counter = int(input("Enter starting number: "))
        valid = False
    elif counter > 0:
        print(counter)
        counter -= 1
    elif counter != 0:
        print("Please enter a valid input")
        valid = True
print("Blast off!")