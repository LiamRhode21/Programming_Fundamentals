cities = ["Edmonton", "Paris", "Munich", "Berlin", "Amsterdam", "Prague"]

cities.remove("Edmonton")

new_city = input("Enter an interesting city: ")

cities.append(new_city)

cities.sort()

print(f"Our list of interesting cities in alphabetical order is: \n {cities}")

