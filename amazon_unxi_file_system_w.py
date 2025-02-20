class File:
    def __init__(self,fileName, size):
        self.fileName = fileName
        self.size = size
        self.children = []
        self.isDir = False if "." in fileName else True
        self.extension = fileName.split(".")[-1]

from abc import ABC, abstractmethod

class Filter(ABC):
    @abstractmethod
    def filter(self):
        pass
class SizeFilter(Filter):
    def __init__(self,size):
        self.size = size

    def filter(self,file):
        return file.size == self.size

class FileType(Filter):
    def __init__(self,type):
        self.type = type
    def filter(self,file):
       return  self.type == file.extension

class File_system:
    def __init__(self):
        self.filter = []
    def addFilter(self):
        self.filter.append(filter)

    def applyORFilter(self,root):
        def dfs(root,result):
            if root.isDir:
                for child in root.children:
                    dfs(child,result)
            else:
                for filter in self.filter:
                    if filter.filer(root):
                        result.append(root)
                        return
        result = []
        dfs(root,result)

    def applyAndFilter(self,root):
        def dfs(root, result):
            if root.isDir:
                for child in root.children:
                    dfs(child, result)
            else:
                for filter in self.filter:
                    if  not filter.filer(root):
                        return
                result.append(root)


        result = []
        dfs(root, result)
