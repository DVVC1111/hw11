import sell_coffee


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
    sell_coffee.sell_coffee()
    
else:
    print("Unkwnown Input")
