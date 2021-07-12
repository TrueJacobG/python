class Manager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, trace):
        if self.file:
            self.file.close()


with Manager("name.txt") as file:
    file.write(":D")
