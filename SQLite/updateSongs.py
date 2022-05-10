from dbConnect import *
import readSongs 
import time

def updateSongs():
    # songID to be updated 
    idField = input('Enter the songID of the song to be updated: ')
    # enter the name of the field to be updated 
    fieldName = input("Which field would you like to update: (Title, Artist, Genre)? ").title() #String title() Method, The title() method returns a copy of the string in which first characters of all the words are capitalized.
    # enter the value of the field name to be updated 
    newFieldValue = input(f"Enter the new value for {fieldName}: ")
    print(f"The new value {newFieldValue} has been entered")

    #add single quotes around the new field value
    newFieldValue = "'"+ newFieldValue +"'"
    print(f"The field value with added single quotes {newFieldValue}")

    #update songs set the field to fieldName(user entry(Title, Artist, Genre)) with the value = newFieldValue
    #WHERE songID = 4/2/1, etc.
    cursor.execute("UPDATE songs SET " + fieldName + "=" + newFieldValue + "WHERE SongID = "+ idField)
    connection.commit() #commit changes to db
    # if record == record :
    #then print (f"Record {idField} updated")
    # else :
    #print (f"The record doesn't exist)
    print(f"Record {idField} updated")
    time.sleep(3)
    readSongs.readSongs() #name of file . name of subroutine

# updateSongs()

