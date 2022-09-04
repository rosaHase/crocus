class Buttons():

    def __init__(self) -> None:
        self.List = []
        self.kursor = 0
        pass
    

    def add(self, text, func):
        self.List.append([text, func])

    def klik(self):
        self.List[self.kursor][1]()


class Menu():

    def __init__(self) -> None:
        self.List = []
        self.kursor = 0
        pass
        

    def addButons(self, mas, buttons):
        """mas = [[x1,y1],[x2,y2]]"""

        a = 0

        for i in buttons.List:

            xy = []

            for j in range(len(i[0])):

                xy.append([mas[a][0] + j, mas[a][1]])

            self.List.append([i[0], i[1], xy])

            a += 1

    def klik(self):
        self.List[self.kursor][0][1]()



