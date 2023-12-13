from tkinter import filedialog


def encrypt_decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open(filename, "wb")
    file.write(data)
    file.close()


filename = filedialog.askopenfilename()
encrypt_decrypt(filename, key = 25)
