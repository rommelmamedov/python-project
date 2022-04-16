import sqlite3
from helpers import printErrorMessage, printInfoMessage, printSuccessMessage

def initializeDatabase():
    try:
        connection = sqlite3.connect('library.db')
        cursor = connection.cursor()
        statement = "CREATE TABLE IF NOT EXISTS books (ID number, Title text, Author text, ISBN number, Category text, UNIQUE (ID, ISBN) ON CONFLICT IGNORE)"
        cursor.execute(statement)

        cursor.execute("INSERT INTO books values(1, 'In Search of Lost Time', 'Marcel Proust', 142437964, 'Modernist')")
        cursor.execute("INSERT INTO books values(2, 'Ulysses', 'James Joyce', 1840226358, 'Modernist novel')")
        cursor.execute("INSERT INTO books values(3, 'Don Quixote', 'Miguel de Cervantes', 142437239, 'Novel')")
        cursor.execute("INSERT INTO books values(4, 'One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 60883286, 'Magic realism')")
        cursor.execute("INSERT INTO books values(5, 'The Great Gatsby', 'F. Scott Fitzgerald', 9780743273565, 'Tragedy')")
        cursor.execute("INSERT INTO books values(6, 'Moby Dick', 'Herman Melville', 1853260088, 'Epic')")
        cursor.execute("INSERT INTO books values(7, 'War and Peace', 'Lev Tolstoy', 1400079985, 'Novel')")
        cursor.execute("INSERT INTO books values(8, 'Hamlet', 'William Shakespeare', 9780743477123, 'Drama')")
        cursor.execute("INSERT INTO books values(9, 'The Odyssey', 'Homer', 393089053, 'Epic poetry')")
        cursor.execute("INSERT INTO books values(10, 'Madame Bovary', 'Gustave Flaubert', 9780679736363, 'Realist novel')")

        connection.commit()
        connection.close()

    except Exception as exception:
        printErrorMessage(exception, 'Database initialization error.')

def queryDataBaseByFieldName(field):
    try:
        connection = sqlite3.connect('library.db')
        cursor = connection.cursor()
        searchString = input(f'Please enter the {field}: ')
        cursor.execute(f"SELECT * FROM books WHERE {field} LIKE '%{searchString}%'")
        searchResult = []
        for row in cursor.fetchall():
             searchResult.append(list(row))

        connection.close()

        printInfoMessage('\n — — — — — — — — — — — — — — — — — — — — — — Search Results  — — — — — — — — — — — — — — — — — — — — —\n')
        for ID, title, author, ISBN, category in searchResult:
            printSuccessMessage(f'[ID: {ID}] Title: {title}, ISBN: {ISBN}, Author: {author} Category: {category}.')
        printInfoMessage('\n — — — — — — — — — — — — — — — — — — — — — — Search Results  — — — — — — — — — — — — — — — — — — — — —\n')


        return searchResult
    except Exception as exception:
        printErrorMessage(exception, 'Database initialization error.')

def getAvailableBooksByLimit(limit = 10):
    try:
        connection = sqlite3.connect('library.db')
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM books LIMIT {limit}")
        searchResult = []
        for row in cursor.fetchall():
             searchResult.append(list(row))

        connection.close()

        printInfoMessage(f'\n — — — — — — — — — — — — — — — — — — — — — — Top {limit} Books  — — — — — — — — — — — — — — — — — — — — —\n')
        for ID, title, author, ISBN, category in searchResult:
            printSuccessMessage(f'[ID: {ID}] Title: {title}, ISBN: {ISBN}, Author: {author} Category: {category}.')
        printInfoMessage(f'\n — — — — — — — — — — — — — — — — — — — — — — Top {limit} Books  — — — — — — — — — — — — — — — — — — — — —\n')


        return searchResult
    except Exception as exception:
        printErrorMessage(exception, 'Database initialization error.')
