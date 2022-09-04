from keyboard import is_pressed
from time import sleep


class Control():

    def __init__(self) -> None:
        self.keyList = []
        self.timeout = 3
        self.out = 0

    def addKey(self, key, func):
        self.keyList.append([key, func])

    def keyListen(self):
        for i in self.keyList:
            
            if is_pressed(i[0]):

                i[1]()
            

