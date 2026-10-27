def display_welcome():
    print("Welcome to movie night!")
    print("Ticket Prices:")
    print("ages 0 to 12: $8.00")
    print("ages 13 to 64: or $12.00")
    print("ages 65 and older: $9.00")

def display_receipt(quantity, ticket_price, total):
    print("Receipt:")
    print(f"Number of tickets: {quantity}")
    print(f"Price per ticket: {ticket_price:.2f}")
    print(f"Total: ${total:.2f}")