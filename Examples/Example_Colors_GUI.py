
#!/usr/bin/env python
from Tkinter import *

root = Tk() #Makes the window
root.wm_title("Colors and Buttons") #Makes the title that will appear in the top left
root.config(background = "#FFFFFF")


def redCircle():
    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='red')
    colorLog.insert(0.0, "Red\n")

def yelCircle():
    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='yellow')
    colorLog.insert(0.0, "Yellow\n")

def grnCircle():
    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='green')
    colorLog.insert(0.0, "Green\n")

def blueCircle():
    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='blue')
    colorLog.insert(0.0, "Blue\n")

def blackCircle():
    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='black')
    colorLog.insert(0.0, "Black\n")

#Left Frame and its contents
leftFrame = Frame(root, width=200, height = 600)
leftFrame.grid(row=0, column=0, padx=10, pady=2)

Label(leftFrame, text="Instructions:").grid(row=0, column=0, padx=10, pady=2)

Instruct = Label(leftFrame, text="Press a button\n2\n2\n3\n4\n")
Instruct.grid(row=1, column=0, padx=10, pady=2)

try:
    imageEx = PhotoImage(file = 'image.gif')
    Label(leftFrame, image=imageEx).grid(row=2, column=0, padx=10, pady=2)
except:
    print("Image not found")

#Right Frame and its contents
rightFrame = Frame(root, width=200, height = 600)
rightFrame.grid(row=0, column=1, padx=10, pady=2)

InstructR = Label(rightFrame, text="Welcome Aborad")
InstructR.grid(row=0, column=1, padx=10, pady=2)

circleCanvas = Canvas(rightFrame, width=100, height=100, bg='white')
circleCanvas.grid(row=0, column=0, padx=10, pady=2)

btnFrame = Frame(rightFrame, width=200, height = 200)
btnFrame.grid(row=1, column=0, padx=10, pady=2)

colorLog = Text(rightFrame, width = 30, height = 10, takefocus=0)
colorLog.grid(row=2, column=0, padx=10, pady=2)

redBtn = Button(btnFrame, text="Red", command=redCircle)		#Donde, texto, Def previamente creada
redBtn.grid(row=0, column=0, padx=10, pady=2)					#Fila, Columna, Separacion

yellowBtn = Button(btnFrame, text="Yellow", command=yelCircle)
yellowBtn.grid(row=0, column=1, padx=10, pady=2)

greenBtn = Button(btnFrame, text="Green", command=grnCircle)
greenBtn.grid(row=0, column=2, padx=10, pady=2)

blueBtn = Button(btnFrame, text="Blue", command=blueCircle)
blueBtn.grid(row=0, column=3, padx=10, pady=2)

blkBtn = Button(btnFrame, text="Black", command=blackCircle)
blkBtn.grid(row=0, column=4, padx=10, pady=2)


root.mainloop() #start monitoring and updating the GUI
