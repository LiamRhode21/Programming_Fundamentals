from .display import display_welcome, display_receipt
from .validation import get_valid_quantity, get_valid_age
from .pricing import get_ticket_price, calculate_total

def main():
    display_welcome()
    age = get_valid_age()
    tickets = get_valid_quantity()
    ticket_price = get_ticket_price(age)
    total = calculate_total(tickets, ticket_price)
    display_receipt(tickets, ticket_price, total)

if __name__ == "__main__":
    main()
