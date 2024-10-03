# customer_banking
module 3 challenge


README: Savings and CD Account Interest Calculator

Overview

This program calculates and displays the interest earned and the updated balance for both a savings account and a certificate of deposit (CD) account over a specified period. Users are prompted to input the account balance, interest rate, and the number of months to maturity for both types of accounts. The program uses two imported functions, create_savings_account and create_cd_account, to calculate interest and update the balances accordingly.

Program Flow

1.	Savings Account Input:
•	The user is prompted to input:
•	The initial balance of the savings account.
•	The interest rate (in percentage).
•	The number of months the savings account will accrue interest.
•	The program calculates the interest earned and the updated balance for the given period.


    2.	CD Account Input:
    •	The user is prompted to input:
    •	The initial balance of the CD account.
    •	The interest rate (in percentage).
    •	The number of months until maturity for the CD account.
    •	The program calculates the interest earned and the updated balance for the CD account over the specified period.
    3.	Results Displayed:
    •	The program displays the interest earned and the updated balance for both the savings and CD accounts.


Prerequisites

Before running the program, ensure that the following modules are properly implemented:

    1.	cd_account.py: Should include the create_cd_account function.
    2.	savings_account.py: Should include the create_savings_account function.

Expected Function Definitions:

    •	create_savings_account(balance, interest_rate, months): Returns a tuple (updated_balance, interest_earned) based on the given inputs.
    •	create_cd_account(balance, interest_rate, months): Returns a tuple (updated_balance, interest_earned) based on the given inputs.

How to Run

    1.	Install Python: Ensure you have Python 3.x installed on your machine.
    2.	Place the Modules: Ensure that the files cd_account.py and savings_account.py are in the same directory as the main script.
    3.	Run the Script: From the command line or terminal, navigate to the directory containing the script and run:
python <script_name>.py

4.	Input Values: Follow the prompts to input the balance, interest rate, and number of months for both the savings and CD accounts.

Sample Input and Output

Input:
enter savings balance: 1000
enter savings interest rate: 5
enter number of months to maturity: 12
enter CD balance: 2000
enter CD interest rate: 4
enter number of months to maturity: 6

Output:
interest earned on savings account is 50.0
updated savings account balance is 1050.0
interest earned on CD account is 40.0
updated CD account balance is 2040.0


Error Handling

The program assumes that valid numerical inputs are provided for the balances, interest rates, and months. If invalid inputs (such as non-numeric values) are entered, the program will raise a ValueError. Adding input validation is recommended for production use.

Customization

You can modify the logic inside the create_savings_account and create_cd_account functions to handle more complex interest calculations, such as compound interest or varying interest rates over time.
d.
