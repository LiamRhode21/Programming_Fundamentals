cities = ["Edmonton", "Paris", "Munich", "Berlin", "Amsterdam", "Prague"]
germany = ["Munich", "Berlin"]

cities.remove("Edmonton")

new_city = input("Enter an interesting city: ")

cities.append(new_city)

cities.sort()

print(f"Our list of interesting cities in alphabetical order is: \n {cities}")

for city in cities:
    if city not in germany:
        print(f"{city} is an interesting city that we can visit")