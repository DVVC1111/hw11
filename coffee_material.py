import mysql.connector
from prettytable import PrettyTable

def coffee_material():
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    port="8889",
    database= "homework10"
    )

    mycursor = mydb.cursor()

    sql = '''select coffee.coffee_name, material.mat_cofbean, material.mat_water, material.mat_sugar from coffee
    inner join material on material.mat_id = coffee.mat_id'''

    mycursor.execute(sql)

    result = mycursor.fetchall()

    customer_information = PrettyTable()
    customer_information.field_names = ["Coffee Name", "Coffee Bean (kg)", "Water (ml)", "Sugar (kg)"]
    customer_information.add_rows(result) 

    print(customer_information.get_string())