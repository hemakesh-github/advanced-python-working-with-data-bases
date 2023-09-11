#tables: authors, books, authorbooks
#authors: id,firstname, and last name
#books: id, title, number of pages
#author books: id, author id, book id
#add a new book, if author is new author should be updated,authors book should be updated
import psycopg2

def insert_data(cur, first_name, last_name, bookname):
    authornamecheck = list(cur.execute("SELECT * FROM authors WHERE first_name = %s AND last_name = %s", (first_name, last_name)))
    if len(authornamecheck) == 0:


conn = psycopg2.connect(database = "red30",
                        user = "postgres",
                        password = "hemakesh",
                        host = "localhost",
                        port = "5432")

cursor = conn.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS authors(id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, no_of_pages INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXITS authorbookd(id INT PRIMARY KEY, author_id, book_id, FOREIGN KEY(author_id) REFERENCES authors(id), FOREIGN KEY (book_id) REFERENCES books(id))")

books = [("Harry Potter and the Sorcerer's Stone", "J.K.Rowling"),("Harry Potter and the Half-Blood Prince", "J.K.Rowling"),("The Hobbit", "J.R.R. Tolkien")]

for book in books:
    insert_data(cursor, book[0], book[1])

