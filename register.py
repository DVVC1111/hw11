import mysql.connector
import mysql_connect


def register(firstname, lastname, phone):
    mydb = mysql_connect.sql_connect()
    mycursor = mydb.cursor()

    sql = "INSERT INTO customer (cus_firstname,cus_lastname,cus_ph) VALUES (%s, %s,%s)"
    val = (firstname, lastname, phone)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "user(s) registered")