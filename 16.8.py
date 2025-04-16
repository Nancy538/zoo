import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect('books.db')
c = conn.cursor()


# Example data
books = [
    ('The Catcher in the Rye', 'J.D. Salinger', 1951),
    ('To Kill a Mockingbird', 'Harper Lee', 1960),
    ('1984', 'George Orwell', 1949)
]

# Insert data
c.executemany('INSERT INTO books VALUES (?, ?, ?)', books)

# Save and close
conn.commit()
conn.close()

from sqlalchemy import create_engine, MetaData, Table, select

# Connect to SQLite database
engine = create_engine('sqlite:///books.db')
connection = engine.connect()

# Reflect the table
metadata = MetaData()
books = Table('books', metadata, autoload_with=engine)

# Create and execute query
stmt = select(books.c.title).order_by(books.c.title)
results = connection.execute(stmt)

# Print results
for row in results:
    print(row.title)

connection.close()
