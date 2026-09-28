
# ==========================================================
# GROUP MEMBERS
# ==========================================================

# Kibirige Samuel Lutwama M25B38/034
# NAMANDA HILDA MATILDA S25B38/018
# ATTI CINDY LYNNETTE S25B38/001
# Lisa Kushaba S25B38/044
# Kabunga Akram Joshua M25B38/004
# Kyanjo Matthew Kiwumulo M25B38/011


from datetime import date


# ==========================================================
# 1. ACCOUNT CLASS
# ==========================================================

class Account:

    # Constructor: sets up a new Account object.
    def __init__(self, acc_no, pin, name, opening_balance=0):
        self.acc_no = acc_no
        self.name = name
        self._pin = pin
        self.balance = opening_balance

        # Each account has its own transaction history.
        self.transactions = []


    # ------------------------------------------------------
    # CUSTOMER LOGIN
    # ------------------------------------------------------

    def login(self, acc_no, pin):

        # Check whether the entered account number is correct.
        if acc_no != self.acc_no:
            print("We could not find this account.")
            return False

        # Check whether the entered PIN is correct.
        if pin != self._pin:
            print("Incorrect PIN.")
            return False

        print(f"Welcome {self.name}")
        return True


    # ------------------------------------------------------
    # DEPOSIT
    # ------------------------------------------------------

    def deposit(self, amount):

        # Deposits must be greater than zero.
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return False

        # Add the money to the balance.
        self.balance += amount

        # Record the successful deposit.
        self.transactions.append(
            Transaction(self.acc_no, "deposit", amount)
        )

        print(
            f"You have successfully deposited {amount} UGX."
        )
        print(f"New balance: {self.balance} UGX")

        return True


    # ------------------------------------------------------
    # WITHDRAW
    # ------------------------------------------------------

    def withdraw(self, amount):

        # A withdrawal must be positive.
        if amount <= 0:
            print("Withdrawal must be greater than zero.")
            return False

        # Do not allow the balance to become negative.
        if amount > self.balance:
            print("Insufficient balance for this withdrawal.")
            return False

        # Subtract the money from the balance.
        self.balance -= amount

        # Record the successful withdrawal.
        self.transactions.append(
            Transaction(self.acc_no, "withdrawal", amount)
        )

        print(
            f"Withdrew {amount} UGX."
        )
        print(f"New balance: {self.balance} UGX")

        return True


    # ------------------------------------------------------
    # DISPLAY ACCOUNT
    # ------------------------------------------------------

    def display(self):

        print("--------------------------------")
        print(f"Account Number: {self.acc_no}")
        print(f"Account Holder: {self.name}")
        print(f"Balance:        {self.balance} UGX")
        print("--------------------------------")


# ==========================================================
# 2. TRANSACTION CLASS
# ==========================================================

class Transaction:

    # Shared class attribute.
    # Every transaction gets a unique ID.
    _next_id = 1


    # Constructor for a Transaction object.
    def __init__(self, acc_no, tx_type, amount):

        # Give this transaction the current ID.
        self.id = Transaction._next_id

        # Increase the shared counter for the next transaction.
        Transaction._next_id += 1

        self.acc_no = acc_no
        self.type = tx_type
        self.amount = amount

        # Record the date of the transaction.
        self.date = date.today()


    # __repr__ provides a readable representation
    # of a Transaction object.
    def __repr__(self):

        return (
            f"[{self.date}] TXN{self.id}: "
            f"{self.type} of {self.amount} UGX "
            f"on account {self.acc_no}"
        )


# ==========================================================
# 3. STAFF CLASS
# ==========================================================

