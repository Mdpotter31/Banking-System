import accounts


def greeting():
  print("Welcome to your first day on the job as a bank teller.")
  print(
      "You will use the command line to perform actions that allow you to view and edit bank accounts. Type 'help' to get started. "
  )


def help():
  print("Please use the following commands to navigate")
  print("view_accounts: View the list of accounts.")
  print("create_account: Create a new account.")
  print("exit: Exit the banking system.")


def miss_Type():
  print("Command not recognized. Please retry.")


def view_accounts():
  print("Viewing accounts...")

  for account in accounts.accounts_data:
    print(
        f"Name: {account['name']}/ Account Number: {account['account']}/ Amount: {account['amount']}"
    )


def create_account():
    print("Creating Accounts...")
    first_name = input("Please provide your first name: ")
    initial_amount = input("Please provide the initial amount for your account: ")
    account_number = accounts.number_generation()  # Correct function call here

    accounts.add_account(first_name, account_number, initial_amount)
    print(f"Account created! Name: {first_name}, Account Number: {account_number}, Initial Amount: {initial_amount}")


def select_accounts():
  print("Selecting Accounts")

  account_choice = input(
      "Please select the account you wish to edit by typing their account number."
  )
  account_number = int(account_choice)
  for account in accounts.accounts_data:
    if account["account"] == account_number:
      account_amount = int(account["amount"])
      print("You chose account " + account_choice)
      print(f"The account has {account_amount}")
      break
  else:
    print("Account number not recoginized")
  while True:
    selection = input("What would you like to edit in the account? Please type withdraw or deposit."
  )
 
    if selection == "withdraw":
      withdraw_amount = int(input("How much would you like to withdraw?"))

      if withdraw_amount <= account_amount:
        print("You get $", withdraw_amount)
        amount_left = account_amount - withdraw_amount
        print("There is $", amount_left, " in the account.")
        account["amount"] = amount_left  #Needs to update the actual amount
        break

      else:
        print("Not enough funds to withdraw amount.")

    elif selection == "deposit":
      deposit_amount = int(input("How much are you depositing?"))
      print("You deposited $", deposit_amount)
      amount_left = account_amount + deposit_amount
      print("There is $", amount_left, " in the account.")
      account["amount"] = amount_left  #Needs to update the actual amount

    else:
      miss_Type()
