import mysql.connector
import mysql_connect

def refilling():

  print("""
    -----Select Item to Refill-----
    ------------------------------
    (1) : Water
    (2) : Coffee Bean
    (3) : Sugar
    (e) : Exit
    
    """)

  user_input = input("Pick Item to Refill: ")

  if user_input == "1":
    print("-----Refilling Water-----")
    refilling = int(input("Input amount to refill: "))
    mydb = mysql_connect.sql_connect()
    mycursor = mydb.cursor()
    sql = "UPDATE resource SET water = water + %s WHERE res_id = 1 "
    val = (refilling, )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "item refilled")
      
  elif user_input == "2":
    print("-----Refilling Coffee Bean-----")
    refilling = int(input("Input amount to refill: "))
    mydb = mysql_connect.sql_connect()
    mycursor = mydb.cursor()
    sql = "UPDATE resource SET cof_bean = cof_bean + %s WHERE res_id = 1 "
    val = (refilling, )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "item refilled")
      
  elif user_input == "3":
    print("-----Refilling Sugar-----")
    refilling = int(input("Input amount to refill: "))
    mydb = mysql_connect.sql_connect()
    mycursor = mydb.cursor()
    sql = "UPDATE resource SET sugar = sugar + %s WHERE res_id = 1 "
    val = (refilling, )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "item refilled")
      
  elif user_input == "e" or user_input == "E":
    return
