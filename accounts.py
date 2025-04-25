import other


accounts_data = [{"name" : "Sarah", "account" : 1234, "amount" : 250},
                 {"name" : "John", "account" : 4567, "amount" : 4500},
                 {"name" : "Conner", "account" : 8910, "amount" : 34}
                ]


def add_account(name, account_number, amount):
  account = {
      "name": name,
      "account": account_number,
      "amount": amount
  }
  accounts_data.append(account)