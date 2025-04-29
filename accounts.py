import random
new_number = 0 

account_numbers = [1234, 4567, 8910]

accounts_data = [{
    "name": "Sarah",
    "account": 1234,
    "amount": 250
}, {
    "name": "John",
    "account": 4567,
    "amount": 4500
}, {
    "name": "Conner",
    "account": 8910,
    "amount": 34
}]


def add_account(name, account_number, amount):
    account = {"name": name, "account": account_number, "amount": amount}
    accounts_data.append(account)

def number_generation():
    global new_number
    while True:
        new_number = random.randint(1000, 9999)
        if new_number in account_numbers:
            print("Numbers match.")
        else:
            account_numbers.append(new_number)
            return new_number
            
            

            
             

  


    
