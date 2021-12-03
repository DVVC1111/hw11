import mysql.connector
import mysql_connect
from datetime import datetime
from prettytable import PrettyTable


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