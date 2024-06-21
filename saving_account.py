from datetime import datetime, date
import csv
import tempfile
import os
class SavingAccount:
    def __init__(self, interest_rate, creation_date, account_number) -> None: #Can map the saving account with the checking account using a dict
        self.interest_rate = interest_rate
        self.account_number = account_number
        self.balance = 0
        self.my_interest = 0
        self.account_creation_date = creation_date #date.today()  

    @staticmethod
    def credit_money(account, amount):
        # self.balance += self.amount
        # return f"${self.amount} has been added to your saving account and the interest rate of {self.interest_rate}"
        with tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False) as temp_file, \
         open("savings_accounts.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
            writer = csv.DictWriter(temp_file, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                if row['account_number'] == account:
                    row['balance'] = str(float(row['balance']) + amount)
                writer.writerow(row)

        # Replace the original file with the updated temporary file    
        os.replace(temp_file.name, 'savings_accounts.csv')
        return f"${amount} has been credited to your account"
    

    @staticmethod
    def debit_money(account, amount):
                    
        with tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False) as temp_file, \
         open("savings_accounts.csv", 'r', newline='') as file:
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
        os.replace(temp_file.name, 'savings_accounts.csv')
        return f"${amount} has been debited from your account"
    
    @staticmethod
    def interest_amount(): # Interest will be 5% of the total balance of the account divided by 12 because of 12 months as 5% interest is over a period of one year

        with tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False) as temp_file,\
         open('savings_accounts.csv', 'r') as f:
            data = csv.DictReader(f)
            writer = csv.DictWriter(temp_file, fieldnames=data.fieldnames)
            writer.writeheader()
            for info in data:
                amount = float(info['interest_rate']) * 0.01
                info['interest_earned'] = str(float(info['balance']) * amount) #str(float(info['balance']) * (float(info['interest_rate']) * 0.01))
                print(info['interest_earned'])
                info['interest_earned'] = float(info['interest_earned'])/12/365
                print("Interest earned",info['interest_earned'])
                writer.writerow(info)
        os.replace(temp_file.name, 'savings_accounts.csv')


    @staticmethod
    def total_balance(account):
        with open('savings_accounts.csv', 'r') as f:
            data = csv.DictReader(f)
            for client in data:
                if client['account_number'] == account:            
                    return client['balance']

    @staticmethod   
    def interest_earned():
        #This gets added to the balance on the 2nd of every month
        with tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False) as temp_file, \
             open("savings_accounts.csv", 'r', newline='') as f:
                data = csv.DictReader(f)
                writer = csv.DictWriter(temp_file, fieldnames=data.fieldnames)
                writer.writeheader()
                for info in data:
                    info['balance'] = str(float(info['interest_earned'])+ float(info['balance'])) # Using abs() to make the value of self.interest as positive always
                    print("Balance", info['balance'], "Interest earned", info['interest_earned'])
                    writer.writerow(info)
            # Replace the original file with the updated temporary file    
        os.replace(temp_file.name, 'savings_accounts.csv')
        #The interest earned should go back to 0 after the previous interest is added to the balance
        

    def to_dict(self):
        return {
            "account_number":  self.account_number,
            "interest_rate": self.interest_rate,
            "balance": self.balance,
            "interest_earned": self.my_interest,

        }
    
    
    