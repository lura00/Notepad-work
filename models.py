import sqlite3


class Notepad:
    # initilize database (connecting)
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        # create memory
        self.conn = sqlite3.connect(':memory:')

        # create a cursor
        self.c = self.conn.cursor()

    # create a table
    def create_table(self):
        #self.c.execute("""DROP TABLE users""")
        self.conn = sqlite3.connect('database.db')
        self.c.execute("""CREATE TABLE IF NOT EXISTS user (
        name TEXT,
        job TEXT,
        notes TEXT,
        date DATE,
        user_id INTEGER PRIMARY KEY AUTOINCREMENT
        )""")
        self.conn.commit()
        # self.conn.close()

    # Insert data into table
    def insert(self, user):
        self.conn = sqlite3.connect('database.db')
        self.c.execute(
            """INSERT INTO user VALUES (?,?,?,?,NULL)""", user)
        self.conn.commit()
        # self.conn.close()

    # print out all data
    def show_all(self):
        self.conn = sqlite3.connect('database.db')
        self.c.execute("SELECT rowid, * FROM user")
        items = self.c.fetchall()

        for item in items:
            print(item)
        self.conn.commit()
        # self.conn.close()

    def delete_one(self, id):
        self.conn = sqlite3.connect('database.db')
        self.c.execute("DELETE FROM user WHERE rowid = (?)", id)
        self.conn.commit()
        # self.conn.close()

    def edit_post(self, column, changed_data, id):
        self.conn = sqlite3.connect('database.db')
        self.c.execute(f"""UPDATE user SET '{column}' = '{changed_data}'
            WHERE rowid = {id}
            """)
        self.conn.commit()
        # self.conn.close()
