# 31) Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data. 


import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("student.db")

# Create cursor object
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Insert data
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)", ("Kaif", 23))
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)", ("Ali", 22))

# Save changes
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

# Display data
print("Student Records:")
for row in rows:
    print(row)

# Close connection
conn.close()