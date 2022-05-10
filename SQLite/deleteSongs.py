from dbConnect import *
import readSongs 
import time

def deleteSongs():
    idField = input('Enter the songID of the song to be deleted: ')
   
    cursor.execute("DELETE FROM songs WHERE song_id = " + idField)
    #method 2
    # cursor.execute(f"DELETE FROM songs WHERE SongID = {idField}")
    connection.commit()
    print(f"Record {idField} deleted")
    time.sleep(3)
    readSongs.readSongs() #name of file . name of subroutine
# deleteSongs()


# commit() Method. This method sends a COMMIT statement to the MySQL server, committing the current transaction. Since by default Connector/Python does not autocommit, it is important to call this method after every transaction that modifies data for tables that use transactional storage engines.

# cursor.execute()
# Allows Python code to execute PostgreSQL command in a database session. Cursors are created by the connection. cursor() method: they are bound to the connection for the entire lifetime and all the commands are executed in the context of the database session wrapped by the connection.