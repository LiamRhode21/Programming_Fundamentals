def calculate_donations(**donations):
    total = 0
    for key, value in donations.items():
        print(f"{key}: ${value:.2f}")
        total += value
    return total

total = calculate_donations(Alex=10, Sam=7.50, Riley=12.25)
print(f"Total raised: ${total:.2f}")

total = calculate_donations()
print(f"Total raised: ${total:.2f}")