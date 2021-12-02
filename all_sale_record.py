import mysql.connector
from prettytable import PrettyTable

def all_sale_record():
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    port="8889",
    database= "homework10"
    )

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