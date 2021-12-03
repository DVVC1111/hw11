import mysql.connector
from prettytable import PrettyTable
import mysql_connect
import sale_report

# Main/System/Report 
# Module Functions

def report(): 
    print("""
        -----Report Options-----
        -------------------------
        (1) : Resource Report
        (2) : Sale Report
        (3) : Member Report
        (e) : Exit
        """)      
    report_select = input("Key in selection: ")
    
    if report_select == "1":
        Report_Function.resource_report()
    
    elif report_select == "2":
        Report_Function.sale_report()
        
    elif report_select == "3":
        Report_Function.member_report() 
    
    elif report_select == "e" or report_select== "E":
        return
        


class Report_Function:
    # Resource Report (1)
    def resource_report():
        mydb = mysql_connect.sql_connect()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT cof_bean, water, sugar FROM resource")
        result = mycursor.fetchall()
        
        myresult = list(result[0])
        myresult[0] = str(myresult[0]) + " kg"
        myresult[1] = str(myresult[1]) + " ml"
        myresult[2] = str(myresult[2]) + " ml"
        display_result = tuple(myresult)
        
        customer_information = PrettyTable()
        customer_information.field_names = ["Coffee Bean", "Water", "Sugar"]
        customer_information.add_rows([display_result]) 
        print(customer_information.get_string())

    # Sale Report (2)
    def sale_report():
        user_input = input("""
                Select Sale Report:
                (1): Get All
                (2): From Specific Date
                (e): Exit
                Key In:  """)
        if user_input == 1:
            # Main/Report/Sale_Report/Get_All
            sale_report.get_all()
        elif user_input == 2:
            # Main/Report/Sale_Report/From_Specific_Date
            sale_report.from_specific_date()

    # Member Report (3)
    def member_report():
        mydb = mysql_connect.sql_connect()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM customer")
        myresult = mycursor.fetchall()

        totalmember = len(myresult)
        print(f"Total Member: {totalmember}")

        customer_information = PrettyTable()
        customer_information.field_names = ["Customer ID", "FirstName", "LastName", "Phone Number"]
        customer_information.add_rows(myresult) 
        print(customer_information.get_string())


        
        
        
        













