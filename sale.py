import mysql.connector
import mysql_connect
from datetime import datetime


def sale():
    today = datetime.today().strftime('%Y-%m-%d')
    mydb = mysql_connect.sql_connect()
    mycursor = mydb.cursor()

    sql = "INSERT INTO sell (cus_id, coffee_id, sell_total,sell_date) VALUES (%i, %i,%f,%s)"
    val = (10, 1, 1.0, today)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, " Sale Successful")