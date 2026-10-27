def get_valid():
    while True:
        try:
            return int(input("How many? "))
        except ValueError:
            print("Please enter an integer.")