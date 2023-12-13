from tkinter import *
from PIL import ImageTk
from tkinter import filedialog
from encryption import ProcessEncryption


class Encrypt_Decrypt:

    def __init__(self):
        # The main window
        self.window = Tk()
        self.window.geometry('1280x700+100+80')
        self.window.resizable(False, False)

        # Background Photo
        self.backgroundImage = ImageTk.PhotoImage(file="Images/bg.jpg")
        self.bg_label = Label(self.window, image=self.backgroundImage)
        self.bg_label.place(x=0, y=0)

        self.loginFrame = Frame(self.window, bg="white", width=700, height=700, bd=10)
        self.loginFrame.place(x=450, y=200)

        # Background Image of the frame
        self.frame_bg = ImageTk.PhotoImage(file="Images/login.png")
        self.label_img = Label(self.loginFrame, image=self.frame_bg)
        self.label_img.place(x=0, y=0)

        # The image of the lock on the top of the frame
        self.logo = PhotoImage(file="Images/password.png")
        self.logo_ = Label(self.loginFrame, image=self.logo)
        self.logo_.pack(pady=30)

        # This is for creating a space between the two widgets
        self.label_next = Label(self.loginFrame, text="")
        self.label_next.pack(pady=15)

        # Encrypt Button
        self.encrypt_button = Button(self.loginFrame, text="Encrypt", bg="green", padx=30, pady=5,
                                     bd=5, command=self.encrypt_decrypt)
        self.encrypt_button.pack(pady=10, padx=135)

        # Decrypt Button
        self.decrypt_button = Button(self.loginFrame, text="Decrypt", bg="red", padx=30, pady=5, bd=5, command=self.encrypt_decrypt)
        self.decrypt_button.pack(pady=5)

        # This label is for creating a space between two widgets
        self.label = Label(self.loginFrame, text="")
        self.label.pack(pady=50)

        self.window.mainloop()

    def encrypt_decrypt(self):
        filename = filedialog.askopenfilename()
        ProcessEncryption(filename, key=25)





