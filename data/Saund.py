
import mido

port = mido.open_output('Microsoft GS Wavetable Synth 0')


class Saund():
    global port

    def __init__(self, melodiMas, timeout) -> None:
        "melodiMas = [[60], [61, 62]]"
        self.melodi = melodiMas
        self.timeout = timeout
        self.note = 0
        self.out = 0

    def play(self):



        for i in self.melodi[self.note]:

            port.send(mido.Message('note_on', note=i))
        
        self.out = 0
        self.note += 1

        self.out += 1

        if self.note == len(self.melodi):
            self.note = 0







