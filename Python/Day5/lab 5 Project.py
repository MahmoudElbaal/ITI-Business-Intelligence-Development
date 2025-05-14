"""
                 ### Product Inventory Management System ###

1) Add New Product
2) List All Products
3) Delete Products by Category
4) Update Product Price       
5) Exit Program


"""
import json

class Product:
    def __init__(self, name, product_id, price, quantity, category):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.quantity = quantity
        self.category = category
    
    def display_info(self):
        print(f"Name: {self.name}, ID: {self.product_id}, Price: ${self.price}, Quantity: {self.quantity}, Category: {self.category}")
        
    def to_dict(self):
        return {
            "name": self.name,
            "product_id": self.product_id,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category
        }

class ProductManager:
    def __init__(self):
        self.products = []
        self.file_path = "products.json"
        self.load_from_file()
        
    def add_product(self, name, product_id, price, quantity, category):
        if any(p.product_id == product_id for p in self.products):
            print(f"Error: Product with ID {product_id} already exists!")
            return
        self.products.append(Product(name, product_id, price, quantity, category))
        self.save_to_file()
        print(f"Product {name} added successfully")
        
    def print_all_products(self):
        if not self.products:
            print("No Products Found")
        else:
            for product in self.products:
                product.display_info()
           
    def update_price_by_id(self, product_id, new_price):
        for product in self.products:
            if product.product_id == product_id:
                product.price = new_price
                self.save_to_file()
                print(f"Price updated for product ID {product_id} to ${new_price}")
                return
        print("Product not found!")
        
    def delete_by_category(self, category):
        initial_count = len(self.products)
        self.products = [p for p in self.products if p.category.lower() != category.lower()]
        if len(self.products) < initial_count:
            self.save_to_file()
            print(f"All products in category '{category}' deleted successfully.")
        else:
            print(f"No products found in category '{category}'")
        
    def save_to_file(self):
        with open(self.file_path, "w") as file:
            json.dump([p.to_dict() for p in self.products], file, indent=4)
            
    def load_from_file(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.products = [Product(p["name"], p["product_id"], p["price"], p["quantity"], p["category"]) for p in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.products = []

class InventoryFrontend:
    def __init__(self):
        self.manager = ProductManager()
        
    def display_menu(self):
        while True:
            print("\n\t\tProduct Inventory Management System\t\t")
            print("1) Add New Product")
            print("2) List All Products")
            print("3) Delete Products by Category")
            print("4) Update Product Price")
            print("5) Exit Program")
            
            choice = input("Enter your choice (1-5): ") 
            
            if choice == "1":
                name = input("Enter Product Name: ")
                product_id = input("Enter Product ID: ")
                price = float(input("Enter Price: $"))
                quantity = int(input("Enter Quantity: "))
                category = input("Enter Category: ")
                self.manager.add_product(name, product_id, price, quantity, category)
                
            elif choice == "2":
                self.manager.print_all_products()
            
            elif choice == "3":
                category = input("Enter Category to Delete: ")
                self.manager.delete_by_category(category)
                
            elif choice == "4":
                product_id = input("Enter Product ID to Update: ")
                new_price = float(input("Enter New Price: $"))
                self.manager.update_price_by_id(product_id, new_price)
            
            elif choice == "5":
                print("Exiting program...")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    system = InventoryFrontend()
    system.display_menu()