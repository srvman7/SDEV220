from datetime import date, datetime

# 13.1 - Write the current date as a string to the text file today.txt
today = date.today().strftime('%d-%m-%Y')
with open("today.txt", "w") as file:
    file.write(today)

# 13.2 - Read the text file today.txt into the sting "today_string".
with open("today.txt", "r") as file:
    today_string = file.read()

# 13.3 - Parse the date from the today_string.
today = datetime.strptime(today_string, "%d-%m-%Y").date()

# 16.8 - Use the sqlalchemy module to connect to books.db.
import sqlalchemy as sa

conn = sa.create_engine('sqlite:///books.db')

conn.execute('''CREATE TABLE books
...     (title VARCHAR(20),
...      author VARCHAR(20),
...      year INTEGER''')

ins = 'INSERT INTO books (title, author, year) VALUES (?, ?, ?)'

conn.execute(ins, "The Weirdstone of Brisingamen", "Alan Garner", 1960)
conn.execute(ins, "Perdido Street Station", "China Miéville", 2000)
conn.execute(ins, "Thud!", "Terry Pratchett", 2005)
conn.execute(ins, "The Spellman Files", "Lisa Lutz", 2007)
conn.execute(ins, "Small Gods", "Terry Pratchett", 1992)

rows = conn.execute('SELECT * FROM books')

print(rows)