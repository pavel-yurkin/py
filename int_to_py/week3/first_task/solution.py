
class FileReader:

    def __init__(self, path):
        self.path = path
        self.output = str

    def read(self):
        try:
            with open(self.path, "r") as f:
                self.output = f.read()
        except FileNotFoundError:
            self.output = ''
        return self.output


