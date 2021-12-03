import mysql.connector
import mysql_connect
from datetime import datetime


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
    
    
    '''
today = datetime.today().strftime('%Y-%m-%d')
mydb = mysql_connect.sql_connect()
mycursor = mydb.cursor()

sql = "INSERT INTO sell (cus_id, coffee_id, sell_total,sell_date) VALUES (%s, %s, %s, %s)"
val = (10, 1, 1.0, today)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, " Sale Successful")
