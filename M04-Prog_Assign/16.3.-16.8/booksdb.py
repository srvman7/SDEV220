# 16.3 - 16.7 assignment.
import csv
import sqlite3

# Create a SQLite database and a books table
conn = sqlite3.connect("books.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    title text,
    author text,
    year integer
)
""")
conn.commit()

# Create a CSV file with books data
with open("books2.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["title", "author", "year"])
    writer.writerows([
        ["The Weirdstone of Brisingamen", "Alan Garner", 1960],
        ["Perdido Street Station", "China Miéville", 2000],
        ["Thud!", "Terry Pratchett", 2005],
        ["The Spellman Files", "Lisa Lutz", 2007],
        ["Small Gods", "Terry Pratchett", 1992]
    ])

# Read books data from the CSV file and insert into the books table
with open("books2.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        cursor.execute("""
        INSERT INTO books (title, author, year)
        VALUES (?,?,?)
        """, (row[0], row[1], row[2]))

conn.commit()

# Select and print the title column from the books table in alphabetical order
cursor.execute("SELECT title FROM books ORDER BY title")
rows = cursor.fetchall()
for row in rows:
    print(row[0])

conn.commit()

# Select and print columns from book table in order by publication
cursor.execute("SELECT * FROM books ORDER BY year")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()