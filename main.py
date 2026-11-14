# Import the three project classes
from policyholder import Policyholder
from product import Product
from payment import Payment

# Create the insurance product
health_insurance = Product("PR001", "Health Insurance", "Provides comprehensive health coverage", 5000)

# Confirm that the product was created
print(f"Product ID: {health_insurance.product_id}")
print(f"Product Name: {health_insurance.product_name}")
print(f"Premium: ${health_insurance.premium:,}")
print(f"Product Status: {health_insurance.status}")

# Create the first policyholder
policyholder_one = Policyholder("PH001", "John Mensah", "john.mensah@example.com")

# Create the second policyholder
policyholder_two = Policyholder("PH002", "Sarah Adeyemi", "sarah.adeyemi@example.com")

# Confirm the first Policyholder
print(f"Policyholder One:")
print(f"ID: {policyholder_one.policyholder_id}")
print(f"Name: {policyholder_one.name}")
print(f"Status: {policyholder_one.status}")
print("-------------------------------")

# Confirm the second policyholder
print("Policyholder Two:")
print(f"ID: {policyholder_two.policyholder_id}")
print(f"Name: {policyholder_two.name}")
print(f"Status: {policyholder_two.status}")

# Assign Health Insurance to both policyholders
policyholder_one.add_product(health_insurance)

policyholder_two.add_product(health_insurance)

# Confirm the product baskets
print(f"{policyholder_one.name}'s product count: {len(policyholder_one.products)}")

print(f"{policyholder_two.name}'s product count: {len(policyholder_two.products)}")

# Create a payment for the first policyholder
payment_one = Payment("PAY001", policyholder_one, health_insurance, health_insurance.premium)

# Create a payment for the second policyholder
payment_two = Payment("PAY002", policyholder_two, health_insurance, health_insurance.premium)

# Confirm both payments
print(f"{policyholder_one.name}'s Payment:")
print(f"Payment ID: {payment_one.payment_id}")
print(f"Policyholder: {payment_one.policyholder.name}")
print(f"Product: {payment_one.product.product_name}")
print(f"Amount Due: ${payment_one.amount_due:,}")
print(f"Payment Status: {payment_one.status}")

print("-------------------------------------")

print(f"{policyholder_two.name}'s Payment:")
print(f"Payment ID: {payment_two.payment_id}")
print(f"Policyholder: {payment_two.policyholder.name}")
print(f"Product: {payment_two.product.product_name}")
print(f"Amount Due: ${payment_two.amount_due:,}")
print(f"Payment Status: {payment_two.status}")

# Process the first policyholder's payment
payment_one.process_payment(health_insurance.premium)

# Process the second policyholder's payment
payment_two.process_payment(health_insurance.premium)

# Display the first Policyholder's payment
print(f"{policyholder_one.name}'s Payment Result:")
print(f"Payment ID: {payment_one.payment_id}")
print(f"Amount Paid: ${payment_one.amount_paid:,}")
print(f"Payment Status: {payment_one.status}")

print("---------------------------")

# Display the second Policyholder's payment
print(f"{policyholder_two.name}'s Payment Result:")
print(f"Payment ID: {payment_two.payment_id}")
print(f"Amount Paid: ${payment_two.amount_paid:,}")
print(f"Payment Status: {payment_two.status}")

# Record the first policyholder's completed payment
policyholder_one.add_payment(payment_one)

# Record the second policyholder's completed payment
policyholder_two.add_payment(payment_two)

# Confirm both payments
print(f"{policyholder_one.name}'s recorded payments: {len(policyholder_one.payments)}")

print(f"{policyholder_two.name}'s recorded payments: {len(policyholder_two.payments)}")

# Display the final policyholder accounts
print("\nFINAL POLICYHOLDER ACCOUNTS")

print("------------------------------")

# Display first policyholder's account
policyholder_one.display_account_details()

# Display second policyholder's account
policyholder_two.display_account_details()

# Demonstrate policyholder management
print("\nPOLICYHOLDER MANAGEMENT DEMONSTRATION")

print("------------------------------------------")

# Demonstrate registration
policyholder_two.register()

# Demonstrate suspension
policyholder_two.suspend()

print(f"Status after suspension: {policyholder_two.status}")

# Demonstrate reactivation
policyholder_two.reactivate()

print(f"Status after reactivation: {policyholder_two.status}")

# Create a separate product for management testing
motor_insurance = Product("PR002", "Motor Insurance", "Provides basic motor vehicle coverage", 8000)

print("\nPRODUCT MANAGEMENT DEMONSTRATION")

print("------------------------------------------")

# Update the product
motor_insurance.update_product("Premium Motor Insurance", "Provides expanded motor vehicle coverage", 10000)

print(f"Updated Product Name: {motor_insurance.product_name}")
print(f"Updated Premium: ${motor_insurance.premium:,}")

# Suspend the product
motor_insurance.suspend_product()

print(f"Status after suspension: {motor_insurance.status}")

# Reactivate the product
motor_insurance.reactivate_product()

print(f"Status after reactivation: {motor_insurance.status}")

# Remove the product
motor_insurance.remove_product()

print(f"Status after removal: {motor_insurance.status}")

# Demonstrate payment reminders and penalties
print("\nPAYMENT MANAGEMENT DEMONSTRATION")

print("---------------------------------")

# Create a fresh unpaid payment
overdue_payment = Payment("PAY003", policyholder_one, health_insurance, health_insurance.premium)

# Send the first reminder
overdue_payment.send_reminder()

# Apply a penalty
overdue_payment.apply_penalty(500)

# Send another reminder
overdue_payment.send_reminder()

# Display the final penalty details
print(f"Payment ID: {overdue_payment.payment_id}")
print(f"Penalty: ${overdue_payment.penalty:,}")
print(f"Payment Status: {overdue_payment.status}")