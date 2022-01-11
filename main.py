from models import Notepad
from datetime import datetime

# # c.execute("""CREATE TABLE users (name text, work text, notes text)""")
# class User_model:
#     __tablename__ = "users"
#     first_name = Column(String, nullable=False)
#     job = Column(String, nullable=False)
#     notes = Column(String, nullable=True)
#     created_at = Column(TIMESTAMP(timezone=True),
#                         nullable=False, server_default=text('now()'))
# class User_post:
#     def __init__(self, name, job, notes):
#         self.name = name
#         self.job = job
#         self.notes = notes
today = datetime.today().strftime('%Y-%m-%d')

db = Notepad()
db.create_table()


def show_menu():
    print("\n===========================================================")
    print("|                        Welcome                          |")
    print("|               This is simply a guestbook                |")
    print("|               Would you like to add a post? press .1    |")
    print("|               Or perhaps see all posts? press .2        |")
    print("|               Edit post? press .3                       |")
    print("|               Delete post? press .4                     |")
    print("|               Exit, press .5                            |")
    print("===========================================================")

# Add a new record to the table


# def add_one(name, job, notes):
#     conn = sqlite3.connect('database.db')
#     c = conn.cursor()
# #     c.execute("""CREATE TABLE users (
# #      first_name text,
# #      job text,
# #      notes text
# #  )""")
#     new_data = User_model(name, job, notes)
#     user = user_post(name, job, notes)
#     c.execute("INSERT INTO users VALUES (?,?,?)", (new_data))
#     conn.commit()
#     conn.close()


# c.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(c.fetchall())
# conn.commit()
# conn.close()


# def show_all():

#     conn = sqlite3.connect('database.db')
#     c = conn.cursor()
#     c.execute("SELECT rowid, * FROM users")
#     items = c.fetchall()

#     for item in items:
#         print(item)
#     conn.commit()
#     conn.close()


# def delete_one(id):
#     conn = sqlite3.connect('database.db')
#     c = conn.cursor()
#     c.execute("DELETE FROM users WHERE rowid = (?)", id)
#     conn.commit()
#     conn.close()


# def edit_post(column, changed_data, id):
#     conn = sqlite3.connect('database.db')
#     c = conn.cursor()
#     c.execute(f"""UPDATE users SET '{column}' = '{changed_data}'
#         WHERE rowid = {id}
#         """)
#     conn.commit()
#     conn.close()


while True:

    show_menu()
    choice = int(input("Make our choice: 1 - 5: "))

    if choice == 1:
        name = input("Enter your name: ")
        work = input("What do you work with? ")
        notes = input("Enter your own thoughts about your work: ")
        user = (name, work, notes, today)
        db.insert(user)

    elif choice == 2:
        db.show_all()

    elif choice == 3:
        column = input(
            "What column do you want to edit? First_name, job or notes? ")
        data = input("What is the new data? ")
        id = input("Enter the row ID ")
        db.edit_post(column, data, id)

    elif choice == 4:
        delete_user_id = input("Enter id of user to be deleted: ")
        db.delete_one(delete_user_id)

    elif choice == 5:
        print("Thank you for using my app, your notes have been saved, come back any time!")
        break
    else:
        print("==>Now something went a little bit wrong, try another number<==")
