from asyncio import SendfileNotAvailableError
from dbConnect import *
import readSongs 
import time

def searchSong():
   
    searchField = input('Which field would you like to search for(Title,Artist,Year?): ').title()
    searchValue = input(f"Enter the value for the {searchField} you want to search:  ").title()
    print(f"The search value entered is {searchValue}")

    #add single quotes around the new field value
    searchValue = "'"+ searchValue +"'"
    print(f"Amended search value {searchValue}")
    
    #search database 
    cursor.execute("SELECT * FROM songs WHERE " + searchField + "=" + searchValue)
    connection.commit()
    time.sleep(3)

    row = cursor.fetchall() #fetch all of the record and hold it in row
    #convert/cast(row) to a string data type
    strRow = str(row)
    if searchValue in strRow:
        for record in row:
            print(record)
    else:
        print(f"the field {searchField} does not contain a {searchValue} in the database")

# searchSong()
