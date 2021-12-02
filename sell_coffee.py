import register

def sell_coffee():
    print('''
        ----- Welcome to CS111 Coffee Shop -----
        For Member or Guest
        (1) : Guest
        (2) : Member
        (3) : Register
        (E) : Exit 
        ''')

    select = int(input("Key in selection: "))

    if select == 3:
        firstname = input("Input Firstname: ")
        lastname = input("Input Lastname: ")
        phone = input("Input Phone Number: ")
        register.register(firstname, lastname, phone)
        
    else:
        print("Unkwnown Input")