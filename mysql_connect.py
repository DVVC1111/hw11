import mysql.connector

def sql_connect():
    mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            port="8889",
            database= "homework10"
        )
    
    return mydb