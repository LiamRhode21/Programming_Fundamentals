birthdays = {
    "dan": "april 14th",
    "gary" : "june 23rd",
    "richard" : "february 2nd",
    "jessica" : "october 30th",
    "mary" : "december 25th"
}

input_name = input("Enter a name: ")

if input_name in birthdays:
    print(f"{input_name}'s birthday is {birthdays[input_name]}")
else:
    print(f"Sorry, we don't have {input_name}'s birthday")