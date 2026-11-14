# Bring Product class into this file
from product import Product

# Define a class named Policyholder
class Policyholder:
    # Define the constructor method
    def __init__(self, policyholder_id, name, email):
        self.policyholder_id = policyholder_id
        self.name = name
        self.email = email
        self.status = "Active"
        # Create an empty list for the policyholder's products
        self.products = []
        # Create an empty list for the policyholder's payments
        self.payments = []
    # Register the policyholder    
    def register(self):
        if self.status == "Active":
            print(f"{self.name} is already registered and active.")
            return
        else:
            self.status = "Active"
            print(f"{self.name} has been registered successfully.")
    # Suspend the policyholder               
    def suspend(self):
        if self.status == "Suspended":
            print(f"{self.name} is already suspended.")
            return
        else:
            self.status = "Suspended"
            print(f"{self.name} has been suspended successfully.")
    # Reactivate the policyholder
    def reactivate(self):
        if self.status == "Active":
            print(f"{self.name} is already active.")
            return
        else:
            self.status = "Active"
            print(f"{self.name} has been reactivated successfully.")
    # Add a product to the policyholder's account
    def add_product(self, product):
        for existing_product in self.products:
            if existing_product.product_id == product.product_id:
                print(f"{self.name} already has {product.product_name}.")
                return
        # This part runs only if no duplicate was found
        self.products.append(product)
        print(f"{product.product_name} has been added to {self.name}'s account.")
    # Add a completed payment to the policyholder's account
    def add_payment(self, payment):
        # Check whether the payment belongs to this policyholder
        if payment.policyholder.policyholder_id != self.policyholder_id:
            print(f"Payment {payment.payment_id} does not belong to {self.name}.")
            return
        # Check whether the payment is complete
        if payment.status != "Paid":
            print(f"Payment {payment.payment_id} cannot be added because it is not fully paid.")
            return
        # Check for a duplicate payment
        for existing_payment in self.payments:
            if existing_payment.payment_id == payment.payment_id:
                print(f"Payment {payment.payment_id} is already recorded for {self.name}.")
                return
        # Add the valid payment
        self.payments.append(payment)
        print(f"Payment {payment.payment_id} has been added to {self.name}'s account.")
    # Display the policyholder's account details    
    def display_account_details(self):
        print("\nPOLICYHOLDER ACCOUNT")


        print("=================================")


        print(f"Policyholder ID: {self.policyholder_id}")


        print(f"Name: {self.name}")


        print(f"Email: {self.email}")


        print(f"Status: {self.status}")

        # Display the policyholder's products
        print("\nPRODUCTS")

        if not self.products:
            print("No products assigned.")
        else:
            for product in self.products:
                print(f"Product ID: {product.product_id}")
                print(f"Product Name: {product.product_name}")
                print(f"Premium: ${product.premium:,}")
                print(f"Product Status: {product.status}")
                print("-------------------------")  
        # Display the policyholder's completed payments
        print("\nPAYMENTS")

        if not self.payments:
            print("No completed payments recorded.")
        else:
            for payment in self.payments:
                print(f"Payment ID: {payment.payment_id}")
                print(f"Product: {payment.product.product_name}")
                print(f"Amount Due: ${payment.amount_due:,}")
                print(f"Amount Paid: ${payment.amount_paid:,}")
                print(f"Penalty: ${payment.penalty:,}")
                print(f"Payment Status: {payment.status}")
                print("-------------------------------")

if __name__ == "__main__":
    # Create one policyholder to test the class
    policyholder_one = Policyholder("PH001", "John Mensah", "john.mensah@example.com")

    # Display the saved policyholder information
    print(f"Policyholder ID: {policyholder_one.policyholder_id}")
    print(f"Name: {policyholder_one.name}")
    print(f"Email: {policyholder_one.email}")
    print(f"Status: {policyholder_one.status}")

    # Test the registration method
    # Ask the policyholder to register
    policyholder_one.register()

    print(f"Status after registration: {policyholder_one.status}")

    # Test suspending an active policyholder
    policyholder_one.suspend()

    print(f"Status after suspension: {policyholder_one.status}")

    # Test suspending an already suspended policyholder
    policyholder_one.suspend()

    # Test reactivating a suspended policyholder
    policyholder_one.reactivate()

    print(f"Status after reactivation: {policyholder_one.status}")

    # Test reactivating an already active policyholder
    policyholder_one.reactivate()

    # Create a fresh active product for testing
    policy_product = Product("PR001", "Health Insurance", "Provides basic health coverage", 5000)

    # Add the product to John's account
    policyholder_one.add_product(policy_product)

    # Confirm that the product was added
    print(f"Number of products: {len(policyholder_one.products)}" )

    # Test duplicate product prevention
    policyholder_one.add_product(policy_product)

    # Confirm that the duplicate was not added
    print(f"Number of products after duplicate attempt: {len(policyholder_one.products)}")

    # Confirm that the payment basket starts empty
    print(f"Payments: {policyholder_one.payments}")

    # Confirm that the payment basket is a list
    print(type(policyholder_one.payments))

    # Display John's basic account details
    policyholder_one.display_account_details()