class Staff:

    # Constructor for a Staff object.
    def __init__(self, name, staff_id, role):

        self.name = name
        self.staff_id = staff_id
        self.role = role

        # Stores staff information after successful login.
        self.members = {}


    # ------------------------------------------------------
    # STAFF LOGIN
    # ------------------------------------------------------

    def login(self, name, staff_id, role):

        # All three details must match.
        if (
            name == self.name
            and staff_id == self.staff_id
            and role == self.role
        ):

            self.members = {
                "Name": name,
                "Staff ID": staff_id,
                "Role": role
            }

            print(f"Welcome {name}")
            return True

        print("Wrong Credentials!")
        return False


    # ------------------------------------------------------
    # STAFF INPUT
    # ------------------------------------------------------

    def prompt_login(self):

        print("\n=== Staff Login ===")

        # Ask the user for staff details.
        name = input("Enter staff name: ").strip()
        staff_id = input("Enter staff ID: ").strip()
        role = input("Enter staff role: ").strip()

        # Make sure no field is left empty.
        if not name or not staff_id or not role:
            print("All staff details are required.")
            return False

        # Send the entered information to login().
        return self.login(name, staff_id, role)


# ==========================================================
# 4. BANKING SYSTEM CLASS
# ==========================================================

class BankingSystem:

    # Constructor.
    def __init__(self):

        # Dictionary storing account objects.
        #
        # Example:
        # "ACC001" -> Account object
        self.accounts = {}


    # ------------------------------------------------------
    # ACCOUNT CREATION
    # ------------------------------------------------------

    def account_creation(
        self,
        acc_no,
        name,
        pin,
        opening_balance=0
    ):

        # Check account number format.
        #
        # Valid example: ACC001
        # Invalid examples: Aisha, 12345, ACCABC
        if (
            not acc_no.startswith("ACC")
            or not acc_no[3:].isdigit()
        ):
            print(
                "Invalid account number. "
                "Use a format such as ACC001."
            )
            return None


        # Check that the account number is unique.
        if acc_no in self.accounts:
            print("An account with this number already exists.")
            return None


        # Check that the account holder's name
        # contains letters and spaces only.
        if not name.replace(" ", "").isalpha():
            print("Name must contain letters only.")
            return None


        # Check PIN format.
        if not pin.isdigit() or len(pin) != 4:
            print("PIN must contain exactly 4 digits.")
            return None


        # Opening balance cannot be negative.
        if opening_balance < 0:
            print("Opening balance cannot be negative.")
            return None


        # Create the Account object.
        account = Account(
            acc_no,
            pin,
            name,
            opening_balance
        )


        # Store the Account object in the dictionary.
        self.accounts[acc_no] = account

        print(f"Account {acc_no} created successfully.")

        return account


    # ------------------------------------------------------
    # FIND ACCOUNT
    # ------------------------------------------------------

    def find_acc(self, acc_no):

        # Return the account if it exists.
        # Otherwise return None.
        return self.accounts.get(acc_no)


    # ------------------------------------------------------
    # DEPOSIT
    # ------------------------------------------------------

    def deposit(self, acc_no, amount):

        account = self.find_acc(acc_no)

        # Refuse the operation if the account does not exist.
        if account is None:
            print("Account does not exist.")
            return False

        # Let the Account object handle the deposit.
        return account.deposit(amount)


    # ------------------------------------------------------
    # WITHDRAW
    # ------------------------------------------------------

    def withdraw(self, acc_no, amount):

        account = self.find_acc(acc_no)

        # Refuse the operation if the account does not exist.
        if account is None:
            print("Account not found.")
            return False

        # Let the Account object handle the withdrawal.
        return account.withdraw(amount)


    # ------------------------------------------------------
    # CHECK BALANCE
    # ------------------------------------------------------

    def check_balance(self, acc_no):

        account = self.find_acc(acc_no)

        if account is None:
            print("Account not found.")
            return None

        # Return the current balance.
        return account.balance


    # ------------------------------------------------------
    # DISPLAY ACCOUNT
    # ------------------------------------------------------

    def display_account(self, acc_no):

        account = self.find_acc(acc_no)

        if account is None:
            print("Account not found.")
            return

        account.display()


# ==========================================================
# DEMO / USER INTERACTION
# ==========================================================

bank = BankingSystem()


# ----------------------------------------------------------
# CREATE ACCOUNTS USING USER INPUT
# ----------------------------------------------------------
# This prevents account details from being completely
# hard-coded into the demonstration.

