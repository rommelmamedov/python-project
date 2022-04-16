from helpers import confirm
from datetime import datetime
from database import getAvailableBooks

'''
----------------------UML-------------------
- Name: Receipt
- Properties: Title, Author, Price, ISBN
- Functionality or behavior : generate(), getContent()
--------------------------------------------
'''

newLine = '\n'

class Receipt:
    def __init__(self, booksIdList):
        self.__booksIdList = booksIdList
        self.__availableBooksByLimit = getAvailableBooks()

    def getContent(self, receiptGenerationDateAndTime, books):
        receiptContent = f'''
Thank you for your purchase!

Purchase date and time: {receiptGenerationDateAndTime}

Books: 

{newLine.join(map(str, books))}
        '''
        return receiptContent

    def generate(self, fileName, receiptGenerationDateAndTime):
        newFile = open(fileName, 'w')
        
        listOfPurchasedBooks = []
        for book in self.__availableBooksByLimit:
            for ID in self.__booksIdList:
                if book[0] == ID:
                    listOfPurchasedBooks.append(f'Book ID: {book[0]}, Title: {book[1]}, ISBN: {book[2]}, Author: {book[3]} Category: {book[4]}.')

        newFile.write(self.getContent(receiptGenerationDateAndTime, listOfPurchasedBooks))


def receipt(purchasedBooksIdList):
    current_purchasedBooksIdList = purchasedBooksIdList
    receiptGenerationDateAndTime = datetime.now().strftime("%d-%b-%Y %H::%M::%S")
    fileName = f'Receipt - {receiptGenerationDateAndTime}.txt'
    newReceipt = Receipt(current_purchasedBooksIdList)
    if confirm('\nDo you want specific name for generated receipt? [Yes/No or Y/N]: '):
        requestedFileName = input(
            'Please enter the name you want for the file: ')
        fileName = f'{requestedFileName}{fileName.replace("Receipt", "")}'
    
    newReceipt.generate(fileName, receiptGenerationDateAndTime)
    current_purchasedBooksIdList = []

    return current_purchasedBooksIdList

