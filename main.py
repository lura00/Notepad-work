from models import Notepad
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

db = Notepad()
# db.create_table()


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
