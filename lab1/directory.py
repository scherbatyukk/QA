class Directory:
    def __init__(self, dirName, maxElements = 0, father = None):
        self.DIR_MAX_ELEMS = maxElements
        self.name = dirName
        self.father = father
        self.elementsCount = 0
        self.fileList = []

    def __delete__(self):
        return

    def __listElements__(self):
        return
    
    def __move__(self, path):
        return