This script will create a SQLite database file named contact_book.db in the same directory where the script is run. The contacts table in the database will have the fields ID, Name, Cell, and Email. It will insert 5 rows of data into the contacts table and then fetch and display all the data in the table.

Please replace the dummy data with your actual data before running the script. Also, make sure to handle the database operations properly in your production code to avoid any data loss or corruption. For example, you might want to add error handling code and close the database connection in a finally block to make sure it gets closed even if an error occurs.

Remember to install the sqlite3 module if it’s not already installed in your Python environment. You can install it using pip:

pip install pysqlite3
