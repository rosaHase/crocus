
import json


def loadFile(name):
    with open(name, "r") as file:
        return json.load(file)


class Windows:

    def __init__(self, screen) -> None:
        self.WIN = screen.WIN
        self.screen = screen
        


    def win(self, height, width, x, y):

        
        a = []

        if (height) * (width) < 8:
            height = 1
            width = 8

        for i in range(height+2):
            
            a.append([])

            a[i].append("|")

            for j in range(width):
                if i == 0 or i == height+1:
                    a[i].append("-")
                else:
                    a[i].append(" ")

            a[i].append("|")


        self.line = 0
        self.BAR = a
        self.lenBar = [height, width]
        self.xy = [x, y]
                    
    def add(self):

        for i in range(self.lenBar[0]+2):

            for j in range(self.lenBar[1]+2):
                
                self.WIN[ i + self.xy[1] ][ j + self.xy[0] ] = self.BAR[i][j]

    def unadd(self):

        for i in range(self.lenBar[0]+2):

            for j in range(self.lenBar[1]+2):
                
                self.WIN[ i + self.xy[1] ][ j + self.xy[0] ] = "."


class buttonBar:


    def addBar(win, button):

        a = 0

        for i in button.List:

            for j in range(win.lenBar[1]):

                try:
                    if a == button.kursor and j == 0:
                        win.BAR[a+1][j+1] = ">"
                    elif j == 0:
                        win.BAR[a+1][j+1] = " "
                    win.BAR[a+1][j+2] = i[0][j]
                except:
                    pass
            
            a += 1

class textBar:


    def addBar(win, text):

        a = 0 + (win.line * win.lenBar[1])

        for i in range(win.lenBar[0]):

            for j in range(win.lenBar[1]):

                try:
                    if text[a] == "\n":
                        a += 1
                        break
                    else:
                        win.BAR[i+1][j+1] = text[a]
                        a += 1
                except:
                    pass

class menuBar:

    def addBar(win, menu):

        b = 0

        for i in menu.List:

            a = 0

            if b == menu.kursor:
                i[0] = i[0].lower()
                i[0] = i[0].upper()


            for j in i[2]:
  
                win.BAR[j[1]][j[0] + 1] = i[0][a]


                win.BAR[j[1]][j[0]] = i[0][a]

                a += 1

            b += 1
        
class canvas:

    def __init__(self) -> None:
        self.cadr = 0

    def gif(self, Windows, x, y, jsonGif):

        js = loadFile(jsonGif)

        win = Windows
        win.win(js["info"]["seting"][1], js["info"]["seting"][0], x, y)

        for i in range(len(win.BAR)):

            for j in range(len(win.BAR[i])):

                if not (i == 0 or i == len(win.BAR) - 1) and not (j == 0 or j == len(win.BAR[i]) - 1):
                    try:
                        win.BAR[i][j] = js["anim"][self.cadr][i-1][j-1]
                        a = js["anim"][self.cadr][i - 1][j - 1]
                    except:
                        pass
                    
                   
                else:
                    pass
                    
            
        self.cadr += 1
        if self.cadr == js["info"]["seting"][2]:
            self.cadr = 0

