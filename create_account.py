from tkinter import *


def create_account():
    account_window = Tk()
    account_window.geometry('1280x700+100+80')
    account_window.resizable(False, False)

    # Labels
    login_label = Label(account_window, text="Sign Up", font=20)
    login_label.place(x=603, y=200)
    user_name_label = Label(account_window, text="User Name")
    user_name_label.place(x=500, y=250)
    pass_label = Label(account_window, text="Password")
    pass_label.place(x=500, y=300)

    # Entries
    user_name_entry = Entry(account_window, width=20)
    user_name_entry.place(x=570, y=250)
    pass_entry = Entry(account_window, width=20, show="•")
    pass_entry.place(x=570, y=300)

    def save_data():
        user_name = user_name_entry.get()
        password = pass_entry.get()
        file = open("metadata.txt", "w")
        file.write(user_name + "\n" + password)
        file.close()
        account_window.destroy()

    submit_button = Button(account_window, text="Submit", command=save_data)
    submit_button.place(x=600, y=350)

    account_window.mainloop()


create_account()

