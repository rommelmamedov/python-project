def printErrorMessage(message):
    print('\033[91m' + message + '\033[0m')

def printSuccessMessage(message):
    print('\033[92m' + message + '\033[0m')

def printWarningMessage(message):
    print('\033[93m' + message + '\033[0m')

def printInfoMessage(message):
    print('\033[94m' + message + '\033[0m')

# Reusable confirmation function
def confirm(message):
    choice = input(message).strip().lower()
    while True:
        if choice in ['yes', 'y']: return True
        elif choice in ['no', 'n']: return False
        else: 
            printWarningMessage("Please respond with 'Yes/Y' or 'No/N'")
            return confirm(message)

def goToMenu():
    return confirm('\nDo you want to go back into main menu? [Yes/No or Y/N]: ')

def getValidIntegerValue(prompt, fieldName):
    inputValue = input(prompt).strip()
    # Condition to checks if user entered numberic value.
    if inputValue.isnumeric():
        return int(inputValue)
    else:
        printErrorMessage(f"Please provide a valid interger value for {fieldName}.")
        return getValidIntegerValue(prompt, fieldName)    

def getValidAndUniqueValue(list, fieldIndex, fieldName):
    value = getValidIntegerValue(f'Please input {fieldName}: ', fieldName)

    for item in list:
        if value == item[fieldIndex]:
            printWarningMessage(f"{fieldName.capitalize()}: '{value}' already exists in the list. Please provide unique value for {fieldName}.")
            return getValidAndUniqueValue(list, fieldIndex, fieldName)

    return value

# Recursive function to get valid and unique value from user.
def getBookByID(list):
    idIndex = 0
    value = getValidIntegerValue(f'Please select ID of the book you want to purchase: ', 'book ID')
    
    for item in list:
        if value == item[idIndex]: return value
        else: continue

    printWarningMessage(f"Book with does not exists in the database. Please correct value for book ID.")
    return getBookByID(list, idIndex)