import mysql.connector
import mysql_connect
from datetime import datetime
import compare_res_mat

# Main/System/Sell_Coffee 
# Module Function

def sell_coffee():
    print('''
        ----- Welcome to CS111 Coffee Shop -----
        ----------------------------------------
        For Member or Guest
        (1) : Guest
        (2) : Member
        (3) : Register
        (e) : Exit 
        ''')
    sell_select = input("Key in selection: ")
    
    if sell_select == "1":
        print("You're a Guest")
        sell_coffee()
        
    elif sell_select == "2":
        Sell_Coffee_Function.member()
        sell_coffee()
        
    elif sell_select == "3":
        Sell_Coffee_Function.register()
        sell_coffee()

    elif sell_select == "e" or sell_select == "E":
        return


class Sell_Coffee_Function:
    
    # Member (2)
    def member():    
        mydb = mysql_connect.sql_connect()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT cus_ph FROM customer")
        myresult = mycursor.fetchall()
        result = []

        for i in myresult:
            result.append(i[0])
            
        phone = input("Type member phone number: ")
        cus_index = int(result.index(phone))
        customer_index = cus_index + 1


        if phone in result:
            print("Member found")
            today = datetime.today().strftime('%Y-%m-%d')
            
            print("""
            -----Select Your Coffee-----
            ------------------------------
            (1) : Americano - 1.5
            (2) : Latte - 2.0
            (3) : Cappuccino - 2.5
            (e) : Exit 
            """)
            
            coffee_id_selection = int(input("Coffee Selection: "))
            total_price = 0
            if coffee_id_selection == 1:
                total_price += 1.5
            elif coffee_id_selection == 2:
                total_price += 2.0
            elif coffee_id_selection == 3:
                total_price += 2.5
            
            mycursor.execute("SELECT  mat_water, mat_cofbean, mat_sugar FROM material WHERE mat_id=%s", (coffee_id_selection, ))
            coffee_mat = list((mycursor.fetchall())[0])
            instock_or_not = compare_res_mat.check_mat(coffee_mat)
            
            if instock_or_not == True:
            
                sql = "INSERT INTO sell (cus_id, coffee_id, sell_total,sell_date) VALUES (%s, %s,%s,%s)"
                val = (customer_index, coffee_id_selection, 1.0, today)
                mycursor.execute(sql, val)

                
                mydb.commit()

                mycursor.execute("SELECT cus_firstname FROM customer WHERE cus_id=%s",(customer_index, ))
                username = (mycursor.fetchall())[0][0]
                
                print(mycursor.rowcount, " Sale Successful")
                    
                print("""
                    Thank you, {0}
                    Total: {1} USD
                    Your Coffee will be ready in 10 hours  
                    """.format(username, total_price)) 
            
            elif instock_or_not == False:
                print("You don't have enough resource")
            
        else: 
            print("No member found")




    # Register (3)
    def register():
        firstname = input("Input Firstname: ")
        lastname = input("Input Lastname: ")
        phone = input("Input Phone Number: ")
        mydb = mysql_connect.sql_connect()
        mycursor = mydb.cursor()

        sql = "INSERT INTO customer (cus_firstname,cus_lastname,cus_ph) VALUES (%s, %s,%s)"
        val = (firstname, lastname, phone)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "user(s) registered")