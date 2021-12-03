import mysql.connector
import mysql_connect
from datetime import datetime
from prettytable import PrettyTable
import compare_res_mat


'''
mydb = mysql_connect.sql_connect()
mycursor = mydb.cursor()
mycursor.execute("SELECT cus_ph FROM customer")
myresult = mycursor.fetchall()
result = []

for i in myresult:
    result.append(i[0])

phone = input("Type member phone number: ")

if phone in result:
    print("Member found")
    
    
    
today = datetime.today().strftime('%Y-%m-%d')
mydb = mysql_connect.sql_connect()
mycursor = mydb.cursor()

sql = "INSERT INTO sell (cus_id, coffee_id, sell_total,sell_date) VALUES (%s, %s, %s, %s)"
val = (10, 1, 1.0, today)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, " Sale Successful")
'''
"""
start_date = input("Enter your start date (YYYY-MM-DD): ")
end_date = input("Enter your end date (YYYY-MM-DD): ")


mydb = mysql_connect.sql_connect()
mycursor = mydb.cursor()
sql = '''select sell.sell_id, customer.cus_firstname, customer.cus_lastname, coffee.coffee_name, coffee.coffee_price from sell 
INNER JOIN customer on customer.cus_id = sell.cus_id
INNER JOIN coffee on coffee.coffee_id = sell.coffee_id 
WHERE sell_date BETWEEN %s and %s ''' 
 

mycursor.execute(sql, (start_date, end_date))

result = mycursor.fetchall()

customer_information = PrettyTable()
customer_information.field_names = ["Sell ID", "First Name", "Last Name", "Coffee", "Sell"]
customer_information.add_rows(result) 

print(customer_information.get_string())
"""
'''
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
else: 
    print("No member found")
'''
'''
mydb = mysql_connect.sql_connect()
mycursor = mydb.cursor()
mycursor.execute("SELECT cof_bean, water, sugar FROM resource")
result = mycursor.fetchall()

myresult = list(result[0])
int_result = list(result[0])
myresult[0] = str(myresult[0]) + " kg"
myresult[1] = str(myresult[1]) + " ml"
myresult[2] = str(myresult[2]) + " ml"

print(int_result)
#display_result = tuple(myresult)
'''

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