import tkinter
from cmu_112_graphics import *
import startpage



def appStarted(app):
    app.page = 0
    app.image1 = app.loadImage('instructions.png')
    app.instructiontext = app.scaleImage(app.image1, 2)
    app.image2 = app.loadImage('howtoplay.png')
    app.howtoplay = app.scaleImage(app.image2, 0.6)
    app.image3 = app.loadImage('controls.png')
    app.controls = app.scaleImage(app.image3, 0.6)
    app.image4 = app.loadImage('modes.png')
    app.modes = app.scaleImage(app.image4, 0.6)
    app.image5 = app.loadImage('page1.png')
    app.page1 = app.scaleImage(app.image5, 0.8)
    app.image6 = app.loadImage('page2.png')
    app.page2 = app.scaleImage(app.image6, 0.8)
    app.image7 = app.loadImage('page3.png')
    app.page3 = app.scaleImage(app.image7, 0.8)
    app.instructionsList = [(app.howtoplay, app.page1), (app.controls, app.page2), (app.modes, app.page3)]
    app.image8 = app.loadImage('back.png')
    app.back = app.scaleImage(app.image8, 0.8)

def drawInstructions(app, canvas):
    horizmid = app.width // 2
    vertmid = app.height // 2
    canvas.create_rectangle(0, 0, app.width, app.height, fill='Light Blue')
    canvas.create_image(app.width//2, 0.15 * app.height, image=ImageTk.PhotoImage(app.instructiontext))
    canvas.create_image(horizmid + 0.02*horizmid, vertmid, 
    image=ImageTk.PhotoImage(app.instructionsList[abs(app.page) % 3][0]) )
    canvas.create_rectangle(0.03 * app.width, 0.85 * app.height, 
    0.15 * app.width, 0.97 * app.height, width='3')
    canvas.create_image(0.9 * app.width, app.height + 0.1 * vertmid, 
    image=ImageTk.PhotoImage(app.instructionsList[abs(app.page) % 3][1]))
    canvas.create_image(0.07 * app.width, 0.92 * app.height, image=ImageTk.PhotoImage(app.back) )

def keyPressed(app, event):
    if (event.key == 'Right'):
        app.page += 1
    if (event.key == 'Left'):
        app.page -= 1

def mousePressed(app, event):
    if (0.03 * app.width <= event.x <= 0.15 * app.width) and (0.85 * app.height 
    <= event.y <= 0.97 * app.height):
        startpage.runStartPage()

def redrawAll(app, canvas):
    drawInstructions(app, canvas)


def runInstructions():
    runApp(width=2000, height=1000)



