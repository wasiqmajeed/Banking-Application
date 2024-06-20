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


    def add_money(self):
        self.balance += self.amount
        return f"${self.amount} has been added to your saving account and the interest rate of {self.interest_rate}"
    
    @staticmethod
    def interest_amount(): # Interest will be 5% of the total balance of the account divided by 12 because of 12 months as 5% interest is over a period of one year

        #I think its best to take the balance of the account everyday and calculate the balance according to that. Need to change the code accordingly

        # time_difference = self.account_creation_date - date.today() # The difference in days between the day of creation of the account vs todays date
        # print(f"{time_difference}, '=', {self.account_creation_date} '-' {date.today()}")
        # if time_difference.days < 30: #This calculates daily interest
        #     self.interest = int(self.balance) * (self.interest * 0.01)
        #     self.interest = (self.interest/12)/365 * time_difference.days # Because of the time_difference.days, the self.interest value comes out to be in minus
        #     return abs(self.interest)
        # else: #This calculates the intrest for whole month at one time.
        #     self.interest = int(self.balance) * (self.interest * 0.01) #Have to work on how the interest is calculated and then added to the csv file
        #     return self.interest/12
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
        #interest = int(balance) * (self.interest_rate * 0.01)
  
        #interest = (interest/12)/365 # Because of the time_difference.days, the self.interest value comes out to be in minus
        #return interest
        

    @staticmethod
    def total_balance(account):
        with open('savings_accounts.csv', 'r') as f:
            data = csv.DictReader(f)
            for client in data:
                if client['account_number'] == account:            
                    return client['balance']

    @staticmethod   
    def interest_earned():
        # if date.today().day == 2:
        #     with tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False) as temp_file, \
        #      open("savings_accounts.csv", 'r', newline='') as f:
        #         data = csv.DictReader(f)
        #         writer = csv.DictWriter(temp_file, fieldnames=data.fieldnames)
        #         writer.writeheader()
        #         for info in data:
        #             info['balance'] += info['interest_earned'] # Using abs() to make the value of self.interest as positive always
        #             writer.writerow(info)
        #     # Replace the original file with the updated temporary file    
        #     os.replace(temp_file.name, 'savings_accounts.csv')
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
        

    def to_dict(self):
        return {
            "account_number":  self.account_number,
            "interest_rate": self.interest_rate,
            "balance": self.balance,
            "interest_earned": self.my_interest,

        }
    
    
    