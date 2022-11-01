# TODO: Compile to readable python files
import os

class Compiler:
    def __init__(self, text, target_path):
        self.text = text
        self.tpath = target_path
        self.file = None

    def __createFile(self):
        os.system(f"touch {self.tpath}")
        self.file = open(self.tpath, "w")

    def compile(self):
        self.__createFile()
        for x in range(len(self.text)):
            if self.text[x][0] == "OUT" and self.text[x+1][0] == "STR":
                self.file.write(f"print('{self.text[x+1][1]}');")
                #print(f'{self.text[x+1][1]}'.replace("\\", ""))
