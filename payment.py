# Bring the Policyholder class into this file
from policyholder import Policyholder

# Bring the Product class into this file
from product import Product

class Payment:
    def __init__(self, payment_id, policyholder, product, amount_due):
        self.payment_id = payment_id
        self.policyholder = policyholder
        self.product = product
        self.amount_due = amount_due
        self.amount_paid = 0
        self.penalty = 0
        self.status = "Pending"
    # Process a payment
    def process_payment(self, amount):
        # Reject zero or negative payments
        if amount <= 0:
            print("Payment amount must be greater than zero.")
            return
        # Reject Suspended Policyholder payment
        if self.policyholder.status != "Active":
            print(f"Payment cannot be processed because {self.policyholder.name} is not active.")
            return
        # Reject Suspended or Removed product
        if self.product.status != "Active":
            print(f"Payment cannot be processed because {self.product.product_name} is not active.")
            return
        # Add the payment amount tothe amount already paid
        self.amount_paid += amount

        # Include the penalty when calculating the total amount required
        total_amount_required = self.amount_due + self.penalty

        # Decide whether the full balance has been paid
        if self.amount_paid >= total_amount_required:
            self.status = "Paid"
            print(f"Payment {self.payment_id} processed successfully.")
        else:
            # Keep a penalized payment overdue until the full balance is paid
            if self.penalty> 0:
                self.status = "Overdue"
            else:
                self.status = "Pending"    
            print("Partial payment received.")
    # Send a payment reminder
    def send_reminder(self):
        if self.status == "Paid":
            print(f"No reminder required for payment {self.payment_id} because it has been paid.")
            return
        else:
            # Calculate outstanding amount
            outstanding_balance = self.amount_due + self.penalty - self.amount_paid
            print(f"Payment reminder for {self.policyholder.name}:")
            print(f"Payment {self.payment_id} has an outstanding balance of ${outstanding_balance:,}")
    # Apply a penalty to an unpaid payment
    def apply_penalty(self, penalty_amount):
        if penalty_amount <= 0:
            print("Penalty amount must be greater than zero.")
            return
        if self.status == "Paid":
            print(f"Penalty cannot be applied to payment {self.payment_id} because it has already been paid.")
            return
        # Add the new amount to existing penalty
        self.penalty += penalty_amount
        # Change payment status to Overdue
        self.status = "Overdue"
        # Calculate the outstanding balance
        outstanding_balance = self.amount_due + self.penalty - self.amount_paid
        print(f"A penalty of ${penalty_amount:,} has been applied to payment {self.payment_id}.")
        print(f"New outstanding balance: ${outstanding_balance:,}.")
            
