from tkinter import *
from tkinter import messagebox
import sqlite3


class ChangeUserPass:

    def __init__(self):
        self.account_window = Tk()
        self.account_window.geometry('1280x700+100+80')
        self.account_window.title("Change Credentials")
        self.account_window.resizable(False, False)

        # Labels
        self.login_label = Label(self.account_window, text="Change Credential", font=20)
        self.login_label.place(x=603, y=200)
        self.user_name_label = Label(self.account_window, text="Current User Name")
        self.user_name_label.place(x=500, y=250)
        self.pass_label = Label(self.account_window, text="Current Password")
        self.pass_label.place(x=500, y=300)
        self.new_user_name_label = Label(self.account_window, text="New User Name")
        self.new_user_name_label.place(x=500, y=350)
        self.new_password_label = Label(self.account_window, text="New Password")
        self.new_password_label.place(x=500, y=400)

        # Entries
        self.user_name_entry = Entry(self.account_window, width=20)
        self.user_name_entry.place(x=630, y=250)
        self.pass_entry = Entry(self.account_window, width=20, show="•")
        self.pass_entry.place(x=630, y=300)
        self.new_user_name_entry = Entry(self.account_window, width=20)
        self.new_user_name_entry.place(x=630, y=350)
        self.new_password_entry = Entry(self.account_window, width=20, show="•")
        self.new_password_entry.place(x=630, y=400)

        # Button
        self.submit_button = Button(self.account_window, text="Save Changes", command=self.check_data)
        self.submit_button.place(x=600, y=450)

        self.account_window.mainloop()

    def check_data(self):
        user_name = self.user_name_entry.get()
        password = self.pass_entry.get()
        new_username = self.new_user_name_entry.get()
        new_password = self.new_password_entry.get()

        conn = sqlite3.connect("users.db")
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Users''')
        result = cur.fetchone()

        if result[0] == user_name and result[1] == password:
            cur.execute('''DROP TABLE Users''')
            cur.execute('''CREATE TABLE IF NOT EXISTS Users (username TEXT PRIMARY KEY, password TEXT)''')
            cur.execute('''INSERT INTO Users (username, password)
                                                    VALUES (?, ?)''', (new_username, new_password))
            conn.commit()
            conn.close()
        else:
            messagebox.showwarning("Warning!", "Incorrect username or password.")

        self.account_window.destroy()
