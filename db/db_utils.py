from db.database import Database

# Create database bookDb
db = Database("bookDb")

sql_books_table = """ CREATE TABLE IF NOT EXISTS books (
                        id integer PRIMARY KEY,
                        title text NOT NULL,
                        author text NOT NULL,
                        publication_year text NOT NULL,
                        genre text NOT NULL,
                        personal_rating integer NOT NULL
                  ); """
insert_form_entry = """ INSERT INTO books (id, title, author, publication_year, genre, personal_rating)
                        VALUES (?, ?, ?, ?, ?, ?);
                    """
sql_select_all = """ SELECT * FROM books; """


def run_db_commands():
    db.create_connection()
    # Checks if DB is valid
    db.check_database()
    # Create books table in DB
    db.create_table(sql_books_table)


def insert_entry(entry_items):
    cursor = db.conn.cursor()
    cursor.execute(insert_form_entry, entry_items)
    print('Entries inserted into table.')
    db.conn.commit()


def print_table():
    cursor = db.conn.cursor()
    cursor.execute(sql_select_all)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    db.conn.commit()


def close_db_connection():
    # Closes DB Connection
    db.close_connection()
