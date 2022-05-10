from dbConnect import *

# ...............................
cursor.execute("""
CREATE TABLE "songs" (
	"song_id"	INTEGER NOT NULL UNIQUE,
	"Title"	TEXT,
	"Artist"	TEXT,
	"Year"	INTEGER,
	PRIMARY KEY("song_id" AUTOINCREMENT)
)"""
)
# ...........................
