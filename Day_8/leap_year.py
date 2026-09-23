year = int(input("Enter your year: "))

leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
leap_year_string = " "

if not leap_year:
    leap_year_string = " Not "

print(f"{year} is{leap_year_string}a leap year")
