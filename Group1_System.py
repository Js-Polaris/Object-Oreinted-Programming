#Kibirige Samuel Lutwama M25B38/034
#NAMANDA HILDA MATILDA S25B38/018
#ATTI CINDY LYNNETTE S25B38/001
#Lisa Kushaba S25B38/044
from datetime import date

class Account:
    def __init__(self,Acc_No, pin,Name,opening_balance = 0):
        self.Acc_No = Acc_No ##This will act as the unique identifier
        self.Name = Name
        self._pin = pin
        self. Balance = opening_balance##starts with 0 amount in the account
        self.transactions = []##Where all the transactions for the account or person are stored.
    def login(self,account_number,pin):
        if account_number !=self.Acc_No:
            print("We could not find this account")
            return False
        if pin != self._pin:
            print("Incorrect Pin")
            return False
        print(f"Welcome {self.Name}")
        return True   
     def deposit(self,amount
        if amount<=0:
            print("This is cannot be a starting deposit number.")
            return False
        self.Balance =+ amount
        self.transactions.append(transactions(self.Acc_No, "deposit",amount))
        print(f"You have successfully deposited {amount}UGX balance; {self.Balance}UGX")
        return True   #CONTINUATION TO CLASS ACCOUNT


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
        return f"[{self.date}] TXN{self.id}: {self.type} of {self.amount} UGX on account {self.acc_no}"
class Staff:
    def __init__(self, Name, Role, Staff_ID):
        self.Name = Name
        self.Role = Role
        self.Staff_id = Staff_ID
        self.Members = {}## dictionary for staff members
    def login(self):
        Login_staff = input("Please enter your credentials in the order \n1.Name\n2.Role\n3.ID")
        name, role,Staff_id =[item.strip() for item in Login_staff.split(",")]##use the comma to show separation of the diffent credentials
        if name == self.Name and role == self.Role and Staff_id == self.Staff_id:
            self.Members ={"Name": name, "Role": role, "ID": Staff_id}
            print(f"Welcome {name}")
        else:
            print("Wrong Credentials!!")
            return False

class Banking_system: ##The heart of the whole system. It handles everything from account creation to lookup
    def __init__(self):
        self.accounts =[]
    def account_creation(self, account_number,name, opening_balance=0):
        account = Account(account_number,name,opening_balance)
        self.accounts.append(account)
        return account
    def find_acc(self,account_number):
        for account in self.accounts:
            if account.Acc_No == account_number:
                return account
        return None
    def deposit(self,account_number, amount):
        account = self.find_acc(account_number)
        if account is None:
            print("Acount doesn't exist")    
            return False
        return account.deposit(amount)
    def withdraw(self, acc_no, amount):
        account = self.find_account(acc_no)
        if account is None:
            print("Account not found.")
            return False
        return account.withdraw(amount)

    def check_balance(self, acc_no):
        """Staff use this to look up the balance on any account."""
        account = self.find_account(acc_no)
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

