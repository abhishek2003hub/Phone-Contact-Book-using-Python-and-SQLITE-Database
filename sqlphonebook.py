import sqlite3
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('contact_book.db')
c = conn.cursor()

# Create table
c.execute('''
    CREATE TABLE contacts
    (ID INTEGER PRIMARY KEY,
    Name TEXT,
    Cell TEXT,
    Email TEXT)
''')
# Insert 5 rows of data
contacts = [
    (1, 'abhishek b', '1234567890', 'abhishek@example.com'),
    (2, 'deepa', '0987654321', 'deepa@example.com'),
    (3, 'keerthana', '1112223333', 'keerthana@example.com'),
    (4, 'gokul yadav', '4445556666', 'gokul.yadav@example.com'),
    (5, 'aishwerya', '7778889999', 'aishwerya@example.com'),
]
c.executemany('INSERT INTO contacts VALUES (?,?,?,?)', contacts)
# Commit the changes
conn.commit()
# Fetch all data
c.execute('SELECT * FROM contacts')
# Display all data
print('ID, Name, Cell#, E-mail')
for row in c.fetchall():
    print(row)
# Close the connection
conn.close()
