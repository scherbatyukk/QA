class BufferFile:
    def __init__(self, maxSize, fileName, father):
        self.MAX_BUF_FILE_SIZE = maxSize
        self.file_name = fileName
        self.father = father
        self.info = []

    def __delete__(self):
        return

    def __move__(self, path):
        return

    def __push__(self, elem):
        return

    def __consume__(self):
        return