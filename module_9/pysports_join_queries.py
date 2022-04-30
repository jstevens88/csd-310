#Title: pysports_join_queries.py
#Author: Jacob Stevens
#Date: 30 April 2022
#Description: Test program for connecting to a MySQL database through Python and creating INNER JOIN for player and team tables

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
    cursor = db.cursor()
    
    
    #Inner Join on Player/Team
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    #store results in teams variable
    players = cursor.fetchall()
   

    #Display result
    print("\n  -- DISPLAYING PLAYER RECORDS --")
    
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")
    

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