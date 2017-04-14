import tkinter
from tkinter import *

window = tkinter.Tk()
canvas = tkinter.Canvas(window,width=500,height=500)
canvas.grid()


class Arrow:
    def click(self, event):
        print("Click!")
        print(event)

    def __init__(self, color='red', direction='left'):
        self.color = color
        self.direction = direction
        if direction == 'left':
            self.a = 50,230
            self.b = 50,270
            self.c = 25,250
        else:
            self.a = 450,230
            self.b = 450,270
            self.c = 475,250
        self.idnumber = canvas.create_polygon(self.a,self.b,self.c,fill=self.color)
        canvas.tag_bind(self.idnumber, "<Button-1>", self.click)



arrow1 = Arrow()
arrow2 = Arrow(direction='right')
canvas.pack()


window.mainloop()