print("================================")
print("       ACCOUNT CREATION")
print("================================")


def create_account_from_input():

    acc_no = input("Enter account number (e.g. ACC001): ").strip()
    name = input("Enter account holder name: ").strip()
    pin = input("Enter a 4-digit PIN: ").strip()

    balance_input = input(
        "Enter opening balance (press Enter for 0): "
    ).strip()

    # If the user does not enter a balance,
    # use 0 as the opening balance.
    if balance_input == "":
        opening_balance = 0

    else:
        # Make sure the balance contains only numbers.
        if not balance_input.isdigit():
            print("Opening balance must be a number.")
            return None

        opening_balance = float(balance_input)

    return bank.account_creation(
        acc_no,
        name,
        pin,
        opening_balance
    )


# Create three accounts.
acc1 = create_account_from_input()
acc2 = create_account_from_input()
acc3 = create_account_from_input()


# ----------------------------------------------------------
# CUSTOMER LOGIN
# ----------------------------------------------------------

print("\n================================")
print("        CUSTOMER LOGIN")
print("================================")

login_acc_no = input("Enter your account number: ").strip()
login_pin = input("Enter your PIN: ").strip()

account = bank.find_acc(login_acc_no)

if account is None:
    print("Account not found.")

else:
    account.login(login_acc_no, login_pin)


# ----------------------------------------------------------
# SUCCESSFUL OPERATIONS
# ----------------------------------------------------------

print("\n================================")
print("       BANKING OPERATIONS")
print("================================")

operation_acc = input(
    "Enter account number for a deposit: "
).strip()

deposit_input = input(
    "Enter deposit amount: "
).strip()

if deposit_input.isdigit():
    bank.deposit(
        operation_acc,
        float(deposit_input)
    )
else:
    print("Invalid deposit amount.")


operation_acc = input(
    "Enter account number for a withdrawal: "
).strip()

withdraw_input = input(
    "Enter withdrawal amount: "
).strip()

if withdraw_input.isdigit():
    bank.withdraw(
        operation_acc,
        float(withdraw_input)
    )
else:
    print("Invalid withdrawal amount.")


# ----------------------------------------------------------
# INVALID OPERATIONS DEMONSTRATION
# ----------------------------------------------------------

print("\n================================")
print("       INVALID OPERATIONS")
print("================================")

# Negative deposit.
bank.deposit("ACC001", -5000)

# Withdrawal greater than available balance.
bank.withdraw("ACC002", 100000)

# Non-existent account.
bank.deposit("ACC999", 1000)


# ----------------------------------------------------------
# STAFF LOGIN
# ----------------------------------------------------------

print("\n================================")
print("          STAFF LOGIN")
print("================================")

# Registered staff details are stored in the system.
# The actual login attempt comes from user input.
teller = Staff(
    "Hilda Namanda",
    "S25B38/011",
    "Teller"
)

teller.prompt_login()


# ----------------------------------------------------------
# BALANCE LOOKUP
# ----------------------------------------------------------

print("\n================================")
print("        BALANCE LOOKUP")
print("================================")

lookup_acc = input(
    "Enter account number to check balance: "
).strip()

balance = bank.check_balance(lookup_acc)

if balance is not None:
    print(f"Current balance: {balance} UGX")


# ----------------------------------------------------------
# FINAL ACCOUNT STATES
# ----------------------------------------------------------

print("\n================================")
print("       FINAL ACCOUNT STATES")
print("================================")

for account_number, account in bank.accounts.items():
    account.display()


# ----------------------------------------------------------
# TRANSACTION HISTORY
# ----------------------------------------------------------

print("\n================================")
print("       TRANSACTION HISTORY")
print("================================")

history_acc = input(
    "Enter account number to view transaction history: "
).strip()

account = bank.find_acc(history_acc)

if account is None:
    print("Account not found.")

elif len(account.transactions) == 0:
    print("No transactions found for this account.")

else:
    for tx in account.transactions:
        print(tx)
