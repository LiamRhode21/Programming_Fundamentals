month_number = input("Enter a month number(1 - 12): ")
is_valid = True

match month_number:
    case "1":
        month = "January"
    case "2":
        month = "February"
    case "3":
        month = "March"
    case "4":
        month = "April"
    case "5":
        month = "May"
    case "6":
        month = "June"
    case "7":
        month = "July"
    case "8":
        month = "August"
    case "9":
        month = "September"
    case "10":
        month = "October"
    case "11":
        month = "November"
    case "12":
        month = "December"
    case _:
        is_valid = False
        print("Invalid Input.")

if is_valid:
    print(f"Month is: \n{month}")