def get_ticket_price(age):
    if age >= 0 and age <= 12:
        return 8.00
    elif age >= 13 and age <= 64:
        return 12.00
    elif age >= 65:
        return 9.00

def calculate_total(quantity, ticket_price):
    total = quantity * ticket_price
    return total

