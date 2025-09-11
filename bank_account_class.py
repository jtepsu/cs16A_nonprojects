class Database:
    def __init__(self):
        self.database = {}

    def create_account(self, num, type, name, init_balance=0):
        index = self.search_account_db(num)
        if index == -1:
            account = Account(num, type, name, init_balance)
            self.database[num] = account
        else:
            print("Account", num, "already exists")
    
    def delete_account(self, num):
        index = self.search_account_db(num)
        if index != -1:
            print("Deleting account:", self.database[num].num)
            del self.database[num]
        else:
            print(num, "invalid account number; nothing to be deleted.")

    def search_account_db(self, num):
        if num in self.database:
                return num
        return -1
    
    def deposit(self, account_num, amount):
        index = self.search_account_db(account_num)
        if index != -1:
            print("Depositing", amount, "to", self.database[account_num].num)
            self.database[account_num].balance += amount
        else:
            print(account_num, "invalid account number; no deposit action performed.")

    def withdraw(self, account_num, amount):
        index = self.search_account_db(account_num)
        if index != -1:
            if self.database[account_num].balance >= amount:
                print("Withdrawing", amount, "from", self.database[account_num].num)
                self.database[account_num].balance -= amount
            else:
                print("withdrawal amount", amount, "exceeds the balance of", self.database[account_num].balance, "for", account_num, "account.")
        else:
            print(account_num, "invalid account number; no withdrawal action performed.")

    def show_account(self, account_num):
        index = self.search_account_db(account_num)
        if index != -1:
            print("Showing details for", self.database[account_num].num)
            self.database[account_num].show()
        else:
            print(account_num, "invalid account number; nothing to be shown for.")
    
    def print_database(self):
        for i in self.database.values():
            i.show()
            print()

class Account:
    def __init__(self, num, type, name, init_balance):
        self.num = num
        self.type = type
        self.name = name
        self.balance = init_balance
    
    def show(self):
        print(f"Account number: {self.num}")
        print(f"Type: {self.type}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")

account_database = Database()
account_database.create_account("0000", "saving", "David Patterson", 1000)
account_database.create_account("0001", "checking", "John Hennessy", 2000)
account_database.create_account("0003", "saving", "Mark Hill", 3000)
account_database.create_account("0004", "saving", "David Wood", 4000)
account_database.print_database()
account_database.show_account('0003')
account_database.deposit('0003', 50)
account_database.show_account('0003')
account_database.withdraw('0003', 25)
account_database.show_account('0003')
account_database.delete_account('0003')
account_database.show_account('0003')
account_database.deposit('0003', 50)
account_database.withdraw('0001', 6000)