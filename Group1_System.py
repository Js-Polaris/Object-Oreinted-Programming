#Kibirige Samuel Lutwama M25B38/034
#NAMANDA HILDA MATILDA S25B38/018
#ATTI CINDY LYNNETTE S25B38/001
#Lisa Kushaba S25B38/044
##Kabunga Akram JOshua M25B38/004
#Kyanjo Matthew Kiwumulo M25B38/011

from datetime import date
import random

##The fixed error handling for the various nticipated errors
class BankingError(Exception):
    """Base class for every error this banking system can raise."""

class AccountNotFoundError(BankingError):
    pass
  class DuplicateAccountError(BankingError):
    pass 
 class InvalidPinError(BankingError):
    pass 
 class InvalidAmountError(BankingError):
    pass 
 class InsufficientFundsError(BankingError):
    pass
class DuplicateStaffError(BankingError):
    pass
class StaffNotFoundError(BankingError):
    pass    
    
  #Actual clases done
class Account:
    def __init__(self,acc_no, pin,Name,opening_balance = 0):
        self.acc_no = Acc_No ##This will act as the unique identifier
        self.name = name
        self._pin = pin
        self.balance = opening_balance##starts with 0 amount in the account
        self.transactions = []##Where all the transactions for the account or person are stored.
        
def authenticate(self,pin):
        if pin != self._pin:
            raise InvalidPinError(f"No account matches {self.acc_no}")
    def login(self,acc_no,pin):
        if acc_no !=self.acc_no:
            raise AccountNotFoundError(f"No acount matches {acc_no}")
        self.authenticate(pin)
        print(f"Welcome {self.name}")
        return True        
    
    def deposit(self,amount):
        if amount<=0:
            raise InvalidAmountError(f"You annot deposit an amount less than 0")
        self.balance += amount
        self.transactions.append(Transaction(self.acc_no, "deposit",amount))
        print(f"You have successfully deposited {amount}UGX balance; {self.balance}UGX")
        return True   #CONTINUATION TO CLASS ACCOUNT

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(f"Withdrawal must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient Account. You tried to get {amount},"
                                         f" Your balance is {self.balance} UGX")
        self.balance -= amount
        self.transactions.append(Transaction(self.acc_no, "withdrawal", amount))
        print(f"Withdrew {amount} UGX. New balance: {self.balance} UGX")
        return True

    def display(self):
        print("------")
        print(f"Account Number: {self.acc_no}")
        print(f"Account Holder: {self.name}")
        print(f"Balance:        {self.balance} UGX")
        print("------")


class Transaction:
    #A single deposit or withdrawal, kept for the account's history.
    _next_id = 1

    def __init__(self, acc_no, tx_type, amount):
        self.id = Transaction._next_id
        Transaction._next_id += 1
        self.acc_no = acc_no
        self.type = tx_type
        self.amount = amount
        self.date = date.today()

    def __repr__(self):
        return (f"[{self.date}] TXN{self.id}: {self.type} of {self.amount} UGX on account {self.acc_no}")
class Staff:
    def __init__(self, Name, Role, staff_id):
        self.Name = Name
        self.Role = Role
        self.Staff_id = staff_id
        self.Members = {}## dictionary for staff members
    def login(self, name, role,staff_id):
        ##to check what credentials are being used
        if name == self.Name and role == self.Role and staff_id == self.staff_id:
            self.Members ={"Name": name, "Role": role, "ID": staff_id}
            print(f"Welcome {name}")
        raise InvalidPinError("Wrong PIN Papi!")
    def prompt_login(self):
        Login_staff = input("Please enter your credentials in the order \n1.Name\n2.Role\n3.ID")
        parts = [item.strip() for item in Login_staff.split(",")]#use the comma to show separation of the diffent credentials
        if len(parts) != 3:
            print("Please enter exactly three values separated by commas.")
            return False
        return self.login(*parts) 

