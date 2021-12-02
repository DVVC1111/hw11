import mysql.connector
import mysql_connect
import sale

#def sell_member():
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
    sale.sale()
else: 
    print("No member found")


    

    
    

    