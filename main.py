import sell_coffee
import report

# Main
print('''
      ----- Welcome to CS111 Coffee Shop -----
      Key in number to get started ...
      (1) : Sell Coffee
      (2) : Report
      (3) : Inventory
      (E) : Exit 
      ''')
main_select = int(input("Key in selection: "))

# Sell Coffee (1)

if main_select == 1:
    print('''
        ----- Welcome to CS111 Coffee Shop -----
        ----------------------------------------
        For Member or Guest
        (1) : Guest
        (2) : Member
        (3) : Register
        (e) : Exit 
        ''')
    sell_select = int(input("Key in selection: "))
    
    if sell_select == 1:
        print("You're a Guest")
        
    elif sell_select == 2:
        sell_coffee.member()
        
    elif sell_select == 3:
        sell_coffee.register()

# Report (2)
        
elif main_select == 2:
    print("""
          -----Report Options-----
          -------------------------
          (1) : Resource Report
          (2) : Sale Report
          (3) : Member Report
          (e) : Exit
          """)      
    report_select = int(input("Key in selection: ")) 
    
    if report_select == 1:
        report.resource_report()
    
    elif report_select == 2:
        report.sale_report()
        
    elif report_select == 3:
        report.member_report() 

# Inventory (3)
       
elif main_select == 3:
    print("Inventory")
   
else:
    print("Unkwnown Input")
