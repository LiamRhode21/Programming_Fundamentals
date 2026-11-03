def get_valid_int(prompt):
    while True:
        try:
            return int(input(f"{prompt}: "))
        except ValueError:
            print("Please enter an integer.")

# print(get_valid_int("Enter number of chickens"))

def get_non_empty_string(prompt):
    while True:
        value = input(f"{prompt}: ")
        if value.strip():
            break
        else:
            print("Please enter a valid string")
    return value