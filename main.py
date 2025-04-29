import other
greeted = False

#Greeting Loop
while True: 
    if not greeted:
        other.greeting()
        greeted = True
        

    command = input("Please type: help ")



    if command == "help":
        other.help()
            
        
    
    elif command == "view_accounts":
        other.view_accounts()
        other.select_accounts()
       
    
    elif command == "create_account":
        other.create_account()
        

    elif command == "exit":
        print("Exiting...")
        exit()
        


    else:
        other.miss_Type()