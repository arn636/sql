# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

#create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

try:
    # insert data
    cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8400000")
    cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 8000000")

    # commit changes
    conn.commit()
except sqlite3.OperationalError as e:
    #print("Oops! Something went wrong. Try again...")
    print("SQLite Error: {}".format(e))

# close the DB connection
conn.close()
