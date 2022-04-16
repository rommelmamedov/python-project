from database import queryDataBaseByFieldName
from helpers import confirm, goToMenu, printErrorMessage, printInfoMessage

def searchBookMenu():
    printInfoMessage('— — — — — — — — — — — — — — —')
    printInfoMessage('| 1 - Search by title.       |')
    printInfoMessage('| 2 - Search by author name. |')
    printInfoMessage('| 3 - Search by category.    |')
    printInfoMessage('| 4 - Exit search.           |')
    printInfoMessage('— — — — — — — — — — — — — — —')
    return input('\nPlease choose one of the following search options (1, 2, 3, 4): ')

def searchBy(field):
    queryDataBaseByFieldName(field)
    if confirm(f'\nDo you want to continue your search by {field}? [Yes/No or Y/N]: '):
        searchBy(field)
    else: 
        if not goToMenu(): 
            searchBook()
    return

def searchBook():
    printInfoMessage('\nBook seaching menu:\n')

    while True:
        choice = searchBookMenu()
        if choice == '1':
            searchBy('title')
        elif choice == '2':
            searchBy('author')
        elif choice == '3':
            searchBy('category')
        elif choice == '4':
            break
        else:
            printErrorMessage('Invalid option! Please select again.')
