import tkinter
from cmu_112_graphics import *

    
def drawBoard(app, canvas):   

    tilewidth = app.width / 80
    tileheight = app.height / 40
    for i in range(81):
        for j in range(41):
            if (i+j) % 2 ==0:
                canvas.create_rectangle(i*tilewidth, j*tileheight, 
                (i+1)*tilewidth, (j+1)*tileheight, fill='white')
            else:
                canvas.create_rectangle(i*tilewidth, j*tileheight, 
                (i+1)*tilewidth, (j+1)*tileheight, fill='beige')
    canvas.create_rectangle(0*tilewidth, 0*tileheight, 80*tilewidth, 3*tileheight, fill='light blue')
    canvas.create_rectangle(77*tilewidth, 0*tileheight, 80*tilewidth, 40*tileheight, fill='light green')
    canvas.create_rectangle(0*tilewidth, 0*tileheight, 3*tilewidth, 25*tileheight, fill='gray')
    canvas.create_rectangle(0*tilewidth, 33*tileheight, 20*tilewidth, 40*tileheight, fill='green')
    canvas.create_rectangle(7*tilewidth, 10*tileheight, 10*tilewidth, 25*tileheight, fill='red')
    canvas.create_rectangle(14*tilewidth, 7*tileheight, 20*tilewidth, 12*tileheight, fill='beige')
    canvas.create_rectangle(54*tilewidth, 11*tileheight, 72*tilewidth, 14*tileheight, fill='red')
    canvas.create_rectangle(54*tilewidth, 19*tileheight, 72*tilewidth, 22*tileheight, fill='red')
    canvas.create_rectangle(54*tilewidth, 27*tileheight, 72*tilewidth, 30*tileheight, fill='red')
    canvas.create_rectangle(51*tilewidth, 10*tileheight, 54*tilewidth, 15*tileheight, fill='red')
    canvas.create_rectangle(51*tilewidth, 18*tileheight, 54*tilewidth, 23*tileheight, fill='red')
    canvas.create_rectangle(51*tilewidth, 26*tileheight, 54*tilewidth, 31*tileheight, fill='red')
    canvas.create_rectangle(25*tilewidth, 7*tileheight, 28*tilewidth, 18*tileheight, fill='blue')
    canvas.create_rectangle(25*tilewidth, 21*tileheight, 28*tilewidth, 32*tileheight, fill='blue')
    canvas.create_rectangle(33*tilewidth, 7*tileheight, 36*tilewidth, 18*tileheight, fill='blue')
    canvas.create_rectangle(33*tilewidth, 21*tileheight, 36*tilewidth, 32*tileheight, fill='blue')
    canvas.create_rectangle(41*tilewidth, 7*tileheight, 44*tilewidth, 18*tileheight, fill='blue')
    canvas.create_rectangle(41*tilewidth, 21*tileheight, 44*tilewidth, 32*tileheight, fill='blue')
    canvas.create_rectangle(25*tilewidth, 35*tileheight, 40*tilewidth, 38*tileheight, fill='purple')

def drawBoardTwo(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.fullMapScaled))

#def redrawAll(app, canvas):
   # drawBoard(app, canvas)

#def runBoard():
    #runApp(width=1680, height=960)

#runBoard()