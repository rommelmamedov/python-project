"""
Ramil Mamedov - 101343299
COMP 2152 - Open Source Development - Term Project
Lab Professor: Mr. Hesham Akbari
"""

from search import search
from receipt import receipt
from purchase import purchase
from database import initializeDatabase
from helpers import goToMenu, printInfoMessage, printErrorMessage

# Library: users should be able to search for books by title or by author, should be able to search by book category (fiction, non-fiction, autobiographies, travel, etc.). The user should be able to purchase one or more books in any combination of authors, titles, categories, etc. The application should generate and display a receipt stating the list of books selected and their return due dates.

# Basic:
#* 1. Should have a functioning menu. [10]
# 2. Should have adequate functions (minimum 3 functions). [15]
# 3. Should make use of files to save the data. [15]
# 4. Should handle adequate exceptions. [7]
# 5. Should display information formatted adequately. [8]
#* 6. Should make use of lists or dictionaries as appropriate. [15]
#* 7. Should follow adequate naming conventions for variables and functions, and should have comments as appropriate. [5]
# 
# Intermediate:
#* 8. Should use an object-oriented approach, (inheritance is optional). [10]
#* 9. Should use a database. [15]

def menu():
    printInfoMessage('— — — — — — — — — — — — — — —')
    printInfoMessage('| 1 - Search for book.      |')
    printInfoMessage('| 2 - Purchase a book.      |')
    printInfoMessage('| 3 - Generate receipt.     |')
    printInfoMessage('| 4 - Exit.                 |')
    printInfoMessage('— — — — — — — — — — — — — — —')
    return input('Choose one of the following options (1, 2, 3, 4): ')


def main():
    initializeDatabase()
    purchased_book_id_list = []
    print("\nWelcome to the library program!")

    while True:
        choice = menu()
        if choice == '1':
            search()
            if not goToMenu():
                break
        elif choice == '2':
            purchased_book_id_list = purchase(purchased_book_id_list)
            if not goToMenu():
                break
        elif choice == '3':
            receipt(purchased_book_id_list)
            if not goToMenu():
                break
        elif choice == '4':
            printInfoMessage('Thanks for using our program!')
            break
        else:
            printErrorMessage('Invalid option! Please select again.')

main()
