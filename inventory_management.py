"""
Inventory Management System
Manages store inventory with products, prices, and quantities
"""

import os

# Global list to store product records
inventory = []

def load_inventory():
    """Load inventory data from inventory.txt file"""
    global inventory
    inventory = []
    
    if not os.path.exists('inventory.txt'):
        print("No existing inventory file found. Starting fresh.")
        return
    
    try:
        with open('inventory.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 4:
                        product = {
                            'id': parts[0],
                            'name': parts[1],
                            'price': float(parts[2]),
                            'quantity': int(parts[3])
                        }
                        inventory.append(product)
        print(f"Loaded {len(inventory)} product(s).")
    except Exception as e:
        print(f"Error loading inventory: {e}")

def save_inventory():
    """Save all inventory data to inventory.txt file"""
    try:
        with open('inventory.txt', 'w') as file:
            for product in inventory:
                line = f"{product['id']},{product['name']},{product['price']},{product['quantity']}\n"
                file.write(line)
        print("Inventory saved successfully.")
    except Exception as e:
        print(f"Error saving inventory: {e}")

def product_id_exists(product_id):
    """Check if a product ID already exists"""
    for product in inventory:
        if product['id'] == product_id:
            return True
    return False

def find_product_by_id(product_id):
    """Find and return a product by its ID"""
    for product in inventory:
        if product['id'] == product_id:
            return product
    return None

def add_product():
    """Add a new product to inventory"""
    print("\n=== Add Product ===")
    
    # Get Product ID
    product_id = input("Enter Product ID: ").strip()
    if not product_id:
        print("Error: Product ID cannot be empty.")
        return
    
    if product_id_exists(product_id):
        print("Error: Product ID already exists.")
        return
    
    # Get Product Name
    product_name = input("Enter Product Name: ").strip()
    if not product_name:
        print("Error: Product name cannot be empty.")
        return
    
    # Get Price
    try:
        price = float(input("Enter Price: "))
        if price <= 0:
            print("Error: Price must be greater than 0.")
            return
    except ValueError:
        print("Error: Price must be a valid number.")
        return
    
    # Get Quantity
    try:
        quantity = int(input("Enter Quantity: "))
        if quantity < 0:
            print("Error: Quantity cannot be negative.")
            return
    except ValueError:
        print("Error: Quantity must be a valid integer.")
        return
    
    # Create product record
    product = {
        'id': product_id,
        'name': product_name,
        'price': price,
        'quantity': quantity
    }
    
    inventory.append(product)
    save_inventory()
    print(f"\nProduct '{product_name}' added successfully!")

def update_product_quantity():
    """Update the quantity of an existing product"""
    print("\n=== Update Product Quantity ===")
    
    product_id = input("Enter Product ID to update: ").strip()
    
    product = find_product_by_id(product_id)
    
    if not product:
        print("Error: Product ID not found.")
        return
    
    print(f"\nProduct: {product['name']}")
    print(f"Current Quantity: {product['quantity']}")
    
    # Get new quantity
    try:
        new_quantity = int(input("Enter new Quantity: "))
        if new_quantity < 0:
            print("Error: Quantity cannot be negative.")
            return
    except ValueError:
        print("Error: Quantity must be a valid integer.")
        return
    
    # Update quantity
    product['quantity'] = new_quantity
    save_inventory()
    print(f"\nQuantity updated successfully! New Quantity: {new_quantity}")

def display_all_products():
    """Display all products in inventory"""
    print("\n=== All Products ===")
    
    if not inventory:
        print("No products in inventory.")
        return
    
    print(f"\n{'Product ID':<12} {'Product Name':<25} {'Price':<12} {'Quantity':<10}")
    print("-" * 70)
    
    for product in inventory:
        print(f"{product['id']:<12} {product['name']:<25} ${product['price']:<11.2f} {product['quantity']:<10}")
    
    print(f"\nTotal Products: {len(inventory)}")

def display_total_inventory_value():
    """Calculate and display the total inventory value"""
    print("\n=== Total Inventory Value ===")
    
    if not inventory:
        print("No products in inventory. Total Value: $0.00")
        return
    
    total_value = sum(product['price'] * product['quantity'] for product in inventory)
    
    print(f"\nTotal Products: {len(inventory)}")
    print(f"Total Inventory Value: ${total_value:.2f}")
    
    print("\nBreakdown:")
    for product in inventory:
        value = product['price'] * product['quantity']
        print(f"  {product['name']}: ${value:.2f} ({product['quantity']} × ${product['price']:.2f})")

def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("Inventory Management System")
    print("=" * 50)
    print("1. Add Product")
    print("2. Update Product Quantity")
    print("3. Display All Products")
    print("4. Display Total Inventory Value")
    print("5. Exit")
    print("=" * 50)

def main():
    """Main program loop"""
    print("Welcome to Inventory Management System!")
    load_inventory()
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            add_product()
        elif choice == '2':
            update_product_quantity()
        elif choice == '3':
            display_all_products()
        elif choice == '4':
            display_total_inventory_value()
        elif choice == '5':
            print("\nSaving all changes...")
            save_inventory()
            print("Thank you for using the Inventory Management System!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
