from database import getAvailableBooks
from helpers import confirm,  getValidAndUniqueValue, printSuccessMessage, printInfoMessage


'''
----------------------UML-------------------
- Name: Receipt
- Properties: Title, Author, Price, ISBN
- Functionality or behavior : generate()
--------------------------------------------
'''


# book1 = Book('The Catcher in the Rye', 'J.D. Salinger', 12.86, 31676917)
# book2 = Book('The Hobbit', 'J.R.R. Tolkien', 18.00, 978004441)
# book3 = Book('Harry Potter Sorcerer Stone', 'J.K. Rowling', 23.44, 97805903)
# book4 = Book('Introduction to Algorithms', 'Thomas H. Cormen', 20.30, 62032937)
# book4.change_price(19.99)


def receipt(purchased_book_id_list):
    class Receipt:
        def __init__(self, book_id_list):
            self.__book_id_list = book_id_list
            self.__availableBooksByLimit = getAvailableBooks()


        def generate(self, fileName):
            self.__book_id_list

    newReceipt = Receipt(purchased_book_id_list)
    newReceipt.generate()


    # printInfoMessage('\nItem creation page:\n')
    # itemNumber = getValidAndUniqueValue(currentItems, 0, 'item number')
    # if itemNumber == 'no': return
  
    # itemName = getValidNameFieldValue('Item')
    # if itemName == 'no': return

    # itemCost = getValidNumericValue('Please input item cost: ', 'item cost')
    # if itemCost == 'no': return
  
    # currentItems.append([itemNumber, itemName, itemCost])

    # printSuccessMessage(f"\nNew item with number: '{itemNumber}' and name: '{itemName}' successfully added into list.")
  
    # if confirm('\nDo you want to add another item into list? [Yes/No or Y/N]: '):
    #     searchBook(currentItems)

    # return currentItems