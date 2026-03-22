class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class Ticket:
    def __init__(self, person, place, seat):
        self.person = person
        self.place = place
        self.seat = seat

items = []
tickets = []

def add_item():
    name = input("\nEnter Item Name: ")
    try:
        qty = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        items.append(Item(name, qty, price))
        print("\nItem Added.")
    except ValueError:
        print("\nInvalid input. Quantity must be an integer and Price a number.")

def display_items():
    if not items:
        print("\nNo items found.")
        return
    print("\n------ ITEM LIST ------")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item.name} | Qty: {item.quantity} | Price: {item.price:.2f}")

def generate_bill():
    if not items:
        print("\nBill is empty.")
        return
    total = 0
    print("\n------- BILL -------")
    for item in items:
        amt = item.quantity * item.price
        print(f"{item.name} x {item.quantity} = {amt:.2f}")
        total += amt
    print(f"--------------------\nTotal: {total:.2f}")

# Main Menu Loop
while True:
    print("\n========= MENU =========")
    print("1. Add Item\n2. Display Items\n3. Generate Bill\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1': add_item()
    elif choice == '2': display_items()
    elif choice == '3': generate_bill()
    elif choice == '4': 
        print("Goodbye.")
        break
    else: print("Invalid option.")
