import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

"""Basic queries SQLite"""
sql = "SELECT * FROM albums WHERE artist=?"
cursor.execute(sql, ["Red"])
print(cursor.fetchall())

print("Here's a listing of all the records in the table:")
for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
    print(row)

print("Results from a LIKE query:")
sql = "SELECT * FROM albums WHERE title LIKE 'The%'"
cursor.execute(sql)

print(cursor.fetchall())

"""Delete data"""
# sql = "DELETE FROM albums WHERE artist = 'John Doe'"
#
# cursor.execute(sql)
# conn.commit()

"""Update date"""
# sql = """
#     UPDATE albums
#     SET artist = 'John Doe'
#     WHERE artist = 'Andy Hunter'
#     """
#
# cursor.execute(sql)
# conn.commit()

"""Insert data in the table"""
# cursor.execute("""INSERT INTO albums
#                 VALUES ('Glow', 'Andy Hunter', '7/24/2012',
#                 'Xplore Records', 'MP3')
#                 """)

"""Save changes"""
# conn.commit()

"""We insert a lot of data into the table using the safe method '?'."""
# albums = [
#     ('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
#     ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
#     ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
#     ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')
# ]
# cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
# conn.commit()

"""Create table"""
# cursor.execute("""CREATE TABLE albums
#                 (title text, artist text, release_date text,
#                 publisher text, media_type text)
#                 """)
