import csv
from checking_account import CheckingAccount
import pandas as pd
from saving_account import SavingAccount
from datetime import datetime, date

# with open('customers.csv', "r") as f:
#     data = f.readlines()
#     for info in data:
#         print(info)
with open('savings_accounts.csv', 'r') as f:
            data = csv.DictReader(f)
            for client in data:
                if client['account_number'] == '11111':
                    date1 = client['account_creation']

def interest(balance, interest):
    interest = int(balance) * (interest * 0.01)
    print(interest)
    interest = (interest/12)/365 # Because of the time_difference.days, the self.interest value comes out to be in minus
    return interest

savings_total = SavingAccount.interest_amount()
savings_interest =  SavingAccount.interest_earned()