if __name__ == "__main__":     
    # Create a policyholder for the payment test
    payment_policyholder = Policyholder("PH001", "John Mensah", "john.mensah@example.com")

    # Create a product for the payment test
    payment_product = Product("PR001", "Health Insurance", "Provides basic health coverage", 5000)

    # Create a pending payment
    payment_one = Payment("PAY001", payment_policyholder, payment_product, payment_product.premium)

    # Display the payment information
    print(f"Payment ID: {payment_one.payment_id}")
    print(f"Policyholder: {payment_one.policyholder.name}")
    print(f"Product: {payment_one.product.product_name}")
    print(f"Amount Due: ${payment_one.amount_due:,}")
    print(f"Amount Paid: ${payment_one.amount_paid:,}")
    print(f"Penalty: ${payment_one.penalty:,}")
    print(f"Payment Status: {payment_one.status}")

    # Test processing a full payment
    payment_one.process_payment(5000)

    # Display the updated payment information
    print(f"Amount Paid: ${payment_one.amount_paid:,}")
    print(f"Payment Status: {payment_one.status}")

    # Create a fresh payment for the partial-payment test
    payment_two = Payment("PAY002", payment_policyholder, payment_product, payment_product.premium)

    # Process a partial payment
    payment_two.process_payment(2000)

    # Display the partial-payment result
    print(f"Payment ID: {payment_two.payment_id}")
    print(f"Amount Due: ${payment_two.amount_due:,}")
    print(f"Amount Paid: ${payment_two.amount_paid:,}")
    print(f"Payment Status: {payment_two.status}")

    # Complete the partial payment
    payment_two.process_payment(3000)

    # Display the completed payment
    print(f"Payment ID: {payment_two.payment_id}")
    print(f"Amount Paid: ${payment_two.amount_paid:,}")
    print(f"Payment Status: {payment_two.status}")

    # Create a fresh payment for invalid-payment testing
    payment_three = Payment("PAY003", payment_policyholder, payment_product, payment_product.premium)

    # Test a zero payment
    payment_three.process_payment(0)

    print(f"Amount Paid after zero payment: ${payment_three.amount_paid:,}")
    print(f"Payment Status after zero payment: {payment_three.status}")

    # Test a negative payment
    payment_three.process_payment(-500)

    print(f"Amount Paid after negative payment: ${payment_three.amount_paid:,}")
    print(f"Payment Status after negative payment: {payment_three.status}")

    # Create a policyholder for the suspension test
    suspended_policyholder = Policyholder( "PH002", "Sarah Adeyemi", "sarah.adeyemi@example.com")

    # Suspend the policyholder before payment
    suspended_policyholder.suspend()

    print(f"Policyholder Status: {suspended_policyholder.status}")

    # Create a payment linked to the suspended policyholder
    payment_four = Payment("PAY004", suspended_policyholder, payment_product, payment_product.premium)

    # Attempt payment from the suspended policyholder
    payment_four.process_payment(5000)

    # Confirm that the rejected payment changed nothing
    print(f"Amount Paid after rejected payment: ${payment_four.amount_paid:,}")
    print(f"Payment Status after rejected payment: {payment_four.status}")

    # Create an active policyholder for the product-status test
    active_policyholder = Policyholder("PH003", "David Okafor", "david.okafor@example.com")

    print(f"Policyholder Status: {active_policyholder.status}")

    # Create a fresh product for the suspension test
    suspended_product = Product("PR002", "Motor Insurance", "Provides motor vehicle coverage", 8000)

    # Suspend the product before payment
    suspended_product.suspend_product()

    print(f"Product Status: {suspended_product.status}")

    # Create a payment for the suspended product
    payment_five = Payment("PAY005", active_policyholder, suspended_product, suspended_product.premium)

    # Attempt payment for the suspended product
    payment_five.process_payment(8000)

    # Confirm that the rejected payment changed nothing
    print(f"Amount Paid after rejected payment: ${payment_five.amount_paid:,}")
    print(f"Payment Status after rejected payment: {payment_five.status}")

    # Test a reminder for an unpaid payment
    payment_three.send_reminder()

    # Test the reminder method on a paid payment
    payment_one.send_reminder()

    # Test a valid payment penalty
    payment_three.apply_penalty(500)

    print(f"Penalty: ${payment_three.penalty:,}")
    print(f"Payment Status: {payment_three.status}")

    # Send a reminder after applying the penalty
    payment_three.send_reminder()

    # Test applying a penalty to a paid payment
    payment_one.apply_penalty(500)

    print(f"Penalty after rejected attempt: ${payment_one.penalty:,}")
    print(f"Payment Status: {payment_one.status}")

    # Test an invalid penalty amount
    payment_three.apply_penalty(-100)

    print(f"Penalty after invalid attempt: ${payment_three.penalty:,}")
    print(f"Payment Status: {payment_three.status}")

    # Add the completed payment to its policyholder's account
    payment_policyholder.add_payment(payment_one)

    print(f"Number of recorded payments: {len(payment_policyholder.payments)}")

    # Test duplicate payment prevention
    payment_policyholder.add_payment(payment_one)

    print(f"Number of recorded payments after duplicate attempt: {len(payment_policyholder.payments)}")

    # Create a pending payment for testing
    payment_six = Payment("PAY006", payment_policyholder, payment_product, payment_product.premium)

    # Attempt to add an unpaid payment
    payment_policyholder.add_payment(payment_six)

    # Confirm that the unpaid payment was not added
    print(f"Number of recorded payments after unpaid attempt: {len(payment_policyholder.payments)}")

    # Test payment ownership validation
    suspended_policyholder.add_payment(payment_one)

    print(f"Sarah's recorded payments: {len(suspended_policyholder.payments)}")

    # Add the payment product to the policyholder's account
    payment_policyholder.add_product(payment_product)

    # Display the complete policyholder account
    payment_policyholder.display_account_details()

    # Test payment processing after a penalty
    penalty_test_payment = Payment("PAY007", payment_policyholder, payment_product, payment_product.premium)

    # Add a $500 penalty
    penalty_test_payment.apply_penalty(500)

    # Pay only the original $5,000 amount
    penalty_test_payment.process_payment(5000)

    print(f"Amount Paid: ${penalty_test_payment.amount_paid:,}")
    print(f"Penalty: ${penalty_test_payment.penalty:,}")
    print(f"Payment Status: {penalty_test_payment.status}")

    # Pay the remaining $500 penalty
    penalty_test_payment.process_payment(500)

    print(f"Total Amount Paid: ${penalty_test_payment.amount_paid:,}")
    print(f"Final Payment Status: {penalty_test_payment.status}")