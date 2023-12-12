from tkinter import *
from PIL import ImageTk


# The main window
window = Tk()
window.geometry('1280x700+100+80')
window.resizable(False, False)


# Encryption and Decryption of the file
def Encrypt():
    import encrypt

def Decrypt():
    import decrypt


# Background Photo
backgroundImage = ImageTk.PhotoImage(file="Images/bg.jpg")
bg_label = Label(window, image=backgroundImage)
bg_label.place(x=0, y=0)

# Login Frame
loginFrame = Frame(window,bg="white", width=700, height=700, bd=10)
loginFrame.place(x=450, y=200)

# Background Image of the frame
frame_bg = ImageTk.PhotoImage(file="Images/login.png")
label_img = Label(loginFrame, image=frame_bg)
label_img.place(x=0, y=0)

# The image of the lock on the top of the frame
logo = PhotoImage(file="Images/password.png")
logo_ = Label(loginFrame, image=logo)
logo_.pack(pady=30)

# This is for creating a space between the two widgets
label_next = Label(loginFrame, text="")
label_next.pack(pady=15)

# Encrypt Button
encrypt_button = Button(loginFrame, text="Encrypt", bg="green", padx=30, pady=5, bd=5, command=Encrypt)
encrypt_button.pack(pady=10, padx=135)

# Decrypt Button
decrypt_button = Button(loginFrame, text="Decrypt", bg="red", padx=30, pady=5, bd=5, command=Decrypt)
decrypt_button.pack(pady=5)

# This label is for creating a space between two widgets
label = Label(loginFrame, text="")
label.pack(pady=50)


window.mainloop()


