def print_header(title):
    print("\n" + "=" * 40)
    print(f"{title:^40}")
    print("=" * 40)

def print_footer():
    print("-" * 40)

def get_item_details():
    item_name = input("Enter item name: ").strip()
    if not item_name:
        print("Item name cannot be empty. Skipping item.")
        return None
    price_str = input(f"Enter price for one '{item_name}': $")
    item_price = float(price_str)

    quantity_str = input(f"Enter quantity for '{item_name}': ")
    item_quantity = int(quantity_str)

    if item_price < 0 or item_quantity <= 0:
        print("Price must be non-negative and quantity must be positive. Skipping item.")
        return None

    return {"name": item_name, "price": item_price, "quantity": item_quantity}

def calculate_item_total(item):
    return item["price"] * item["quantity"]

def calculate_subtotal(bill_items):
    subtotal = 0.0
    for item in bill_items:
        subtotal += calculate_item_total(item)
    return subtotal

def apply_discounts(subtotal):
    discount_percentage = 0.0
    discount_description = "No discount"

    if subtotal >= 200:
        discount_percentage = 15.0
        discount_description = "15% Super Saver Discount!"
    elif subtotal >= 100:
        discount_percentage = 10.0
        discount_description = "10% Value Discount"
    elif subtotal >= 50:
        discount_percentage = 5.0
        discount_description = "5% Off Your Purchase"

    discount_amount = (subtotal * discount_percentage) / 100.0
    return discount_amount, discount_percentage, discount_description

def display_bill(bill_items, subtotal, discount_amount, discount_percentage, discount_description, final_total):
    print_header("RECEIPT")
    print(f"{'Item':<20} {'Qty':<5} {'Price':<7} {'Total':<7}")
    print("-" * 40)

    for item in bill_items:
        item_line_total = calculate_item_total(item)
        print(f"{item['name']:<20} {item['quantity']:<5} ${item['price']:.2f}  ${item_line_total:.2f}")

    print_footer()
    print(f"{'Subtotal:':<30} ${subtotal:>7.2f}")

    if discount_amount > 0:
        print(f"{discount_description:<30} -${discount_amount:>6.2f}")
        print_footer()

    print(f"{'TOTAL DUE:':<30} ${final_total:>7.2f}")
    print_footer()
    print(f"{'Thank you for shopping with us!':^40}")
    print("=" * 40 + "\n")

def main_menu():
    print_header("GROCERY BILLING SYSTEM")
    print("1. Add Item to Bill")
    print("2. View Current Bill Items")
    print("3. Finalize and Print Bill")
    print("4. Start New Bill")
    print("5. Exit")
    print_footer()
    choice = input("Enter your choice (1-5): ")
    return choice

def view_current_items(bill):
    print_header("CURRENT BILL ITEMS")
    if not bill:
        print("No items added to the bill yet.")
        print_footer()
        return

    for i, item in enumerate(bill):
        print(f"{i+1}. {item['name']} (Qty: {item['quantity']}, Price: ${item['price']:.2f})")
    print_footer()
    print(f"Current Subtotal: ${calculate_subtotal(bill):.2f}")
    print_footer()

if __name__ == "__main__":
    current_bill = []

    while True:
        user_choice = main_menu()

        if user_choice == '1':
            print_header("ADD ITEM")
            item_data = get_item_details()
            if item_data:
                current_bill.append(item_data)
                print(f"'{item_data['name']}' added successfully.")
            print_footer()

        elif user_choice == '2':
            view_current_items(current_bill)

        elif user_choice == '3':
            if not current_bill:
                print("Bill is empty. Add items before finalizing.")
                continue

            sub = calculate_subtotal(current_bill)
            disc_amt, disc_perc, disc_desc = apply_discounts(sub)
            final = sub - disc_amt
            display_bill(current_bill, sub, disc_amt, disc_perc, disc_desc, final)
            print("Bill finalized. Starting a new bill for the next customer.")
            current_bill = []

        elif user_choice == '4':
            if current_bill:
                confirm = input("Current bill has items. Are you sure you want to start a new bill? (yes/no): ").lower()
                if confirm == 'yes':
                    current_bill = []
                    print("New bill started.")
                else:
                    print("Operation cancelled.")
            else:
                current_bill = []
                print("New bill started (current was empty).")
            print_footer()

        elif user_choice == '5':
            print_header("GOODBYE!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 5.")
            print_footer()