class Banking_system: ##The heart of the whole system. It handles everything from account creation to lookup
    class Banking_system: ##The heart of the whole system. It handles everything from account creation to lookup
    def __init__(self):
        self.accounts ={}
    def account_creation(self, acc_no, pin, name, opening_balance=0):
        if acc_no in self.accounts:
            raise DuplicateAccountError(f"Account {acc_no} already exists.")
        account = Account(acc_no, pin, name, opening_balance)
        self.accounts[acc_no] = account
        return account

    def interactive_account_creation(self, opening_balance=0):
        name = input("Please enter your name here: ").strip()
        while len(name)==0:
            name = input("Name cannot be empty or with numbers. Re enter the name: ")
        def Pin_setup():
            try:
                pin = int(input("Please enter a PIN(minimum 5digits): "))
                re_entry = int(input("Please re-enter the pin: "))
            except ValueError:
                print("Enter a digit for the pin")    
                return Pin_setup()
            if len(str(pin))<5:
                print("PIN must be at least 5 digits")
                return Pin_setup()
            if pin !=re_entry:
                print("The pins do not match")
                return pin 
        pin = Pin_setup()
                        
        acc_no = f"DSC:{random.randint(10000, 99999)}"
        while acc_no in self.accounts:
            acc_no = f"DSC:{random.randint(10000, 99999)}"
        account = Account(acc_no, pin, name, opening_balance)
        self.accounts[acc_no] = account
        print(f"Welcome {name}, your account has been created with account number {acc_no}.")
        return account           

    def register_staff(self, name, role, staff_id):
        if staff_id in self.staff:
            raise DuplicateStaffError(f"This member already works for us")
        staff = Staff(name, role, staff_id)
        self.staff[staff_id] = staff
        return staff

    def interactive_staff_registration(self):
        name = input("Pleas put your name in here: ")
        while len(name)== 0:
            name = input("The name cannot be empty. Enter it again: ")
        role = input("Staff role (e.g. Teller, Manager): ").strip()
        while len(role) == 0:
            role = input("Role cannot be empty. Staff role: ")
        staff_id = input("Staff ID: ").strip()
        while len(staff_id) == 0 or staff_id in self.staff:
            if staff_id in self.staff:
                print(f"Staff ID {staff_id} is already taken.")
            staff_id = input("Please enter a unique staff ID: ")

            staff = self.register_staff(name, role, staff_id)
            print(f"Staff member {name} registered with ID {staff_id}.")
            return staff

    def find_staff(self, staff_id):
            staff = self.staff.get(staff_id)
            if staff is None:
                raise StaffNotFoundError(f"No staff with ID {staff_id}")
            return staff

    def find_acc(self,acc_no):
        return self.accounts.get(acc_no)
    
    def deposit(self,acc_no, amount):
        account = self.find_acc(acc_no)
        if account is None:
            print("Acount doesn't exist")    
            return False
        return account.deposit(amount)
    
    def withdraw(self, acc_no, amount):
        account = self.find_acc(acc_no)
        if account is None:
            print("Account not found.")
            return False
        return account.withdraw(amount)

    def check_balance(self, acc_no):
        ##Staff use this to look up the balance on any account.
        account = self.find_acc(acc_no)
        if account is None:
            print("Account not found.")
            return None
        return account.balance

    def display_account(self, acc_no):
        ##Staff use this to show a clear summary of an account.
        account = self.find_acc(acc_no)
        if account is None:    
            print("Account not found.")
            return
        account.display()

def customer_menu(bank):
    acc_no = input("Enter your account number: ").strip()
    pin = input("Enter your PIN: ").strip()

    try:
        account = bank.find_acc(acc_no)
        account.login(acc_no, pin)
    except BankingError as e:
        print(f"Login failed: {e}")
        return

    while True:
        print("--- Customer Menu ---
1. Deposit
2. Withdraw
3. Check balance
4. View transaction history
5. Log out
")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                amount = float(input("Amount to deposit: "))
                bank.deposit(acc_no, pin, amount)
            except ValueError:
                print("Please enter a valid number.")
            except BankingError as e:
                print(f"Deposit failed: {e}")

        elif choice == "2":
            try:
                amount = float(input("Amount to withdraw: "))
                bank.withdraw(acc_no, pin, amount)
            except ValueError:
                print("Please enter a valid number.")
            except BankingError as e:
                print(f"Withdrawal failed: {e}")

        elif choice == "3":
            print(f"Balance: {account.balance} UGX")

        elif choice == "4":
            if not account.transactions:
                print("No transactions yet.")
            for tx in account.transactions:
                print(tx)

        elif choice == "5":
            print("Logged out.")
            return

        else:
            print("Invalid option, try again.")


def staff_login_flow(bank):
    
    staff_id = input("Staff ID: ").strip()
    try:
        staff = bank.find_staff(staff_id)
    except StaffNotFoundError as e:
        print(e)
        return None
    name = input("Name: ").strip()
    role = input("Role: ").strip()
    try:
        staff.login(name, role, staff_id)
    except BankingError as e:
        print(f"Login failed: {e}")
        return None
    return staff

def staff_menu(bank):
    staff = staff_login_flow(bank)
    if staff is None:
        return

    while True:
        print("
--- Staff Menu ---
1. Check account balance
2. Display account details
3. Log out
")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            acc_no = input("Account number: ").strip()
            try:
                print(f"Balance: {bank.check_balance(acc_no)} UGX")
            except BankingError as e:
                print(e)
        elif choice == "2":
            acc_no = input("Account number: ").strip()
            try:
                bank.display_account(acc_no)
            except BankingError as e:
                print(e)
        elif choice == "3":
            print("Logged out.")
            return
        else:
            print("Invalid option, try again.")

def main_menu():
    bank = Banking_system() 

    while True:
        print("
==== Campus Credit System ====
1. Create customer account
2. Register staff member
3. Login as staff
4. Login as customer
5. Exit
")
        choice = input("Enter desired action here: ").strip()
        if choice == "1":
            try:
                bank.interactive_account_creation()
            except BankingError as e:
                print(f"Could not create account: {e}")
        elif choice == "2":
            try:
                bank.interactive_staff_registration()
            except BankingError as e:
                print(f"Could not register staff: {e}")
        elif choice == "3":
            staff_menu(bank)
        elif choice == "4":
            customer_menu(bank)
        elif choice == "5":
            print("Thank you for banking with Campus Credit. Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number from 1 to 5.")
if __name__ == "__main__":
    main_menu()


