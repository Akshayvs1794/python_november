#database connectivity in python

import mysql.connector

try:
    
    conn = mysql.connector.connect(host="127.0.0.1", 
                                   user="root", 
                                   passwd="root",
                                   database="demo")
    myCursor = conn.cursor()
    myCursor.execute("select * from student")

    for i in myCursor:
        print(i)

except Exception as e:
    print("ERROR : ",e)