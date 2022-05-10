from dbConnect import *
import time

#create a subroutine to add songs to table in c8MyMusicDB database
def addSongs():
    #create an empty list
    songs = list()
    # capture data input from the user 
    title = input("Enter song Title: ")
    artist = input("Enter Artist: ")
    year = input("Enter song Year: ")

    #append captured data to songs list
    #songs.songid is auto increment and would be added automatically
    "listName.append(dataCaptured)"
    songs.append(title)
    songs.append(artist)
    songs.append(year)

    #insert data from songs list into the songs table in c8MyMusicDB database
    cursor.execute("INSERT INTO songs VALUES(NULL,?,?,?)", songs)
    connection.commit() #commit/write changes to the table in the database permanently
    print(f"{title} added to songs table")
    time.sleep(3) #delay for 3 seconds before executing the next line of code

    #read data from table songs in c8MyMusicDB database
    cursor.execute("SELECT * FROM songs") #select all songs
    row = cursor.fetchall() #fetches all data from songs table and passes it to row variable
    for record in row: #iterate through the row
        print(record) #print every record on its own line
# addSongs() #call/invoke the function


