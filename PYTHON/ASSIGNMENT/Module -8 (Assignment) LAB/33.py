# 33) Write a Python program to insert data into an SQLite3 database and fetch it.


import sqlite3

# Connect to database
conn = sqlite3.connect("college.db")

# Create cursor
cursor = conn.cursor()

# Create table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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