
#Title: mysql_test.py
#Author: Jacob Stevens
#Date: 23 April 2022
#Description: Test program for connecting to a MySQL database through Python
    
    


#Imports
import mysql.connector
from mysql.connector import errorcode

#Configures connection profile
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


#Catch any potential errors
try:
    #connect to the pysports database 
    db = mysql.connector.connect(**config) 
    
    #output the connection status 
    print("\n\tUser {} is connected to {} MySQL database on host {}".format(config["user"], config["database"], config["host"]))

    input("\n\n\tPress any key to continue...")


#Error Handling
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\tThe supplied username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\tThe specified database does not exist")

    else:
        print(err)

#Close database connection
finally:
    
    db.close()