import mysql.connector
from prettytable import PrettyTable
import mysql_connect

mydb = mysql_connect.sql_connect()

mycursor = mydb.cursor()

mycursor.execute("SELECT cof_bean, water, sugar FROM resource")

result = mycursor.fetchall()

myresult = list(result[0])


myresult[0] = str(myresult[0]) + " kg"
myresult[1] = str(myresult[1]) + " ml"
myresult[2] = str(myresult[2]) + " ml"

display_result = tuple(myresult)




customer_information = PrettyTable()
customer_information.field_names = ["Coffee Bean", "Water", "Sugar"]
customer_information.add_rows([display_result]) 

print(customer_information.get_string())
