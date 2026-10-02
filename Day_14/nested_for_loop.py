for row in range(1,4):
    for seat in range(1,5):
        name = input("Enter your name: ")
        print(f"Row{row}, Seat {seat} is purchased by {name}")

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
stars = []

for row in range(rows):
    print("")
    for column in range(columns):
        print("*", end = "")
print("\n")

for row in range(rows):
    print("*" * columns)