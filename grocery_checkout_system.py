price={
    "apple":0.50,
    "banana":0.30,
    "milk":1.20,
    "bread":2.00,
    "cheese":3.50
}

item1_name=input("enter the name of first item: ").lower()
item1_qty=int(input(f"Enter the quantity of {item1_name}:"))

item2_name=input("enter the name of second item: ").lower()
item2_qty=int(input(f"Enter the quantity of {item2_name}:"))

item3_name=input("enter the name of third item: ").lower()
item3_qty=int(input(f"Enter the quantity of {item3_name}:"))


item1_price=price.get(item1_name,0)
item2_price=price.get(item2_name,0)
item3_price=price.get(item3_name,0)


item1_total=item1_price * item1_qty
item2_total=item2_price * item2_qty
item3_total=item3_price * item3_qty

subtotal=item1_total+item2_total+item3_total
tax=subtotal * 0.085
total_amount=subtotal+tax

print("--------Receipt-------")
print(f"{item1_name.capitalize()}: {item1_qty} @ ${item1_price:.2f} each= ${item1_total:.2f}")
print(f"{item2_name.capitalize()}: {item2_qty} @ ${item2_price:.2f} each= ${item2_total:.2f}")
print(f"{item3_name.capitalize()}: {item3_qty} @ ${item3_price:.2f} each= ${item3_total:.2f}")

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total Amount ${total_amount:.2f}")

