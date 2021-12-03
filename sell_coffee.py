import mysql.connector
import mysql_connect
from datetime import datetime

# Main/Sell_Coffee 
# Module Function

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

    if phone in result:
        print("Member found")
        today = datetime.today().strftime('%Y-%m-%d')
        sql = "INSERT INTO sell (cus_id, coffee_id, sell_total,sell_date) VALUES (%s, %s,%s,%s)"
        val = (10, 1, 1.0, today)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, " Sale Successful")
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