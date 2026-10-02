numbers = [2, 4, 6, 8]
doubled = []

for number in numbers:
    doubled.append(number * 2)

print(numbers)
print(doubled)

doubled_alt = [number * 2 for number in numbers]
print(doubled_alt)

names = ["Fred", "Wilma", "Barney"]
upper_names = [name.upper() for name in names]

print(upper_names)

numbers = [3,8,12,5,20,31,4]

numbers.sort()

bigger_than_10 = []

for number in numbers:
    if number > 10:
        bigger_than_10.append(number)

print(bigger_than_10)

bigger_than_10 = [number for number in numbers if number > 10 ]

print(bigger_than_10)

