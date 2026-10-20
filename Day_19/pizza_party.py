def calculate_order_total(pizza_count, price_each, delivery_fee = 5.00):
    return pizza_count * price_each + delivery_fee



pizza_count = int(input("Number of pizzas: "))
price_per = float(input("Price per pizza: "))
delivery_fee = float(input("Enter delivery fee: "))
custom_total_delivery = calculate_order_total(pizza_count, price_per, delivery_fee)
total_delivery = calculate_order_total(pizza_count, price_per)
delivery_fee = 0
total_pickup = calculate_order_total(pizza_count, price_per, delivery_fee)
print(f"Custom delivery fee total: ${custom_total_delivery:.2f}")
print(f"Delivery total: ${total_delivery:.2f}")
print(f"Pickup total: ${total_pickup:.2f}")