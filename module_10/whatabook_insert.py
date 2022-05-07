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
    
    
    # insert book records 
    cursor.execute("INSERT INTO book(book_name, author, details) VALUES('The Return of the King', 'J.R.Tolkien', 'The third part of The Lord of the Rings');")
    cursor.execute("INSERT INTO book(book_name, author, details) VALUES('The Fellowship of the Ring', 'J.R.Tolkien', 'The first part of The Lord of the Rings');")
    cursor.execute("INSERT INTO book(book_name, author, details) VALUES('The Two Towers', 'J.R.Tolkien', 'The second part of The Lord of The Rings');")

    cursor.execute("INSERT INTO book(book_name, author) VALUES('The Hobbit or There and Back Again', 'J.R.Tolkien');")
    cursor.execute("INSERT INTO book(book_name, author) VALUES('Dune: Deluxe Edition', 'Frank Herbert');")
    cursor.execute("INSERT INTO book(book_name, author) VALUES(\"Charlote's Web\", 'E.B. White');")
    cursor.execute("INSERT INTO book(book_name, author) VALUES('The Great Gatsby', 'F. Scott Fitzgerald');")
    cursor.execute("INSERT INTO book(book_name, author) VALUES('The Lion, the Witch, and the Wardrobe', 'C.S. Lewis');")
    cursor.execute("INSERT INTO book(book_name, author) VALUES('The Catcher and the Rye', 'J.D. Salinger' );")
    
    #insert users
    cursor.execute("INSERT INTO user(first_name, last_name) VALUES('Thorin', 'Oakenshield' );")
    cursor.execute("INSERT INTO user(first_name, last_name) VALUES('Bilbo', 'Baggins');")
    cursor.execute("INSERT INTO user(first_name, last_name) VALUES('Frodo', 'Baggins');")

    #insert wishlist
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES((SELECT user_id FROM user WHERE first_name = 'Thorin'),(SELECT book_id FROM book WHERE book_name = 'The Hobbit or There and Back Again'));")
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES((SELECT user_id FROM user WHERE first_name = 'Bilbo'),(SELECT book_id FROM book WHERE book_name = 'The Fellowship of the Ring'));")
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES((SELECT user_id FROM user WHERE first_name = 'Frodo'),(SELECT book_id FROM book WHERE book_name = 'The Return of the King'));")
    # commit the insert to the database 
    db.commit()


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