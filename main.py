import other


help = input(other.greeting())

if help == "help":
    command = input(other.help())
    
else:
    other.miss_Type()

if command == "view_accounts":
    other.view_accounts()
    other.select_accounts()

if command == "create_account":
    other.create_account()
    

if command == "exit":
    other.exit()

else:
    other.miss_Type()
