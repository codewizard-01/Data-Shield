
class ProcessEncryption:
    def __init__(self, filename, key):
        self.file = open(filename, "rb")
        self.data = self.file.read()
        self.file.close()
        self.data = bytearray(self.data)
        for index, value in enumerate(self.data):
            self.data[index] = value ^ key

        self.file = open(filename, "wb")
        self.file.write(self.data)
        self.file.close()
