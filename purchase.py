from database import getAvailableBooksByLimit
from helpers import confirm,  getBookByID, printInfoMessage, printSuccessMessage


def makePurchase(purchase_list):
    current_purchase_list = purchase_list
    availableBooks = getAvailableBooksByLimit(10)
    current_purchase_list.append(getBookByID(availableBooks))

    if confirm('\nDo you want to confirm purchase and generate the receipt? [Yes/No or Y/N]: '):
        # updatedEmployees = updateEmployeeList(employeeDiscountNumber, currentEmployees, totalPurchased, totalDiscounts)
        printSuccessMessage(f"\nNew item purchase by employee with discount number: completed successfully.")
        printInfoMessage(f"\nTotal purchase amount is:.")

    if confirm('\nDo you want to make another purchase? [Yes/No or Y/N]: '):
        makePurchase(current_purchase_list)
    # else:
        # getAllEmployeesSummary(updatedEmployees)

    return

