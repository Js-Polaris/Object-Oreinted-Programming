#Kibirige Samuel Lutwama M25B38/034
#NAMANDA HILDA MATILDA S25B38/018
#ATTI CINDY LYNNETTE S25B38/001
#Lisa Kushaba S25B38/044
##Kabunga Akram JOshua M25B38/004
#Kyanjo Matthew Kiwumulo M25B38/011

from datetime import date
class Account:
    def __init__(self,acc_no, pin,Name,opening_balance = 0):
        self.acc_no = Acc_No ##This will act as the unique identifier
        self.name = name
        self._pin = pin
        self.balance = opening_balance##starts with 0 amount in the account
        self.transactions = []##Where all the transactions for the account or person are stored.
        
    def login(self,acc_no,pin):
        if acc_no !=self.acc_no:
            print("We could not find this account")
            return False
        if pin != self._pin:
            print("Incorrect Pin")
            return False
        print(f"Welcome {self.Name}")
        return True   
        
    def deposit(self,amount):
        if amount<=0:
            print("This is cannot be a starting deposit number.")
            return False
        self.balance += amount
        self.transactions.append(Transaction(self.acc_no, "deposit",amount))
        print(f"You have successfully deposited {amount}UGX balance; {self.Balance}UGX")
        return True   #CONTINUATION TO CLASS ACCOUNT

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be a positive amount.")
            return False
        if amount > self.balance:
            print("Insufficient balance for this withdrawal.")
            return False
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
    def login(self, name, staff_id,role):
        if name == self.Name and role == self.Role and staff_id == self.Staff_id:
            self.Members ={"Name": name, "Role": role, "ID": staff_id}
            print(f"Welcome {name}")
        else:
            print("Wrong Credentials!!")
            return False
    def prompt_login(self):
        Login_staff = input("Please enter your credentials in the order \n1.Name\n2.Role\n3.ID")
        parts = [item.strip() for item in Login_staff.split(",")]#use the comma to show separation of the diffent credentials
        if len(parts) != 3:
            print("Please enter exactly three values separated by commas.")
            return False
        return self.login(*parts) 

class Banking_system: ##The heart of the whole system. It handles everything from account creation to lookup
    def __init__(self):
        self.accounts ={}
    def account_creation(self, account_number,name, opening_balance=0):
        account = Account(acc_no,name,opening_balance)
        if acc_no is self.accounts:
            print("An account of this number exists.")
            return None
        self.accounts.[acc_no] = account ##adding the new accounts to the list
        return account
        
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
        """Staff use this to look up the balance on any account."""
        account = self.find_acc(acc_no)
        if account is None:
            print("Account not found.")
            return None
        return account.balance

    def display_account(self, acc_no):
        """Staff use this to show a clear summary of an account."""
        account = self.find_account(acc_no)
        if account is None:    
            print("Account not found.")
            return
        account.display()

# ---- Demo ----

bank = BankingSystem()

#Account creation
acc1 = bank.account_creation("ACC001", "Aisha Namutebi", 50000)
acc2 = bank.account_creation("ACC002", "Brian Okello")
acc3 = bank.account_creation("ACC003","Mulo Innocent",350000)

print("=== Customer login ===")
acc1.login("ACC001", "0000")# wrong PIN
acc1.login("ACC001", "1234")#correct

print("=== Successful deposits and withdrawals ===")
bank.deposit("ACC001", 20000)
bank.withdraw("ACC001", 10000)
bank.deposit("ACC002", 30000)
bank.deposit("ACC003",300000)
bank.withdraw("ACC003",649000)

print("\n=== Invalid operations (must be refused) ===")
bank.deposit("ACC001", -5000)     # negative deposit
bank.withdraw("ACC002", 100000)#withdrawal bigger than balance
bank.deposit("ACC999", 1000)#account does not exist

print("\n=== Staff: balance lookup ===")
teller = Staff("Hilda Namanda", "Teller", "S25B38/011")
teller.login("Hilda Namanda", "Teller", "S25B38/011")
print(f"Balance on ACC001: {bank.check_balance('ACC001')} UGX")
print(f"Balance on ACC003: {bank.check_balance('ACC003')} UGX")

print("\n=== Final state of each account ===")
bank.display_account("ACC001")
bank.display_account("ACC002")
bank.display_account("ACC003")

print("\n=== Transaction history for ACC001 ===")
for tx in acc1.transactions:
    print(tx)
