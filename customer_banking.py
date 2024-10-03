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
    savings_balance = float(input("enter savings balance: "))
    savings_interest = float(input("enter savings interest rate: "))
    savings_maturity = int(input("enter number of months to maturity: "))


    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_account = create_savings_account(savings_balance, savings_interest, savings_maturity)


    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"interest earned on savings account is {updated_savings_account[1]}")
    print(f"updated savings account balance is {updated_savings_account[0]}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("enter CD balance: "))
    cd_interest = float(input("enter CD interest rate: "))
    cd_maturity = int(input("enter number of months to maturity: "))

    # Call the create_cd_account function and pass the variables from the user.
    # updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    updated_cd_account = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"interest earned on CD account is {updated_cd_account[1]}")
    print(f"updated CD account balance is {updated_cd_account[0]}")


if __name__ == "__main__":
    # Call the main function.
    main()
