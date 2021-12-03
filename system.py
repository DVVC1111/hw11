import sell_coffee
import report

def System():
    print('''
        ----- Welcome to CS111 Coffee Shop -----
        Key in number to get started ...
        (1) : Sell Coffee
        (2) : Report
        (3) : Inventory
        (E) : Exit 
        ''')
    main_select = input("Key in selection: ")

    # Sell Coffee (1)
    if main_select == "1":
        sell_coffee.sell_coffee()
        System()

    # Report (2)      
    elif main_select == "2":
        report.report()
        System()
        

    # Inventory (3) 
    elif main_select == "3":
        print("Inventory")
        System()
    
    elif main_select == "e" or main_select == "E":
        return
    
    # Catch Input
    else:
        print("Unkwnown Input")