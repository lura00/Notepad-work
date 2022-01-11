import sqlite3


class Notepad:
    # initilize database (connecting)
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        self.create_table()

    # create a table
    def create_table(self):
        # Uncomment to delete table
        # self.c.execute("""DROP TABLE users""")
        self.c.execute("""CREATE TABLE IF NOT EXISTS user (
        name TEXT,
        job TEXT,
        notes TEXT,
        date DATE,
        user_id INTEGER PRIMARY KEY AUTOINCREMENT
        )""")
        self.conn.commit()

    # Insert data into table
    def insert(self, user):
        self.c.execute(
            """INSERT INTO user VALUES (?,?,?,?,NULL)""", user)
        self.conn.commit()

    # print out all data
    def show_all(self):
        self.c.execute("SELECT rowid, * FROM user")
        items = self.c.fetchall()

        for item in items:
            print(item)
        self.conn.commit()

    # This func will delete one entry
    def delete_one(self, id):
        self.c.execute("DELETE FROM user WHERE rowid = (?)", id)
        self.conn.commit()

    # Edit a entry in table.
    def edit_post(self, column, changed_data, id):
        self.c.execute(f"""UPDATE user SET '{column}' = '{changed_data}'
            WHERE rowid = {id}
            """)
        self.conn.commit()
