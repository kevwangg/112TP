import tkinter
from cmu_112_graphics import *
import instructionspage
import creditspage
import game


def appStarted(app):
    app.horizdiv = app.width // 3
    app.vertdiv = app.height // 4
    app.offsetW = app.width // 10
    app.offsetH = app.height // 20
    app.horizavg = app.horizdiv // 2
    app.vertavg = app.vertdiv // 2
    app.image1 = app.loadImage('start.png')
    app.startbutton = app.scaleImage(app.image1, 1)
    app.image2 = app.loadImage('instructions.png')
    app.instructionbutton = app.scaleImage(app.image2, 1)
    app.image3 = app.loadImage('credits.png')
    app.creditbutton = app.scaleImage(app.image3, 1)


def drawStartPage(app, canvas):
    horizdiv = app.width // 3
    vertdiv = app.height // 4
    offsetH = app.height // 20

    canvas.create_rectangle(0, 0, app.width, app.height, fill='light blue')

    canvas.create_text(horizdiv + horizdiv // 2, offsetH, text='Title', font='Arial 50 bold')

    canvas.create_rectangle(horizdiv, vertdiv + offsetH, 
    2 * horizdiv , 2 * vertdiv - offsetH, width=5)

    canvas.create_image(app.width // 2, 0.25 * app.height + 0.5 * vertdiv, 
    image=ImageTk.PhotoImage(app.startbutton))

    canvas.create_rectangle(horizdiv, 2 * vertdiv + offsetH, 
    2 * horizdiv , 3 * vertdiv - offsetH, width=5)

    canvas.create_image(app.width // 2, 0.5 * app.height + 0.5 * vertdiv, 
    image=ImageTk.PhotoImage(app.instructionbutton))

    canvas.create_rectangle(horizdiv, 3 * vertdiv + offsetH, 
    2 * horizdiv , 4 * vertdiv - offsetH, width=5)

    canvas.create_image(app.width // 2, 0.75 * app.height + 0.5 * vertdiv, 
    image=ImageTk.PhotoImage(app.creditbutton))

def mousePressed(app, event):
    horizdiv = app.width // 3
    vertdiv = app.height // 4
    offsetH = app.height // 20
    if (horizdiv <= event.x <= 2 * horizdiv) and (vertdiv + offsetH <= 
    event.y <= 2 * vertdiv - offsetH):
        game.runGame()
    if (horizdiv <= event.x <= 2 * horizdiv) and (2 * vertdiv + offsetH <= 
    event.y <= 3 * vertdiv - offsetH):
        instructionspage.runInstructions()
    elif (horizdiv <= event.x <= 2 * horizdiv) and (3 * vertdiv + offsetH <= 
    event.y <= 4 * vertdiv - offsetH):
        creditspage.runCredits()


def redrawAll(app, canvas):
    drawStartPage(app, canvas)


def runStartPage():
    runApp(width=2000, height=1000)

