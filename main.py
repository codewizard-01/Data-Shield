from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from create_account import Account
from action_page import EncryptDecrypt
from change_credentials import ChangeUserPass
import sqlite3


class MainPage:

    def __init__(self):
        # Main Window
        self.window = Tk()
        self.window.geometry('1280x700+100+80')
        self.window.title("Data Shield")
        self.window.resizable(False, False)

        # Background Image
        self.background_image = ImageTk.PhotoImage(file="Images/bg.jpg")
        self.bg_label = Label(self.window, image=self.background_image)
        self.bg_label.place(x=0, y=0)

        self.loginFrame = Frame(self.window, bg='white')
        self.loginFrame.place(x=400, y=150)

        # The first image at the top of the framec
        self.logoImage = PhotoImage(file='Images/student.png')
        self.logo_label = Label(self.loginFrame, image=self.logoImage, bg="white")
        self.logo_label.grid(row=0, column=1)

        # The image for the username label
        self.UsernameImage = PhotoImage(file='Images/user.png')
        self.Username_label = Label(self.loginFrame, image=self.UsernameImage, text='Username', compound=LEFT,
                                    font=('Sans-serif', 20, 'bold'), bg='white')
        self.Username_label.grid(row=1, column=0)

        # The image for the password label
        self.passwordImage = PhotoImage(file='Images/password.png')
        self.password_label = Label(self.loginFrame, image=self.passwordImage, text='Password', compound=LEFT,
                                    font=('Sans-serif', 20, 'bold'), bg='white')
        self.password_label.grid(row=2, column=0)

        # Entries
        self.usernameEntry = Entry(self.loginFrame, font=('Times New Roman', 20, 'normal'), bd=5)
        self.usernameEntry.grid(row=1, column=1, pady=10, padx=20)
        self.passwordEntry = Entry(self.loginFrame, font=('Times New Roman', 20, 'normal'), bd=5, show="•")
        self.passwordEntry.grid(row=2, column=1, pady=10, padx=20)

        # Buttons
        self.loginButton = Button(self.loginFrame, text="Login", font=('Sans-serif', 14, 'bold'), width=15,
                                  fg='white', bg='cornflowerblue', activebackground='green', activeforeground='white',
                                  cursor='hand2', command=self.login)
        self.loginButton.grid(row=3, column=1)
        self.signup_button = Button(self.loginFrame, text="Don't have account?", padx=36, activebackground='green',
                                    cursor='hand2', command=self.signup)
        self.signup_button.grid(row=4, column=1, pady=10)
        self.change_user_pass = Button(self.loginFrame, text="Change Password", padx=42, activebackground="red",
                                       cursor="hand2", command=self.change_credential)
        self.change_user_pass.grid(row=5, column=1)

        self.window.mainloop()

    def login(self):

        # Connect to database
        conn = sqlite3.connect("users.db")
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Users''')
        result = cur.fetchone()
        user_name = result[0]
        password = result[1]
        conn.close()

        # Password and username validation check
        if self.usernameEntry.get() == '' or self.passwordEntry.get() == '':
            messagebox.showerror("Error", 'fields cannot be empty')
        elif self.usernameEntry.get() == user_name and self.passwordEntry.get() == password:
            self.window.destroy()
            EncryptDecrypt()
        else:
            messagebox.showerror('Error', 'Please enter correct credentials')

    def signup(self):
        Account()

    def change_credential(self):
        ChangeUserPass()


show_main_page = MainPage()
