import mysql.connector
from prettytable import PrettyTable
from datetime import datetime
import mysql_connect

# Get All
def get_all():
    mydb = mysql_connect.sql_connect()
    mycursor = mydb.cursor()
    sql = '''select sell.sell_id, customer.cus_firstname, customer.cus_lastname, coffee.coffee_name, coffee.coffee_price from sell
INNER JOIN customer on customer.cus_id = sell.cus_id
INNER JOIN coffee on coffee.coffee_id = sell.coffee_id'''
    mycursor.execute(sql)
    result = mycursor.fetchall()

    customer_information = PrettyTable()
    customer_information.field_names = ["Sell ID", "First Name", "Last Name", "Coffee", "Sell"]
    customer_information.add_rows(result) 

    print(customer_information.get_string())
    
# Specific Date    
def from_specific_date():
    mydb = mysql_connect.sql_connect()
    mycursor = mydb.cursor()

    sql = '''select sell.sell_id, customer.cus_firstname, customer.cus_lastname, coffee.coffee_name, coffee.coffee_price from sell
INNER JOIN customer on customer.cus_id = sell.cus_id
INNER JOIN coffee on coffee.coffee_id = sell.coffee_id
WHERE sell_date BETWEEN '12:00:00' and "22:00:00" '''

    mycursor.execute(sql)

    result = mycursor.fetchall()

    customer_information = PrettyTable()
    customer_information.field_names = ["Sell ID", "First Name", "Last Name", "Coffee", "Sell"]
    customer_information.add_rows(result) 

    print(customer_information.get_string())