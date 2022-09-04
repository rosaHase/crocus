

from data.Screen import Screen
from data.Windows import Windows, textBar, canvas, buttonBar
from data.Buttons import Buttons
from data.Saund import Saund
from data.Control import Control

import time
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

screen = Screen()
screen.LINE = 1

control = Control()
control.timeout = 3

saund = Saund(
    [[60],[61],[60],[62, 60]],
    30
    )

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

win1 = Windows(screen)



win2 = Windows(screen)
c = canvas()

win3 = Windows(screen)
win3.win(2, 10, screen.halfX - 10, screen.halfY - 2)

win3.line = 1


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

text = [
    "hallo",
    "sdfhjijiowdcjiowjopkopsdckop",
    "sdfhj"
]
textKey = 0
textNum = 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

button = Buttons()

def start ():
    global screen
    screen.LINE = 0

button.add("start", start)
button.add("quit", quit)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def up():
    global button
    if not button.kursor -1 < 0:
        button.kursor -= 1

def down():
    global button
    if not button.kursor + 1 == len(button.List):
        button.kursor += 1

def enter():
    global screen, win3, button, textKey, textNum

    if screen.LINE == win3.line:
        
        button.klik()

    else:
        textNum = 0
        textKey += 1

control.addKey("esc", quit)
control.addKey("up", up)
control.addKey("down", down)
control.addKey("enter", enter)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


while True:

    if textKey == len(text):
        textKey = 0
        screen.LINE = 1

    a = ""

    if screen.LINE == 0:

        if textNum >= len(text[textKey]):
            if text[textKey][len(text[textKey]) - 1] == "#":
                a = text[textKey] + " "
            else:
                a = text[textKey] + "#"

        else:
            
            for i in range(textNum):
                a += text[textKey][i]

        textNum += 1


    win1.win(10, 136, 1, 37)
    

    textBar.addBar(win1, a)
    buttonBar.addBar(win3, button)
    c.gif(win2, 1, 1, "anim.json")
    screen.write()
    screen.update(control, win1, win2, win3, audio=saund)

    time.sleep(1/30)


    



    

    

    
    

    
        





