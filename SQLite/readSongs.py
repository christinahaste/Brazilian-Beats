from dbConnect import *

def readSongs():
    cursor.execute("SELECT * FROM songs") #select all songs
    row = cursor.fetchall() #fetches all data from songs table and passes it to row variable
    for record in row: #iterate through the row
        print(record) #print every record on its own line

# readSongs()
