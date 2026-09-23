
print(f"Welcome to the Ultimate Gym \nPlease select a package: \n- Package A: $40/month, 4 months \n- Package B: $55/month, 8 months \n- Package C: $75/month, 12 months \n- Package D: $100/month, 12 month")

package = input("Enter your package letter (A, B, C, D): ")

match package.upper():
    case "A":
        print(f"You have selected Package A \nYour monthly fee is $40 \nYour total fee is $160")
    case "B":
        print(f"You have selected Package B \nYour monthly fee is $55 \nYour total fee is $440")
    case "C":
        print(f"You have selected Package C \nYour monthly fee is $75 \nYour total fee is $900")
    case "D":
        print(f"You have selected Package A \nYour monthly fee is $100 \nYour total fee is $1200")