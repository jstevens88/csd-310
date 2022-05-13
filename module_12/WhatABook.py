#Title: whatabook
#Author: Jacob Stevens
#Date: 13 MAY 2022
#Description: Whatabook program interface

#Imports
import sys
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
def showMenu():
    print("\n\t--Main Menu--")

    print("\t1. View Book List\n\t2. View Store Locations\n\t3. My Account\n\t4. Exit")

    try:
        choice = int(input('Enter number for Menu item desired:'))

        return choice
    except ValueError:
        print("\nInvalid number, program terminated...\n")
        sys.exit(0)

def showBooks(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details FROM book")
    bookList = _cursor.fetchall()

    print("\t--Book List--")

    for book in bookList:
        print("\t\nBook Name: {}\nAuthor: {}\nDetails: {}\n".format(book[1], book[2], book[3]))


def showLocations(_cursor):
    _cursor.execute("SELECT store_id, locale FROM store")
    storeLocations = _cursor.fetchall()

    print("\t--Store Locations--")

    for store in storeLocations:
        print("\t\nLocale: {}".format(store[1]))


def validateUser():
    try:
        user_id = int(input('\n\tEnter a customer id: '))

        if user_id < 0 or user_id > 3:
            print("\nInvalid customer number, program terminated...\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

def showAccountMenu():
    print("\n\t--Account Menu--")

    print("\t1. Wishlist\n\t2. Add Book\n\t3. Main Menu")
    try:
        acc_choice = int(input('Enter number for menu item desired:'))

        return acc_choice
    except ValueError:
        print("\nInvalid number, program terminated...\n")
        sys.exit(0)

def showWishlist(_cursor, _user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id = {}".format(_user_id))
    wishlist = _cursor.fetchall()

    print("\n\t--Wishlist--")
    for wish in wishlist:
        print("\n\tBook Name: {}\n\tAuthor: {}".format(wish[4], wish[5]))


def showAvailableBooks(_cursor, _user_id):
    _cursor.execute("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    addWishBooks = _cursor.fetchall()

    print("\n\t--Available Books to Add--")

    for books in addWishBooks:
        print("\n\tBook ID: {}\n\tBook Name: {}".format(books[0], books[1]))

def addBook(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))


#Catch any potential errors
try:
    """ try/catch block for handling potential MySQL database errors """ 
    db = mysql.connector.connect(**config) # connect to the WhatABook database 
    cursor = db.cursor() # cursor for MySQL queries
    print("\n\t**Welcome to the WhatABook Application**")

    user_menu_selection = showMenu() # show the main menu 

    
    while user_menu_selection != 4:
        if user_menu_selection == 1:
            showBooks(cursor)
        if user_menu_selection == 2:
            showLocations(cursor)

        if user_menu_selection == 3:
            my_user_id = validateUser()
            account_selection = showAccountMenu()

            while account_selection != 3:
                if account_selection == 1:
                    showWishlist(cursor, my_user_id)
                if account_selection == 2:
                    showAvailableBooks(cursor, my_user_id)
                    book_id = int(input("\n\tEnter the id of the book you want to add: "))

                    addBook(cursor, my_user_id, book_id)
                    db.commit() 
                    print("\n\tBook id: {} was added to your wishlist!".format(book_id))

                 
                if account_selection <= 0 or account_selection > 3:
                    print("\n\tInvalid option, please retry...")

                
                account_selection = showAccountMenu()
        
        
        if user_menu_selection <= 0 or user_menu_selection > 4:
            print("\n\tInvalid option, please retry...")
            
       
        user_menu_selection = showMenu()

    print("\n\tProgram terminated...")


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