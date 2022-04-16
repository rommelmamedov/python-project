from helpers import confirm, getValidNameFieldValue, getValidAndUniqueValue, printSuccessMessage, printInfoMessage


'''
----------------------UML-------------------
- Name: Receipt
- Properties: Title, Author, Price, ISBN
- Functionality or behavior : generate_receipt()
--------------------------------------------
'''


class Order:
    def __init__(self, ISBN, title):
        self.ISBN = ISBN
        self.title = title
        self.returnDate = None

    def setReturnDate(self, returnDate):
        self.returnDate = returnDate

#
# book1 = Book('The Catcher in the Rye', 'J.D. Salinger', 12.86, 31676917)
# book2 = Book('The Hobbit', 'J.R.R. Tolkien', 18.00, 978004441)
# book3 = Book('Harry Potter Sorcerer Stone', 'J.K. Rowling', 23.44, 97805903)
# book4 = Book('Introduction to Algorithms', 'Thomas H. Cormen', 20.30, 62032937)

# book4.change_price(19.99)

# print(book1)
# print(book2)
# print(book3)
# print(book4)


def generateReceipt():
    print('— — — — — — — — — — — — — — —')
    printInfoMessage('| 1 - Search for book.      |')
    printInfoMessage('| 2 - Purchase a book.      |')
    printInfoMessage('| 3 - Generate receipt.     |')
    printInfoMessage('| 4 - Exit.                 |')
    print('— — — — — — — — — — — — — — —')

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