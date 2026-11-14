# Insurance Policy Management System

## Project Overview

This project is a Python-based insurance policy management system developed as part of a Master of Science in Data Analytics milestone assignment. The system manages policyholders, insurance products, and payments through separate object-oriented classes.

Policy managers can use the system to register, suspend, and reactivate policyholders; create, update, suspend, reactivate, and remove insurance products; process full or partial payments; send payment reminders; and apply penalties to unpaid payments.

The final demonstration creates two policyholders who purchase and fully pay for the same insurance product. Their complete account details are then displayed.

## Project Requirements

The project addresses the following requirements:

- Create separate classes for policyholders, products, and payments.
- Store each class in a separate Python file.
- Register, suspend, and reactivate policyholders.
- Create, update, suspend, reactivate, and remove insurance products.
- Process full and partial payments.
- Generate payment reminders.
- Apply payment penalties.
- Create at least two policyholders who have paid for a product.
- Display the account details of both policyholders.
- Include instructions for accessing and running the project.

## Technologies Used

- Python 3
- Visual Studio Code
- Object-oriented programming
- Python classes and objects
- Conditional statements
- Methods and functions
- Lists
- Input validation
- Modular file organization

No external Python packages are required.

## Project Structure

```text
insurance-policy-management-system/
|
|-- policyholder.py
|-- product.py
|-- payment.py
|-- main.py
|-- README.md
`-- .gitignore
```

## File Descriptions

### `policyholder.py`

Contains the `Policyholder` class. The class manages policyholder information, account status, assigned products, completed payments, and account displays.

Main methods:

- `register()`
- `suspend()`
- `reactivate()`
- `add_product()`
- `add_payment()`
- `display_account_details()`

### `product.py`

Contains the `Product` class. The class manages insurance product information, product updates, and product status changes.

Main methods:

- `update_product()`
- `suspend_product()`
- `reactivate_product()`
- `remove_product()`

### `payment.py`

Contains the `Payment` class. The class manages payment processing, partial payments, reminders, penalties, outstanding balances, and payment status.

Main methods:

- `process_payment()`
- `send_reminder()`
- `apply_penalty()`

### `main.py`

Imports the three classes and demonstrates the complete policy management workflow.

The demonstration includes:

- Creating an insurance product
- Creating two policyholders
- Assigning the product to both policyholders
- Processing a full payment for each policyholder
- Recording both completed payments
- Displaying both policyholder accounts
- Demonstrating policyholder suspension and reactivation
- Demonstrating product updates and status changes
- Demonstrating payment reminders and penalties

## Class Design

### Policyholder Class

Each policyholder stores:

- Policyholder ID
- Name
- Email address
- Account status
- Assigned products
- Completed payment records

New policyholders automatically begin with the status `Active`. Creating a `Policyholder` object represents registering a new member. The `register()` method confirms or restores the active status.

### Product Class

Each product stores:

- Product ID
- Product name
- Description
- Premium
- Product status

New products automatically begin with the status `Active`.

Product status values used in the project are:

- `Active`
- `Suspended`
- `Removed`

### Payment Class

Each payment stores:

- Payment ID
- Linked policyholder
- Linked insurance product
- Amount due
- Amount paid
- Penalty
- Payment status

Payment status values used in the project are:

- `Pending`
- `Overdue`
- `Paid`

## Business Rules

The system applies the following rules:

1. A new policyholder begins with `Active` status.
2. A suspended policyholder can be reactivated.
3. A policyholder cannot receive the same product twice.
4. A new product begins with `Active` status.
5. A product premium must be greater than zero when updated.
6. A product can be suspended, reactivated, or marked as removed.
7. A payment amount must be greater than zero.
8. A suspended policyholder cannot make a payment.
9. A suspended or removed product cannot accept a payment.
10. Partial payments remain `Pending` when no penalty exists.
11. A penalized payment remains `Overdue` until the full balance is paid.
12. The full amount required equals the product amount due plus any penalty.
13. A fully paid transaction cannot receive another penalty.
14. Only completed payments can be recorded in a policyholder account.
15. A payment can be recorded only for the policyholder who owns it.
16. Duplicate payment IDs cannot be recorded twice in the same account.

## Final Demonstration

The final demonstration in `main.py` creates the following insurance product:

```text
Product ID: PR001
Product Name: Health Insurance
Premium: $5,000
Status: Active
```

It also creates two policyholders:

```text
PH001 - John Mensah
PH002 - Sarah Adeyemi
```

Both policyholders receive Health Insurance and make separate full payments:

```text
PAY001 - John Mensah - $5,000 - Paid
PAY002 - Sarah Adeyemi - $5,000 - Paid
```

The program then displays each policyholder's:

- Policyholder information
- Account status
- Insurance product
- Product premium and status
- Payment ID
- Amount due
- Amount paid
- Penalty
- Payment status

## Payment Reminder and Penalty Demonstration

The project also creates a separate unpaid payment for reminder and penalty testing:

```text
Payment ID: PAY003
Original Amount Due: $5,000
Penalty: $500
Final Outstanding Balance: $5,500
Payment Status: Overdue
```

The first reminder displays the original `$5,000` balance. After the penalty is applied, the next reminder displays the updated `$5,500` balance.

## Running the Project in Visual Studio Code

### Requirements

Before running the project, ensure that:

- Python 3 is installed.
- Visual Studio Code is installed.
- The Microsoft Python extension is installed in Visual Studio Code.

### Run the Complete Demonstration

1. Open the project folder in Visual Studio Code.
2. Open the integrated terminal.
3. Confirm that the terminal is in the project folder.
4. Run:

```bash
python main.py
```

If the computer uses `python3`, run:

```bash
python3 main.py
```

The program will display the complete policyholder, product, and payment management demonstration.

## Running Individual Class Tests

Each class file contains development tests protected by:

```python
if __name__ == "__main__":
```

This means the tests run only when the file is executed directly. The tests do not run when the classes are imported into `main.py`.

### Test the Policyholder Class

```bash
python policyholder.py
```

### Test the Product Class

```bash
python product.py
```

### Test the Payment Class

```bash
python payment.py
```

## Expected Main Program Results

The final run should confirm that:

- Health Insurance is created with an active status.
- John Mensah and Sarah Adeyemi are active policyholders.
- Both policyholders receive Health Insurance.
- `PAY001` and `PAY002` are processed successfully.
- Both completed payments are recorded in the correct accounts.
- Both policyholder account details are displayed.
- Sarah Adeyemi is suspended and reactivated successfully.
- Motor Insurance is updated, suspended, reactivated, and removed.
- `PAY003` receives reminders and a `$500` penalty.
- The final status of `PAY003` is `Overdue`.

## Error and Validation Handling

The project handles several invalid operations without stopping unexpectedly:

- Zero or negative product premiums
- Duplicate product assignments
- Repeated policyholder suspension or reactivation
- Zero or negative payment amounts
- Payments from suspended policyholders
- Payments for suspended or removed products
- Duplicate completed payment records
- Incomplete payments added to policyholder accounts
- Payments added to the wrong policyholder account
- Zero or negative penalties
- Penalties applied to fully paid transactions
- Additional payments attempted after a transaction is fully paid

## Testing Checklist

Before submission, confirm that:

- [ ] `policyholder.py` runs successfully.
- [ ] `product.py` runs successfully.
- [ ] `payment.py` runs successfully.
- [ ] `main.py` runs from beginning to end without a traceback.
- [ ] Both policyholders display one active product.
- [ ] Both policyholders display one completed payment.
- [ ] `PAY001` displays `Paid`.
- [ ] `PAY002` displays `Paid`.
- [ ] `PAY003` displays `Overdue` after the penalty.
- [ ] Product-management actions display correctly.
- [ ] Policyholder suspension and reactivation display correctly.
- [ ] No class-file test code runs when imported into `main.py`.

## Possible Future Improvements

Future versions could include:

- Automatic payment dates and due dates
- Customer addresses and telephone numbers
- Multiple product premiums or payment schedules
- Payment history reports
- Policy renewal dates
- Refund and overpayment handling
- File or database storage
- A graphical user interface
- User authentication and access controls
- Automated email or SMS payment reminders

## Author

Oluremi Moses Akindeko

## Purpose
Developed as a Master of Science in Data Analytics milestone assignment using Python programming concepts from Modules 1 through 3.

## License

This project is intended for educational and portfolio purposes.
