# Define a class named Product
class Product:
   # Define the constructor 
    def __init__(self, product_id, product_name, description, premium):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.premium = premium
        self.status = "Active"
    # Update the product information
    def update_product(self, new_product_name, new_description, new_premium):
        if new_premium <= 0:
            print("Product premium must be greater than zero.")
            return
        else:
            self.product_name = new_product_name
            self.description = new_description
            self.premium = new_premium
            print(f"{self.product_name} has been updated successfully.")
    # Suspend the product
    def suspend_product(self):
        if self.status == "Suspended":
            print(f"{self.product_name} is already suspended.")
            return
        else:
            self.status = "Suspended"
            print(f"{self.product_name} has been suspended successfully.")
    # Reactivate the product
    def reactivate_product(self):
        if self.status == "Active":
            print(f"{self.product_name} is already active.")
            return
        else:
            self.status = "Active"
            print(f"{self.product_name} has been reactivated successfully.")
    # Remove the product
    def remove_product(self):
        if self.status == "Removed":
            print(f"{self.product_name} is already removed.")
            return
        else:
            self.status = "Removed"
            print(f"{self.product_name} has been removed successfully.")             

if __name__ == "__main__":
    # Create one product to test the class
    health_product = Product("PR001", "Health Insurance", "Provides basic health coverage", 5000)   

    # Display the saved product information
    print(f"Product ID: {health_product.product_id}")
    print(f"Product Name: {health_product.product_name}")
    print(f"Description: {health_product.description}")
    print(f"Premium: ${health_product.premium:,}")
    print(f"Status: {health_product.status}")

    # Test updating the product
    health_product.update_product("Premium Health Insurance", "Provides expanded health coverage", 7500)

    print(f"Updated Product Name: {health_product.product_name}")
    print(f"Updated Description: {health_product.description}")
    print(f"Updated Premium: ${health_product.premium:,}")
    print(f"Product Status: {health_product.status}")

    # Test an invalid product update
    health_product.update_product("Invalid Health Product", "This update should not be accepted", -100)

    print(f"Product Name after invalid update: {health_product.product_name}")
    print(f"Premium after invalid update: ${health_product.premium:,}")

    # Test suspending an active product
    health_product.suspend_product()

    print(f"Status after suspension: {health_product.status}")

    # Test suspending an already suspended product
    health_product.suspend_product()

    # Test reactivating a suspended product
    health_product.reactivate_product()

    print(f"Status after reactivation: {health_product.status}")

    # Test reactivating an already active product
    health_product.reactivate_product()

    # Test removing an active product
    health_product.remove_product()

    print(f"Status after removal: {health_product.status}")

    # Test removing an already removed product
    health_product.remove_product()