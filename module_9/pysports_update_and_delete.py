#Title: pysports_update_and_delete.py
#Author: Jacob Stevens
#Date: 30 April 2022
#Description: Test program for connecting to a MySQL database through Python and updating/deleting records through join queries

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
    
    
    # insert player query 
    cursor.execute("INSERT INTO player(first_name, last_name, team_id) VALUES('Smeagol','Shire Folk', 1);")
    

    

    # commit the insert to the database 
    db.commit()

    # inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get the results from the cursor object 
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYERS AFTER INSERT --")
    
    # iterate over the player data set and display the results 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    # update the newly inserted record 
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    # execute the update query
    cursor.execute(update_player)


    # inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get the results from the cursor object 
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYERS AFTER UPDATE --")
    
    # iterate over the player data set and display the results 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    # delete query 
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute(delete_player)
    
    # inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get the results from the cursor object 
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYERS AFTER DELETE --")
    
    # iterate over the player data set and display the results 
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