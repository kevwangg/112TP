import tkinter
from cmu_112_graphics import *
import startpage

################################
#DIFFICULTY PAGE
################################

def difficulty_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='light blue')
    canvas.create_image(app.width//2, 0.2 * app.height, image=ImageTk.PhotoImage(app.difficultyScaled))
    canvas.create_rectangle(0.2*app.width, 0.3*app.height, 0.4*app.width, 0.6*app.height, fill='light blue', width=3)
    canvas.create_image(0.3*app.width, 0.45*app.height, image=ImageTk.PhotoImage(app.easyScaled))
    canvas.create_rectangle(0.6*app.width, 0.3*app.height, 0.8*app.width, 0.6*app.height, fill='light blue', width=3)
    canvas.create_image(0.7*app.width, 0.45*app.height, image=ImageTk.PhotoImage(app.hardScaled))

def difficulty_mousePressed(app, event):
    if (0.2*app.width<=event.x<=0.4*app.width) and (0.3*app.height<=event.y<=0.6*app.height):
        app.mode = 'charSelect'
    elif (0.6*app.width<=event.x<=0.8*app.width) and (0.3*app.height<=event.y<=0.6*app.height):
        app.mode = 'charSelect'



################################
#CHARACTER SELECTION
################################

def charSelect_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='light blue')
    canvas.create_image(app.width//2, 0.2 * app.height, image=ImageTk.PhotoImage(app.charSelectScale))
    canvas.create_rectangle(0.1*app.width, 0.3*app.height, 0.3*app.width, 0.9*app.height, fill='light blue', width=3)
    canvas.create_image(0.2*app.width, 0.6*app.height, image=ImageTk.PhotoImage(app.harryScaled))
    canvas.create_rectangle(0.4*app.width, 0.3*app.height, 0.6*app.width, 0.9*app.height, fill='light blue', width=3)
    canvas.create_image(0.5*app.width, 0.6*app.height, image=ImageTk.PhotoImage(app.annieScaled))
    canvas.create_rectangle(0.7*app.width, 0.3*app.height, 0.9*app.width, 0.9*app.height, fill='light blue', width=3)
    canvas.create_image(0.8*app.width, 0.6*app.height, image=ImageTk.PhotoImage(app.frankScaled))


def charSelect_mousePressed(app, event):
    if (0.1*app.width<=event.x<=0.3*app.width) and (0.3*app.height<=event.y<=0.9*app.height):
        app.mode = 'game'
    elif (0.4*app.width<=event.x<=0.6*app.width) and (0.3*app.height<=event.y<=0.9*app.height):
        app.mode = 'game'
    elif (0.7*app.width<=event.x<=0.9*app.width) and (0.3*app.height<=event.y<=0.9*app.height):
        app.mode = 'game'



################################
#GAME
################################




def appStarted(app):
    app.paused = False
    app.mode = 'difficulty'
    app.image1 = app.loadImage('gamepaused.png')
    app.gamepaused = app.scaleImage(app.image1, 1)
    app.image2 = app.loadImage('pauseinstructions.png')
    app.pausedinstructions = app.scaleImage(app.image2, 1)
    app.difficulty = app.loadImage('difficulty.png')
    app.difficultyScaled = app.scaleImage(app.difficulty, 1)
    app.easy = app.loadImage('easy.png')
    app.easyScaled = app.scaleImage(app.easy, 1)
    app.hard = app.loadImage('hard.png')
    app.hardScaled = app.scaleImage(app.hard, 1)
    app.charSelect = app.loadImage('charselect.png')
    app.charSelectScale = app.scaleImage(app.charSelect, 1)
    app.harry = app.loadImage('harry.png')
    app.harryScaled = app.scaleImage(app.harry, 0.7)
    app.frank = app.loadImage('frank.png')
    app.frankScaled = app.scaleImage(app.frank, 0.7)
    app.annie = app.loadImage('annie.png')
    app.annieScaled = app.scaleImage(app.annie, 0.7)


def game_drawBoard(app, canvas):
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


def game_keyPressed(app, event):
    if app.paused == True:
        if (event.key == 'r'):
            startpage.runStartPage()
    if (event.key == 'p'):
        app.paused = not app.paused

def game_drawPauseBoard(app, canvas):
    midW = app.width // 2
    midH = app.height // 2
    canvas.create_rectangle(midW - 0.3*midW, midH - 0.4*midH, 
    midW + 0.3*midW, midH + 0.3*midH, fill='light blue')
    canvas.create_image(midW, midH - 0.3*midH, image=ImageTk.PhotoImage(app.gamepaused))
    canvas.create_image(midW, midH+0.1*midH, image=ImageTk.PhotoImage(app.pausedinstructions))

def game_redrawAll(app, canvas):
    game_drawBoard(app, canvas)
    if app.paused == True:
        game_drawPauseBoard(app, canvas)




def runGame():
    runApp(width=2000, height=1000)

