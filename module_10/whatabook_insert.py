#Title: whatabook Inserts
#Author: Jacob Stevens
#Date: 7 MAY 2022
#Description: Program to insert Book records into whatabook database

#Imports
import mysql.connector
from mysql.connector import errorcode

#Configures connection profile
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#Catch any potential errors
try:
    #connect to the pysports database 
    db = mysql.connector.connect(**config) 
    cursor = db.cursor()
    
    
    # insert player query 
    cursor.execute("INSERT INTO book(book_name, author, details) VALUES('The Return of the King', 'J.R.Tolkien', 'The third part of The Lord of the Rings');")
    cursor.execute("INSERT INTO book(book_name, author, details) VALUES('The Fellowship of the Ring', 'J.R.Tolkien', 'The first part of The Lord of the Rings');")
    cursor.execute("INSERT INTO book(book_name, author, details) VALUES('The Two Towers', 'J.R.Tolkien', 'The second part of The Lord of The Rings');")

    cursor.execute("INSERT INTO book(book_name, author) VALUES('The Hobbit or There and Back Again', 'J.R.Tolkien');")
    cursor.execute("INSERT INTO book(book_name, author) VALUES('Dune: Deluxe Edition', 'Frank Herbert');")
    cursor.execute("INSERT INTO book(book_name, author) VALUES('Charlote's Web', 'E.B. White');")
    cursor.execute("INSERT INTO book(book_name, author) VALUES('The Great Gatsby', 'F. Scott Fitzgerald');")
    cursor.execute("INSERT INTO book(book_name, author) VALUES('The Lion, the Witch, and the Wardrobe', 'C.S. Lewis');")
    cursor.execute("INSERT INTO book(book_name, author) VALUES('The Catcher and the Rye', 'J.D. Salinger' );")
    
    # commit the insert to the database 
    db.commit()
