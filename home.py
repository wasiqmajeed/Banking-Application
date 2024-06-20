from account_creation import create_saving, new_customer
from checking_account import CheckingAccount
import csv

print("Welcome to Personal Bank!")

def find_user(account_num):
    with open('customers.csv', "r") as file:
        data = csv.DictReader(file)
        for info in data:
            if info["account_number"] == account_num:
                return True



customer_info = int(input("If you are an existing customer please press 1, if you would like to create a new account please press 2\n"))

if customer_info == 1:
    user_account = input("Please enter your account number!\n")
    #user_password = input("Please enter your account password!")

    if find_user(user_account): # Need to later change it to if user_account in users and user_password == passwords, currently just checking with users
        
        user_choice = int(input("Press 1 to check your balance, Press 2 to withdraw money, Press 3 to deposit money or Press 4 to change password.\n"))
        current_or_saving = int(input('Please press 1 for Checking account, Press 2 for Saving account.\n'))

        if user_choice == 1:

            #User can check balance in current and saving account
            if current_or_saving == 1:
                account_balance = CheckingAccount.total_balance(user_account)
                print(account_balance)
            else:
                pass #Savings account         

        elif user_choice == 2:

            #  User can withdraw money from current or saving account
            debit_amount = int(input("Please enter the amount that your would like to withdraw!\n"))

            if current_or_saving  == 1:
                debit_amount = CheckingAccount.debit_money(user_account, debit_amount)
            else:
                pass # Savings acccount

        elif user_choice == 3:

            # User can deposit money to current or saving account
            amount = int(input("Please enter the amount that your would like to deposit!\n"))
            if current_or_saving == 1:
                account = CheckingAccount.credit_money(user_account, amount)  
            else:
                pass      #Saving account  

        else:
            pass # Change password  

    else:
        print("No Matching account found!")  

elif customer_info == 2:
    account_type =  int(input('Would you like to create a 1. Checking account or 2.Savings account\n'))
    if account_type == 1:
        new_customer()
    elif account_type == 2:
        # Create a Savings account
        account_number = input("Please enter your account number\n") # Before creating a savings account, we need to check if they a checkings accounts and only then we can create a savings account
        with open('customers.csv', "r") as file:
            data = csv.DictReader(file)
            for info in data:
                if info['account_number'] ==  account_number:
                    create_saving(5, account_number) #Currently the savings account number and checkings account number is same, later I should update it to be different
                    break
            else:    
                print("To Create a Savings account, you need to first create a Checking account!")
                    

       
    else:
        print("Input not recognized, please try again.")

else:
    print("Unknown button pressed!")