from tkinter import *
from tkinter import messagebox
import sqlite3


class Account:

    def __init__(self):
        self.account_window = Tk()
        self.account_window.geometry('1280x700+100+80')
        self.account_window.title("Create Account")
        self.account_window.resizable(False, False)

        # Labels
        self.login_label = Label(self.account_window, text="Sign Up", font=20)
        self.login_label.place(x=603, y=200)
        self.user_name_label = Label(self.account_window, text="User Name")
        self.user_name_label.place(x=500, y=250)
        self.pass_label = Label(self.account_window, text="Password")
        self.pass_label.place(x=500, y=300)

        # Entries
        self.user_name_entry = Entry(self.account_window, width=20)
        self.user_name_entry.place(x=570, y=250)
        self.pass_entry = Entry(self.account_window, width=20, show="•")
        self.pass_entry.place(x=570, y=300)

        # Button
        self.submit_button = Button(self.account_window, text="Submit", command=self.save_data)
        self.submit_button.place(x=600, y=350)

        self.account_window.mainloop()

    def save_data(self):
        user_name = self.user_name_entry.get()
        password = self.pass_entry.get()

        conn = sqlite3.connect("users.db")
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Users''')
        result = cur.fetchone()
        conn.close()

        if result[0] == user_name and result[1] == password:
            messagebox.showinfo("Warning!", "An account with this username and password exists.")
        else:
            messagebox.showwarning("Warning!", "You cannot create an account. An account already exists."
                                               " Please type the correct username and password.")
        self.account_window.destroy()
