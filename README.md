# Customer Banking module 3 challenge
Savings and CD Account Interest Calculator

# Overview

This program calculates and displays the interest earned and the updated balance for a savings account and a certificate of deposit (CD) account over a specified period. Users are prompted to input the account balance, interest rate, and the months to maturity for both accounts. The program uses two imported functions, create_savings_account, and create_cd_account, to calculate interest and update the balances accordingly.

# Program Flow

1.	Savings Account Input:
- The user is prompted to input:
- The initial balance of the savings account.
- The interest rate (in percentage).
- The number of months the savings account will accrue interest.
- The program calculates the interest earned and the updated balance for the given period.


2.	CD Account Input:
- The user is prompted to input:
- The initial balance of the CD account.
- The interest rate (in percentage).
- The number of months until maturity for the CD account.
- The program calculates the interest earned and the updated balance for the CD account over the specified period.
- Results Displayed:
- The program displays the interest earned and the updated balance for both the savings and CD accounts.


# Prerequisites

Before running the program, ensure that the following modules are properly implemented:

1. cd_account.py: Should include the create_cd_account function.
2. savings_account.py: Should include the create_savings_account function.

This Python script within these files calculates the interest earned and updates the balance for a Savings Account and a CD account based on user-defined inputs such as the account balance, interest rate, and number of months. The program uses the Account class (imported from Account.py) to manage account details and perform balance updates.

The Account.py file creates the Account Class and defines the set_balance and set_interest methods

## Function Definitions:

    1. create_savings_account(balance, interest_rate, months): Returns a tuple (updated_balance, interest_earned) based on the given inputs.
    2. create_cd_account(balance, interest_rate, months): Returns a tuple (updated_balance, interest_earned) based on the given inputs.


    3. Functions create_cd_account and create_savings account:
        These functions perform the following tasks:
        	- Account Creation: Instantiates an Account object with the initial balance.
        	- Interest Calculation: Calculates the interest earned using the formula:
        	- Balance Update: Updates the account balance by adding the interest earned.
        	- Set Methods: Uses set_balance() and set_interest() methods of the Account class to update the account object.
        	- Return Values: The function returns the updated balance and interest earned.
         Parameters:
            - balance (float): The initial balance of the CD account.
            - interest_rate (float): The annual percentage rate (APR) for the CD account.
            - months (int): The number of months the CD will earn interest.
    4. Returns:
    	- The function returns the updated balance and interest earned for each account.

# How to Run
1. Install Python: Ensure you have Python 3.x installed on your machine.
2. Place the Modules: Ensure that the files cd_account.py and savings_account.py are in the same directory as the main script.
3. Run the Script: From the command line or terminal, navigate to the directory containing the script and run:
python <script_name>.py
4. Input Values: Follow the prompts to input the balance, interest rate, and number of months for both the savings and CD accounts.

# Sample Input and Output

**Input:**  
    enter savings balance: 1000  
    enter savings interest rate: 5  
    enter number of months to maturity: 12  
    enter CD balance: 2000  
    enter CD interest rate: 4  
    enter number of months to maturity: 6  

**Output:**  
    interest earned on savings account is 50.0  
    updated savings account balance is 1050.0  
    interest earned on CD account is 40.0  
    updated CD account balance is 2040.0  


# Error Handling

The program checks that the user enters a numeric value for all the inputs.  If the user enters an invalid value, the program tells them they have made an error and prompts them to try again. It assumes that valid numerical inputs are provided for the balances, interest rates, and months. 
