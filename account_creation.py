from checking_account import CheckingAccount
from saving_account import SavingAccount
from datetime import datetime, date
import json
import csv


customer_list = []
saving_account_info = []


def new_customer() -> None:
    name = input("Please enter the your name:\n")
    surname = input("Please enter the your surname:\n")
    account_num = input("Please enter the your account number:\n") # We can create a random account number using random package
    age = input("Please enter your age:\n")
    balance = 0
    #password variable will also be needed for the client to login later using the password.

    user = CheckingAccount(name, surname, account_num, age, balance)
    
    customer_list.append(user.to_dict())

    with open("customers.csv", 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['f_name', 'l_name', 'account_number', 'age', 'balance'])
        #writer.writeheader()  # Write the header row, This is only need when we input the first customer,
        writer.writerows(customer_list)  # Write the data rows


def create_saving(interest_rate: int, account_number: str) -> None:
    note_day = 15
    note_month = 5
    today = date.today()
    note_year = today.year
    note_date = date(note_year, note_month, note_day)
    #creation_date = date.today()
    saving_account = SavingAccount(interest_rate, note_date, account_number)
    saving_account_info.append(saving_account.to_dict())

    with open("savings_accounts.csv", 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['account_number', 'interest_rate', 'balance', 'interest_earned'])
        #writer.writeheader()  # Write the header row
        writer.writerows(saving_account_info)  # Write the data rows

    

    

# if __name__ == '__main__':
#     new_customer()

    