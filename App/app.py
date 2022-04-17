from tkinter import *
from PIL import Image,ImageTk
import copy
import os

c1,c2,c3,c4,c5 = '#2C4251','#D16666','#56CBF9','#A8C69F','#CCE2A3'

width,height = 800,800
def _create_circle(self,x,y,r,**kwargs):
   return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle

root=Tk()
canvas = Canvas(root,width=width,height=height,bg=c4)
canvas.pack()
goose = Image.open("HealthHonkLogo.png")
resize_geese = goose.resize((width//2,height//2))
img = ImageTk.PhotoImage(resize_geese)
#canvas.create_rectangle(0,0,width,height//2+height//8,fill=c4)
canvas.create_image(width//2,height//8, anchor=N, image=img)
#canvas.create_rectangle(0,height//2+height//8,height,width,fill="#2C4251")

hImg = Image.open("HomeButton.png").resize((120, 54))
aImg = Image.open("AboutImage.png").resize((120, 54))
rImg = Image.open("recordButton.png").resize((175, 175))
tImg = ImageTk.PhotoImage(Image.open("HealthHonkTitle.png").resize((350, 94)))
homeImage = ImageTk.PhotoImage(hImg)
aboutImage = ImageTk.PhotoImage(aImg)
recordImage = ImageTk.PhotoImage(rImg)


def goHome():
   homeButton = Button(root, image=homeImage, command=goHome)
   aboutButton = Button(root, image=aboutImage, command=goAbout)
   recordButton = Button(root, image=recordImage, command=record, borderwidth=0, fg='green')
   canvas.create_image(width // 2, height * (1 / 12), anchor=N, image=tImg)
   homeButton.place(x=10, y=10)
   aboutButton.place(x=150, y=10)
   recordButton.place(x=width // 2, y=height * (9 / 11), anchor=S)
   canvas.create_image(width // 2, height // 8, anchor=N, image=img)

def goAbout():
   canvas.delete('all')
   homeButton = Button(root, image=homeImage, command=goHome)
   aboutButton = Button(root, image=aboutImage, command=goAbout)
   homeButton.place(x=10, y=10)
   aboutButton.place(x=150, y=10)

def record():
   os.system("python3 App/main.py")


homeButton = Button(root, image=homeImage, command=goHome)
aboutButton = Button(root, image=aboutImage, command=goAbout)
recordButton = Button(root, image=recordImage, command=record, borderwidth=0, fg='green')
canvas.create_image(width // 2, height * (1 / 12), anchor=N, image=tImg)
homeButton.place(x=10, y=10)
aboutButton.place(x=150, y=10)
recordButton.place(x=width // 2, y=height * (9 / 11), anchor=S)

root.mainloop()
