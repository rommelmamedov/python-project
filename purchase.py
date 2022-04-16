from database import getAvailableBooks
from helpers import confirm,  getBookByID, printInfoMessage, printSuccessMessage


def purchase(purchased_book_id_list):
    current_purchased_book_id_list = purchased_book_id_list
    availableBooks = getAvailableBooks()
    current_purchased_book_id_list.append(getBookByID(availableBooks))

    if confirm('\nDo you want to confirm purchase and generate the receipt? [Yes/No or Y/N]: '):
        printSuccessMessage(f"\nPurchase were successfully. Purchase book IDs: {current_purchased_book_id_list}")
        printInfoMessage(f"\nYou can generate receipt file by choosing 3rd option from main menu.")

    if confirm('\nDo you want to make another purchase? [Yes/No or Y/N]: '):
        purchase(current_purchased_book_id_list)

    return current_purchased_book_id_list

