from helpers import confirm, getValidNameFieldValue, getValidNumericValue, getValidAndUniqueValue, printSuccessMessage, printInfoMessage

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