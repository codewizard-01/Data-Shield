from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def login():
    filename = open("metadata.txt", "r")

    # List for keeping the username and password
    metadata = []
    data = filename.readline()
    while data != "":
        metadata.append(data.strip("\n"))
        data = filename.readline()

    user_name = metadata[0]
    password = metadata[1]

    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror("Error", 'fields cannot be empty')
    elif usernameEntry.get() == user_name and passwordEntry.get() == password:
        window.destroy()
        import login
    else:
        messagebox.showerror('Error', 'Please enter correct credentials')

def signup():
    import create_account


# Main Window
window = Tk()
window.geometry('1280x700+100+80')
window.resizable(False, False)

# Background Image
background_image = ImageTk.PhotoImage(file="Images/bg.jpg")
bg_label = Label(window, image=background_image)
bg_label.place(x=0, y=0)

# Login Frame
loginFrame = Frame(window, bg='white')
loginFrame.place(x=400, y=150)

# The first image at the top of the frame
logoImage = PhotoImage(file='Images/student.png')
logo_label = Label(loginFrame, image=logoImage)
logo_label.grid(row=0, column=1)

# The image for username
UsernameImage = PhotoImage(file='Images/user.png')
Username_label = Label(loginFrame, image=UsernameImage, text='Username'
                     ,compound=LEFT, font=('times new roman', 20, 'bold'), bg='white')
Username_label.grid(row=1, column=0)

# Username Entry
usernameEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5)
usernameEntry.grid(row=1, column=1, pady=10, padx=20)

# The image for password label
passwordImage = PhotoImage(file='Images/password.png')
password_label = Label(loginFrame, image=passwordImage, text='password'
                    ,compound=LEFT, font=('times new roman', 20, 'bold'), bg='white')
password_label.grid(row=2, column=0)

# Password Entry
passwordEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, show="•")
passwordEntry.grid(row=2, column=1, pady=10, padx=20)

# The Login Button
loginButton = Button(loginFrame, text="Login", font=('times new roman', 14, 'bold'), width=15,
                   fg='white', bg='cornflowerblue'
                   ,activebackground='green', activeforeground='white', cursor='hand2', command=login)
loginButton.grid(row=3, column=1)

# The Signup Button
signup_button = Button(loginFrame, text="Don't have account?", padx=29, activebackground='green',
                       activeforeground='white', cursor='hand2', command=signup)
signup_button.grid(row=4, column=1, pady=10)


window.mainloop()
