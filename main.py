import sell_coffee
import report

print('''
      ----- Welcome to CS111 Coffee Shop -----
      Key in number to get started ...
      (1) : Sell Coffee
      (2) : Report
      (3) : Inventory
      (E) : Exit 
      ''')

first_select = int(input("Key in selection: "))

if first_select == 1:
    print('''
        ----- Welcome to CS111 Coffee Shop -----
        For Member or Guest
        (1) : Guest
        (2) : Member
        (3) : Register
        (E) : Exit 
        ''')
    sell_select = int(input("Key in selection: "))
    
    if sell_select == 1:
        print("You're a Guest")
        
    elif sell_select == 2:
        sell_coffee.member()
        
    elif sell_select == 3:
        sell_coffee.register()
        
        
    
else:
    print("Unkwnown Input")
