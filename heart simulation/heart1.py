from tkinter import Canvas, Tk, Frame
from math import cos, sin
from random import randint, choice

#cos i sin za računanje točaka na krivulji
#randint služi za dobivanje random boja
#choice služi da se odabere random char iz liste znakova (srca i zvjezdice)

class Heart(Frame):
    def __init__(self, master):
        super().__init__(master)
        #master u ovom slučaju je Tkinter prozor, u 11. liniji se 
        #inicijalizira Frame klasa koju nasljeđuje Heart klasa

        self.canvas = Canvas(master, bg = 'black')
        #za postavljanje tkinter platna u cijeli prozor
        self.canvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        

        self.objects = [] 
        self.counter = 0 #counter za praćenje objekata
        self.chars = ["♡", "♥", "ʚ♡ɞ", "★", "⚝" ]
        self.char = "★" #početni simbol

        self.create_obj()
        self.update()

    def create_obj(self):
        #napravi 200 objekata na Tkinter platnu i spremi ih se u objects[] listu
        for i in range(200):
            obj = self.canvas.create_text(0, 0, font = ('Arial', 24))
            self.canvas.coords(obj, 500, 250)
            self.objects.append(obj)

    def draw(self, obj, x, y, color, char):
        self.canvas.itemconfig(obj, fill = color, text = char)
        self.canvas.move(obj, x, y)

    def update(self):
        for t in range(0, 200, 1):
            #xp i yp su sam formule s interneta za oblik srca 
            xp = -1 * int(16 * pow(sin(t), 3))
            yp = -1 * int(13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t))
            color = f'#{randint(100, 255):02x}00{randint(100, 255):02x}'


            self.draw(self.objects[self.counter], xp, yp, color, self.char)

            xy = self.canvas.coords(self.objects[self.counter])

            self.counter += 1
            if self.counter >= 200:
                self.counter = 0
            if xy[0] >= 800: #provjerava jesu se objekti pomakli predaleko u horizontalnom smjeru
                self.char = choice(self.chars) #random bira novi simbol
                for s in range(200):
                    self.canvas.moveto(self.objects[s], 520, 270) #vraća objekte u centar
        
        self.master.after(100, self.update) #basically animacija

if __name__ == "__main__":
    root = Tk()
    root.title("Heart Animation")
    root.geometry('1280x720')
    app = Heart(root)
    app.mainloop()


#  /)/)
# ( . .)
# ( づ♡
