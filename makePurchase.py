from getAllEmployeesSummary import getAllEmployeesSummary
from helpers import confirm, getItemFromListByUniqueIdentifier, getValidIdentifier, printInfoMessage, printSuccessMessage, printWarningMessage

def updateEmployeeList(employeeDiscountNumber, currentEmployees, totalPurchased, totalDiscounts):
    updatedEmployees = []

    for employee in currentEmployees:
        if employeeDiscountNumber == employee[6]:
            employee[4] = totalPurchased
            employee[5] = totalDiscounts
    
    updatedEmployees = currentEmployees

    return updatedEmployees


def calculateCost(employee, item):
    maxTotalDiscount = 200
    maxYearlyPercentage = 10
    employeeType = employee[2]
    yearsWorked = employee[3]
    totalPurchased = employee[4]
    totalDiscounts = employee[5]

    totalYearBasedPercentage = yearsWorked * 2
    totalPercentage = 0
    if totalYearBasedPercentage > maxYearlyPercentage:
        totalPercentage = totalYearBasedPercentage - (totalYearBasedPercentage - maxYearlyPercentage)
    else:
        totalPercentage = totalYearBasedPercentage

    if employeeType == 'manager': totalPercentage += 10
    elif employeeType == 'hourly': totalPercentage += 2

    itemCost = item[2]
    totalPurchased += itemCost - (itemCost * totalPercentage / 100)
    totalDiscounts += itemCost * totalPercentage / 100
    return totalPurchased, totalDiscounts, maxTotalDiscount


def makePurchase(currentItems, currentEmployees):
    updatedEmployees = currentEmployees
    
    printInfoMessage('\n— — — — — — Items Summary — — — — — —')
    print('\nItem Number, Item Name, Item Cost\n')
    for itemNumber, itemName, itemCost in currentItems:
        print(f'{itemNumber}, {itemName}, ${itemCost:.2f}\n')
    printInfoMessage('— — — — — — Items Summary — — — — — —\n')
    
    employeeDiscountNumber = getValidIdentifier(currentEmployees, 6, 'employee discount number')
    if employeeDiscountNumber == 'no': return
    
    itemNumber = getValidIdentifier(currentItems, 0, 'item number')
    if itemNumber == 'no': return
    
    if confirm('\nDo you want to confirm purchase? [Yes/No or Y/N]: '):
        employee = getItemFromListByUniqueIdentifier(currentEmployees, employeeDiscountNumber, 6)
        item = getItemFromListByUniqueIdentifier(currentItems, itemNumber, 0)
        totalPurchased, totalDiscounts, maxTotalDiscount = calculateCost(employee, item)
        
        if totalDiscounts > maxTotalDiscount:
            printWarningMessage(f"\nSorry employee with discount number: '{employeeDiscountNumber}' is not allowed to make this purchase. No discount allowed once you have received $200 discount. After this purchase calculated discount amount will be: ${totalDiscounts:.2f}.")
        else:
            updatedEmployees = updateEmployeeList(employeeDiscountNumber, currentEmployees, totalPurchased, totalDiscounts)
            printSuccessMessage(f"\nNew item purchase by employee with discount number: '{employeeDiscountNumber}' for the item with number: '{itemNumber}' completed successfully.")
            printInfoMessage(f"\nTotal purchase amount is: ${totalPurchased:.2f}.")
            printInfoMessage(f"\nTotal discount amount is: ${totalDiscounts:.2f}.")

    if confirm('\nDo you want to make new purchase? [Yes/No or Y/N]: '):
        makePurchase(currentItems, currentEmployees)
    else: 
        getAllEmployeesSummary(updatedEmployees)
    
    return updatedEmployees

'''
----------------------UML-------------------
- Name: Book
- Properties: Title, Author, Price, ISBN
- Functionality or behavior : change_price()
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
