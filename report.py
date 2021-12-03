import mysql.connector
from prettytable import PrettyTable
import mysql_connect
import sale_report

# Resource Report (1)
def resource_report():
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

# Sale Report (2)
def sale_report():
    user_input = input("""
            Select Sale Report:
            (1): Get All
            (2): From Specific Date
            (e): Exit
            Key In:  """)
    if user_input == 1:
        sale_report.get_all()
    elif user_input == 2:
        sale_report.from_specific_date()

# Customer Report (3)
def customer_report():
    mydb = mysql_connect.sql_connect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM customer")
    myresult = mycursor.fetchall()

    totalmember = len(myresult)
    print(f"Total Member: {totalmember}")

    customer_information = PrettyTable()
    customer_information.field_names = ["Customer ID", "FirstName", "LastName", "Phone Number"]
    customer_information.add_rows(myresult) 
    print(customer_information.get_string())


        
        
        
        













