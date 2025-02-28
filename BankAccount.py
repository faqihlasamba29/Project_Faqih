class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.__account_number = account_number
        self.__balance = balance
        self.date_of_opening = date_of_opening
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Saldo anda tidak cukup")
    
    def check_balance(self):
        print(f"Sisa Saldo adalah: {self.__balance}")
    

nasabah = BankAccount('1790000037874', 5000000, '17 February 2025', 'Faqih Lasamba')
print(nasabah.check_balance())
