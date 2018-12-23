a = ("test file.txt")


class FileOps():
    def Open(self):
        self = open(a, "r")
    def Read(self):
        self = FileOps.Open.read()


print(FileOps.Read(a))

