# 32) Write a Python program to create a database and a table using SQLite3. 


import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect("college.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

print("Database and table created successfully.")

# Close connection
conn.close()