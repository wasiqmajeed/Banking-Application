import csv
import tempfile
import os
class CheckingAccount:
    def __init__(self, f_name, l_name, account_number, age, balance, credit_amount=0, debit_amount=0) -> None:
        self.f_name =  f_name
        self.l_name = l_name
        self.account_number = account_number
        self.age = age
        self.credit_amount = credit_amount
        self.debit_account = debit_amount
        self.balance = balance

    @staticmethod
    def credit_money(account, amount):
        with tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False) as temp_file, \
         open("customers.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
            writer = csv.DictWriter(temp_file, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                if row['account_number'] == account:
                    row['balance'] = str(float(row['balance']) + amount)
                writer.writerow(row)

        # Replace the original file with the updated temporary file    
        os.replace(temp_file.name, 'customers.csv')
        return f"${amount} has been credited to your account"
    
    
    @staticmethod
    def debit_money(account, amount):
        # with open('customers.csv', 'r') as f:
        #     data = csv.DictReader(f)
        #     for client in data:
        #         if client['account_number'] == account:
        #             if amount > client["balance"]:
        #                 print("Insufficient funds. Operation canclled!")
        #             else:
        #                 client["balance"] -= amount
        #                 return f"${amount} has been debited from your account"
                    
        with tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False) as temp_file, \
         open("customers.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
            writer = csv.DictWriter(temp_file, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                if row['account_number'] == account:
                    if amount > float(row["balance"]):
                            print("Insufficient funds. Operation canclled!")
                    else:
                        row['balance'] = str(float(row['balance']) - amount)
                writer.writerow(row)

        # Replace the original file with the updated temporary file    
        os.replace(temp_file.name, 'customers.csv')
        return f"${amount} has been debited from your account"

    @staticmethod
    def total_balance(account):
        with open('customers.csv', 'r') as f:
            data = csv.DictReader(f)
            for client in data:
                if client['account_number'] == account:
                    return client['balance']

    
    def to_dict(self):
        return {
            "f_name": self.f_name,
            "l_name": self.l_name,
            "account_number":  self.account_number,
            "age": self.age,
            "balance": self.balance,

        }
    



