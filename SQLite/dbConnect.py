import sqlite3 #import sqlite module/library
from sqlite3 import Error

# create db
connection = sqlite3.connect('BrazilianBeats.db')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
songs(song_id INTEGER PRIMARY KEY, Title TEXT, Artist TEXT, Year TEXT)"""

cursor.execute(command1)

cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Acabou Chorare', 'Novos Baianos', '1972')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Tropicalia ou Panis et Circencis', 'Caetano Veloso', '1968')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Construção', 'Chico Buarque', '1971')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Chega de Saudade', 'João Gilberto', '1959')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Secos & Molhados', 'Secos & Molhados', '1973')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'A Tábua de Esmeralda', 'Jorge Ben', '1974')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Clube da Esquina', 'Milton Nascimento & Lô Borges', '1972')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Cartola', 'Cartola', '1976')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Os Mutantes', 'Os Mutantes', '1968')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Transa', 'Caetano Veloso', '1972')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Elis & Tom', 'Elis Regina and Tom Jobim', '1974')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Krig-ha, Bandolo!', 'Raul Seixas', '1973')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Da Lama ao Caos', 'Chico Science & Nação Zumbi', '1994')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Sobrevivendo no Inferno', 'Racionais MCs', '1997')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Samba Esquema Novo', 'Jorge Ben', '1963')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Fruto Proibido', 'Rita Lee & Tutti Frutti', '1975')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Racional', 'Tim Maia', '1975')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Afrociberdelia', 'Chico Science & Nação Zumbi', '1996')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Cabeça Dinossauro', 'Titãs', '1986')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Fa-Tal - Gal A Todo Vapor', 'Gal Costa', '1971')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Dois', 'Legião Urbana', '1986')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'A Divina Comédia ou Ando Meio Desligado', 'Os Mutantes', '1970')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Coisas', 'Moacir Santos', '1965')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Roberto Carlos Em Ritmo de Aventura', 'Roberto Carlos', '1967')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Tim Maia', 'Tim Maia', '1970')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Expresso 2222', 'Gilberto Gil', '1972')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Nós Vamos Invadir sua Praia', 'Ultraje a Rigor', '1985')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES ( 'Os Afro-Sambas', 'Baden Powell e Vinicius de Moraes', '1966')")
cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Year`) VALUES (  'A Dança da Solidão', 'Paulinho da Viola', '1972')")
