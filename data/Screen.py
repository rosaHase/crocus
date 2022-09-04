from os import system
from time import sleep

class Screen():

    def __init__(self, fps = 25, height = 50, width = 140) -> None:

        self.fps = fps
        self.time = 0

        system(f"mode {width}, {height}")
        
        a = []
        for i in range(height):
            a.append([])
            for j in range(width):
                a[i].append(".")


        self.WIN = a
        self.bufs = [1, "", ""]
        self.counter = 0
        self.LINE = 0
        self.listMenuButton = []
        self.halfX = len(a[0]) // 2
        self.halfY = len(a) // 2

# ~ ~ ~ ~

# ~ ~ ~ ~

    def ret(self):

        a = []
        for i in range(len(self.WIN)):
            a.append([])
            for j in range(len(self.WIN[i])):
                a[i].append(".")
        self.WIN = a

# ~ ~ ~ ~


    def write(self):

        if not self.bufs[1] == self.bufs[2]:

            self.counter += 1

            print(self.bufs[self.bufs[0]], end="\r", flush=True)
            

            if self.bufs[0] == 1:
                self.bufs[0] = 2

            else:
                self.bufs[0] = 1

# ~ ~ ~ ~

    def update(self, control, *win, audio=0):

        for i in win:
            if i.line == self.LINE:
                i.add()
            else:
                i.unadd()
        
        if control.out == self.time:
        
            control.keyListen()
            control.out = self.time + control.timeout

        try:
            if audio.out == self.time:
                audio.play()
                audio.out = self.time + audio.timeout
            
        except:
            pass

        a = ""

        #self.ret()

        for i in self.WIN:

            for j in i:

                a += j

        self.bufs[self.bufs[0]] = a

        self.time += 1
