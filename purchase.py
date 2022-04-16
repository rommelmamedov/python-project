from database import getAvailableBooks
from helpers import confirm,  getBookByID, printInfoMessage, printSuccessMessage


def purchase(purchasedBooksIdList):
    current_purchasedBooksIdList = purchasedBooksIdList
    availableBooks = getAvailableBooks()
    current_purchasedBooksIdList.append(getBookByID(availableBooks))

    if confirm('\nDo you want to confirm purchase? [Yes/No or Y/N]: '):
        printSuccessMessage(f"\nPurchase were successfully. IDs of purchased book: {current_purchasedBooksIdList}")
        printInfoMessage(f"\nYou can generate receipt file by choosing 3rd option from main menu.")

    if confirm('\nDo you want to make another purchase? [Yes/No or Y/N]: '):
        purchase(current_purchasedBooksIdList)

    return current_purchasedBooksIdList

