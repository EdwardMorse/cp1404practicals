"""
CP1404 Practical 1
Shop calculator
"""

number_of_items = int(input("Enter the number of items: "))

total_price = 0.00

while number_of_items < 0:
    print("Invalid number of items.")
    number_of_items = int(input("Enter the number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Enter price of item $: "))
    total_price += price_of_item
if total_price > 100:
    total_price = total_price * 0.9
print(f"Your total price is ${total_price:.2f}")
