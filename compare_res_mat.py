import mysql.connector
import mysql_connect

def check_mat(coffee_material):
    mydb = mysql_connect.sql_connect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT  water, cof_bean,sugar FROM resource")
    result = mycursor.fetchall()
    total_resource = list(result[0])
    
    for i in range(len(coffee_material)):
        if coffee_material[i] > total_resource[i]:
            return False
            break
    return True


    

    