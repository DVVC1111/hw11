import mysql.connector
import mysql_connect

coffee_id_selection = int(input("Pick Coffee: "))

mydb = mysql_connect.sql_connect()
mycursor = mydb.cursor()
mycursor.execute("SELECT  mat_water, mat_cofbean, mat_sugar FROM material WHERE mat_id=%s", (coffee_id_selection, ))
coffee_mat = list((mycursor.fetchall())[0])
print(coffee_mat)