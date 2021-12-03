import mysql.connector
import mysql_connect

# Decrease the resource accordingly after sale


def decrease_resource(coffee_material):
    mydb = mysql_connect.sql_connect()
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE resource SET water = water - %s WHERE res_id = 1 ", (coffee_material[0], ))
    mycursor.execute("UPDATE resource SET cof_bean = cof_bean - %s WHERE res_id = 1 ", (coffee_material[1], ))
    mycursor.execute("UPDATE resource SET sugar = sugar - %s WHERE res_id = 1 ", (coffee_material[2], ))
    mydb.commit()
    

   