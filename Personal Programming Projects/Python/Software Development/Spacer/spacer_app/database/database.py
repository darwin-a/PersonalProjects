import sqlite3
from sqlite3 import Error


class db:

    def __init__(self, name=None):
        """ create a database connection to a SQLite database """
        self.conn = None
        self.cursor = None

        if name:
            self.open_db(name)

    def open_db(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()
            print(sqlite3.version)
        except Error as e:
            print("Failed connecting to database...", e)

    def create_table(self, query):
        c = self.cursor
        print(query)
        c.execute(query)

    def edit_db(self, query):  # edit
        c = self.cursor
        c.execute(query)
        self.conn.commit()

    def edit_table_db(self, query, inserts):  # inserts
        c = self.cursor
        print(query, inserts)
        c.execute(query, inserts)
        self.conn.commit()

    def select_from_db(self, query):  # selection
        c = self.cursor
        c.execute(query)
        rows = c.fetchall()
        return rows


def main():
    test = db("test.db")


if __name__ == "__main__":
    main()
