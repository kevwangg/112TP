import tkinter
from cmu_112_graphics import *
import startpage

def appStarted(app):
    app.image1 = app.loadImage('credits.png')
    app.credits = app.scaleImage(app.image1, 1)
    app.image2 = app.loadImage('back.png')
    app.back = app.scaleImage(app.image2, 0.8)
    app.image3 = app.loadImage('credits1.png')
    app.credits1 = app.scaleImage(app.image3, 0.6)
    app.image4 = app.loadImage('creditnames.png')
    app.credits2 = app.scaleImage(app.image4, 0.6)
    


def drawCredits(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='Light Blue')
    canvas.create_rectangle(0.03 * app.width, 0.85 * app.height, 
    0.15 * app.width, 0.97 * app.height, width='3')
    canvas.create_image(0.07 * app.width, 0.92 * app.height, image=ImageTk.PhotoImage(app.back))
    canvas.create_image(app.width//2, 0.15 * app.height, image = ImageTk.PhotoImage(app.credits))
    canvas.create_image(app.width//4, 0.4 * app.height, image = ImageTk.PhotoImage(app.credits1))
    canvas.create_image(0.75 * app.width, 0.4 * app.height, image=ImageTk.PhotoImage(app.credits2))



def mousePressed(app, event):
    if (0.03 * app.width <= event.x <= 0.15 * app.width) and (0.85 * app.height 
    <= event.y <= 0.97 * app.height):
        startpage.runStartPage()




def redrawAll(app, canvas):
    drawCredits(app, canvas)




def runCredits():
    runApp(width=2000, height=1000)










