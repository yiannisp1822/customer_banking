# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """

    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

check_bank_accounts = True
while check_bank_accounts:
    while True:
        try:
            savings_balance = float(input("Enter savings balance: "))
            break

        except ValueError:
            print("Savings balance must be a number. Please try again.")
            

    while True:
        try: 
            savings_interest = float(input("Enter savings interest rate: "))
            break

        except ValueError:
            ("Savings interest must be a number. Please try again.")

    while True:
        try:
            savings_maturity = abs(int(input("Enter number of months to maturity: ")))
            break

        except ValueError:
            ("Maturity must be a number. Please try again.")
        
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_account = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Interest earned on savings account is {updated_savings_account[1]}")
    print(f"Updated savings account balance is {updated_savings_account[0]}")

    while True:
        try:
            cd_balance = float(input("Enter CD balance: "))
            break

        except ValueError:
            print("CD balance must be a positive number.")


    while True:
        try:
            cd_interest = float(input("Enter CD interest rate: "))
            break

        except ValueError:
            print("CD interest rate must be a number.")

    while True:
        try:
            cd_maturity = abs(int(input("Enter number of months to maturity: ")))
            break

        except ValueError:
            print("CD maturity months must be a number.")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_account = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Interest earned on CD account is {updated_cd_account[1]}")
    print(f"Updated CD account balance is {updated_cd_account[0]}")

    while True:
        stay_on = input("Would you like to continue? (Y)es or (N)o ").strip().lower()
        if stay_on in ['y', 'n']:
            check_bank_accounts = (stay_on == 'y')
            if stay_on == 'n':
                print("Goodbye.")
            break
        else:
            print("Invalid input, please try again - type (Y)es or (N)o.")

if __name__ == "__main__":
    # Call the main function.
    main()
