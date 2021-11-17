import tkinter
from cmu_112_graphics import *
import startpage
import random
import drawBoard

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
        app.gamemode = 'Easy'
        app.zombie = easyZombie
        for i in range(6):
            food = random.choice(app.listList[i])
            app.foodReq[food] = [random.randint(1, 5)]
            app.tempFoodList.append(food)
        print(app.gamemode)
        print(app.foodReq)
    elif (0.6*app.width<=event.x<=0.8*app.width) and (0.3*app.height<=event.y<=0.6*app.height):
        app.mode = 'charSelect'
        app.gamemode = 'Hard'
        app.zombie = hardZombie
        for i in range(6):
            food1 = random.choice(app.listList[i])
            food2 = random.choice(app.listList[i])
            while food1 == food2:
                food2 = random.choice(app.listList[i])
            app.foodReq[food1] = [random.randint(1, 5)]
            app.foodReq[food2] = [random.randint(1, 5)]
            app.tempFoodList.extend([food1, food2])
        print(app.gamemode)
        print(app.foodReq)



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
    canvas.create_image(0.21*app.width, 0.75*app.height, image=ImageTk.PhotoImage(app.harryStats))
    canvas.create_image(0.51*app.width, 0.75*app.height, image=ImageTk.PhotoImage(app.annieStats))
    canvas.create_image(0.81*app.width, 0.75*app.height, image=ImageTk.PhotoImage(app.frankStats))



def charSelect_mousePressed(app, event):
    if (0.1*app.width<=event.x<=0.3*app.width) and (0.3*app.height<=event.y<=0.9*app.height):
        app.mode = 'game'
        app.char = Harry
        print(app.char.name)
    elif (0.4*app.width<=event.x<=0.6*app.width) and (0.3*app.height<=event.y<=0.9*app.height):
        app.mode = 'game'
        app.char = Annie
        print(app.char.name)
    elif (0.7*app.width<=event.x<=0.9*app.width) and (0.3*app.height<=event.y<=0.9*app.height):
        app.mode = 'game'
        app.char = Frank
        print(app.char.name)




################################
#GAME
################################

class Player(object):
    def __init__(self, name, speed, dash, health):
        self.name = name
        self.speed = speed
        self.dash = dash
        self.health = health
    
    def hit(self, health):
        self.health -= 1

Harry = Player('Harry', 2, 15, 3)
Annie = Player('Annie', 5, 12, 2)
Frank = Player('Frank', 30, 8, 1)

class Zombie(object):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

easyZombie = Zombie('Easy Zombie', 20)
hardZombie = Zombie('Hard Zombie', 9)

def appStarted(app):
    tilewidth = app.width / 80
    tileheight = app.height / 40
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
    app.gamemode = None
    app.char = None
    app.zombie = None
    app.fullDict = {'Lettuce': (75*tilewidth, 5*tileheight, 77*tilewidth, 8*tileheight),  'Cabbage': (75*tilewidth, 21*tileheight, 77*tilewidth, 24*tileheight)
    , 'Carrot': (75*tilewidth, 9*tileheight, 77*tilewidth, 12*tileheight), 'Cucumber': (75*tilewidth, 13*tileheight, 77*tilewidth, 16*tileheight),
    'Spinach': (75*tilewidth, 17*tileheight, 77*tilewidth, 20*tileheight), 'Green Beans': (72*tilewidth, 27*tileheight, 74*tilewidth, 30*tileheight), 
    'Broccoli': (75*tilewidth, 25*tileheight, 77*tilewidth, 28*tileheight), 'Onion': (75*tilewidth, 29*tileheight, 77*tilewidth, 32*tileheight), 
    'Mushroom': (75*tilewidth, 33*tileheight, 77*tilewidth, 36*tileheight), 'Tomato': (72*tilewidth, 11*tileheight, 74*tilewidth, 14*tileheight),
    'Eggplant': (72*tilewidth, 19*tileheight, 74*tilewidth, 22*tileheight), 'Apple': (54*tilewidth, 17*tileheight, 57*tilewidth, 19*tileheight), 'Orange': (58*tilewidth, 22*tileheight, 61*tilewidth, 24*tileheight), 
    'Pear': (62*tilewidth, 17*tileheight, 65*tilewidth, 19*tileheight), 'Avocado': (66*tilewidth, 22*tileheight, 69*tilewidth, 24*tileheight),
    'Grapes': (64*tilewidth, 14*tileheight, 67*tilewidth, 16*tileheight), 'Bananas': (58*tilewidth, 25*tileheight, 61*tilewidth, 27*tileheight), 
    'Blueberries': (54*tilewidth, 30*tileheight, 57*tilewidth, 32*tileheight), 'Strawberries': (62*tilewidth, 30*tileheight, 65*tilewidth, 32*tileheight), 
    'Watermelon': (49*tilewidth, 10*tileheight, 51*tilewidth, 15*tileheight), 'Lemon': (66*tilewidth, 25*tileheight, 69*tilewidth, 27*tileheight),
    'Peach': (56*tilewidth, 9*tileheight, 59*tilewidth, 11*tileheight), 'Cantaloupe': (49*tilewidth, 26*tileheight, 51*tilewidth, 31*tileheight),
    'Ham': (3*tilewidth, 5*tileheight, 5*tilewidth, 8*tileheight), 'Bacon': (3*tilewidth, 9*tileheight, 5*tilewidth, 12*tileheight),
    'Sausage': (3*tilewidth, 13*tileheight, 5*tilewidth, 16*tileheight), 'Beef': (10*tilewidth, 15*tileheight, 12*tilewidth, 18*tileheight), 
    'Chicken Breast': (3*tilewidth, 17*tileheight, 5*tilewidth, 20*tileheight), 'Chicken Wings': (3*tilewidth, 21*tileheight, 5*tilewidth, 24*tileheight),
    'Fish': (5*tilewidth, 11*tileheight, 7*tilewidth, 14*tileheight), 'Turkey': (5*tilewidth, 19*tileheight, 7*tilewidth, 22*tileheight),
    'Tofu': (7*tilewidth, 25*tileheight, 10*tilewidth, 27*tileheight), 'Milk': (69*tilewidth, 3*tileheight, 74*tilewidth, 5*tileheight), 'Yogurt': (59*tilewidth, 3*tileheight, 64*tilewidth, 5*tileheight),
    'Cheese': (49*tilewidth, 3*tileheight, 54*tilewidth, 5*tileheight), 'Butter': (39*tilewidth, 3*tileheight, 44*tilewidth, 5*tileheight),
    'Ice Cream': (29*tilewidth, 3*tileheight, 34*tilewidth, 5*tileheight), 'White Bread': (9*tilewidth, 3*tileheight, 12*tilewidth, 5*tileheight), 'Croissant': (12*tilewidth, 7*tileheight, 14*tilewidth, 10*tileheight), 
    'Bagels': (20*tilewidth, 7*tileheight, 22*tilewidth, 10*tileheight), 'Baguette': (14*tilewidth, 12*tileheight, 16*tilewidth, 14*tileheight), 
    'Brioche': (18*tilewidth, 12*tileheight, 20*tilewidth, 14*tileheight), 'Multigrain': (14*tilewidth, 3*tileheight, 17*tilewidth, 5*tileheight),
    'Sourdough': (19*tilewidth, 3*tileheight, 22*tilewidth, 5*tileheight), 'Popcorn': (23*tilewidth, 22*tileheight, 25*tilewidth, 25*tileheight), 'Cookies': (36*tilewidth, 27*tileheight, 38*tilewidth, 30*tileheight), 
    'Candy': (31*tilewidth, 15*tileheight, 33*tilewidth, 18*tileheight), 'Chips': (44*tilewidth, 9*tileheight, 46*tilewidth, 12*tileheight), 
    'Chocolate': (36*tilewidth, 8*tileheight, 38*tilewidth, 11*tileheight), 'Ramen': (39*tilewidth, 23*tileheight, 41*tilewidth, 26*tileheight), 
    'Cereal': (28*tilewidth, 10*tileheight, 30*tilewidth, 13*tileheight), 'Cake': (24*tilewidth, 32*tileheight, 32*tilewidth, 34*tileheight)}
    app.vegList = ['Lettuce', 'Cabbage', 'Carrot', 'Cucumber','Spinach', 'Green Beans', 'Broccoli', 'Onion', 'Mushroom', 'Tomato','Eggplant']
    app.fruitList = ['Apple', 'Orange', 'Pear', 'Avocado','Grapes', 'Bananas', 'Blueberries', 'Strawberries', 'Watermelon', 'Lemon','Peach', 'Cantaloupe']
    app.meatList = ['Ham', 'Bacon','Sausage', 'Beef', 'Chicken Breast', 'Chicken Wings','Fish', 'Turkey','Tofu']
    app.dairyList = ['Milk', 'Yogurt','Cheese', 'Butter','Ice Cream']
    app.breadList = ['White Bread', 'Croissant', 'Bagels', 'Baguette', 'Brioche', 'Multigrain','Sourdough']
    app.snackList = ['Popcorn', 'Cookies',  'Candy', 'Chips', 'Chocolate', 'Ramen', 'Cereal']
    app.cake = 'Cake'
    app.listList = [app.vegList, app.fruitList, app.meatList, app.dairyList, app.breadList, app.snackList]
    app.foodReq = dict()
    app.charX = 0.7 * app.width
    app.charY = 0.9 * app.height
    app.currDir = [0, -1]
    app.fullMap = app.loadImage('betterMap.png')
    app.fullMapScaled = app.scaleImage(app.fullMap, 0.5)
    app.listOn = True
    app.offSetW = 0.1 * app.width
    app.offSetH = 0.3 * app.height
    app.r1 = 30
    app.tilewidth = app.width / 80
    app.tileheight = app.height / 40
    app.up = app.loadImage('up.png')
    app.up1 = app.scaleImage(app.up, 3)
    app.down = app.loadImage('down.png')
    app.down1 = app.scaleImage(app.down, 3)
    app.right = app.loadImage('right.png')
    app.right1 = app.scaleImage(app.right, 3)
    app.left = app.loadImage('left.png')
    app.left1 = app.scaleImage(app.left, 3)
    app.imageList = [app.up1, app.down1, app.right1, app.left1]
    app.currImg = app.imageList[0]
    app.prevMove = []
    app.harryStats = app.loadImage('harrystats.png')
    app.annieStats = app.loadImage('anniestats.png')
    app.frankStats = app.loadImage('frankstats.png')
    app.tempFoodList = []
    app.quest = app.loadImage('quest.png')
    app.questSc = app.scaleImage(app.quest, 3)
    app.inSplashScreen = False
    app.currFood = None
    app.counter = 0
    app.gameComplete = False
    app.hardMode = False
    app.hardEventsDict = {'Christmas Time!': ['Santa’s still coming to town,\n make sure to buy some food to help him\n on his journey! Get:', 
    [(2, 'Cookies'), (1, 'Milk')]], 'Mom’s Secret Recipe': ['Mom wants to make her special recipe again,\n but she won’t tell you the recipe. Get:', 
    [(2, 'Carrot'), (1, 'Fish')]], 'Neighborhood Party': ['A BBQ during an apocalypse?\n Better help get the food! Get:', [(2, 'Beef'), (1, 'Chicken Wings')]],
    'Home Alone': ['Home alone with your siblings again.\n Might as well get some snacks! Get:', [(5, 'Chocolate'), (1, 'Ice Cream')]],
    'Limited Time Offer': ['A discount on cereals so you can get\n a new ray gun to shoot zombies with! Get:', [(3, 'Cereal'), (1, app.cake)]]}
    app.currEvent = None
    app.hardEvents = ['Christmas Time!', 'Mom’s Secret Recipe', 'Neighborhood Party', 'Home Alone', 'Limited Time Offer' ]
    app.hardImg = app.loadImage('hardmodephone.png')
    app.hardImgIcon = app.scaleImage(app.hardImg, 0.2)
    app.hardImgDisplay = app.scaleImage(app.hardImg, 2)
    app.hardCounter = 0
    app.zombieLeft = app.loadImage('zombieleft.png')
    app.zombieLeftSc = app.scaleImage(app.zombieLeft, 3)
    app.zombieRight = app.loadImage('zombieright.png')
    app.zombieRightSc = app.scaleImage(app.zombieRight, 3)
    app.zombieUp = app.loadImage('zombieup.png')
    app.zombieUpSc = app.scaleImage(app.zombieUp, 3)
    app.zombieDown = app.loadImage('zombiedown.png')
    app.zombieDownSc = app.scaleImage(app.zombieDown, 3)
    app.zombieList = [[[7*app.tilewidth,5*app.tileheight],[ 7*app.tilewidth,5*app.tileheight], [31*app.tilewidth, 5*app.tileheight], [+1, 0], [app.zombieRightSc], [app.zombieRightSc, app.zombieLeftSc]],
    [[11*app.tilewidth,7*app.tileheight], [11*app.tilewidth,7*app.tileheight], [11*app.tilewidth, 28*app.tileheight], [0, +1], [app.zombieDownSc], [app.zombieDownSc, app.zombieUpSc]],
    [[21*app.tilewidth,28*app.tileheight], [21*app.tilewidth,28*app.tileheight], [21*app.tilewidth, 7*app.tileheight], [0, -1], [app.zombieUpSc], [app.zombieUpSc, app.zombieDownSc]],
    [[23*app.tilewidth,19*app.tileheight], [23*app.tilewidth,19*app.tileheight], [46*app.tilewidth, 19*app.tileheight], [+1, 0], [app.zombieRightSc], [app.zombieRightSc, app.zombieLeftSc]],
    [[47*app.tilewidth,6*app.tileheight], [47*app.tilewidth,6*app.tileheight], [47*app.tilewidth, 30*app.tileheight], [0, +1], [app.zombieDownSc], [app.zombieDownSc, app.zombieUpSc]],
    [[49*app.tilewidth,5*app.tileheight], [49*app.tilewidth,5*app.tileheight], [72*app.tilewidth, 5*app.tileheight], [+1, 0], [app.zombieRightSc], [app.zombieRightSc, app.zombieLeftSc]],
    [[75*app.tilewidth,30*app.tileheight], [75*app.tilewidth,30*app.tileheight], [75*app.tilewidth, 6*app.tileheight], [0, -1], [app.zombieUpSc], [app.zombieUpSc, app.zombieDownSc]]]
    app.timerDelay = 25
    app.placeholderBanana = app.loadImage('placeholderbanana.png')
    app.placeholder = app.scaleImage(app.placeholderBanana, 5)
    app.banan = app.loadImage('banana.png')
    app.banana = app.scaleImage(app.banan, 5)
    app.blub = app.loadImage('blueberries.png')
    app.blueberries = app.scaleImage(app.blub, 5)
    app.strawb = app.loadImage('strawberries.png')
    app.strawberries = app.scaleImage(app.strawb, 5)
    app.lem = app.loadImage('lemons.png')
    app.lemon = app.scaleImage(app.lem, 5)
    app.apl = app.loadImage('apple.png')
    app.apple = app.scaleImage(app.apl, 5)
    app.pictDict = {'Lettuce': app.placeholder,  'Cabbage': app.placeholder
    , 'Carrot': app.placeholder, 'Cucumber': app.placeholder,
    'Spinach': app.placeholder, 'Green Beans': app.placeholder, 
    'Broccoli': app.placeholder, 'Onion': app.placeholder, 
    'Mushroom': app.placeholder, 'Tomato': app.placeholder,
    'Eggplant': app.placeholder, 'Apple': app.apple, 'Orange': app.placeholder, 
    'Pear': app.placeholder, 'Avocado': app.placeholder,
    'Grapes': app.placeholder, 'Bananas': app.banana, 
    'Blueberries': app.blueberries, 'Strawberries': app.strawberries, 
    'Watermelon': app.placeholder, 'Lemon': app.lemon,
    'Peach': app.placeholder, 'Cantaloupe': app.placeholder,
    'Ham': app.placeholder, 'Bacon': app.placeholder,
    'Sausage': app.placeholder, 'Beef': app.placeholder, 
    'Chicken Breast': app.placeholder, 'Chicken Wings': app.placeholder,
    'Fish': app.placeholder, 'Turkey': app.placeholder,
    'Tofu': app.placeholder, 'Milk': app.placeholder, 'Yogurt': app.placeholder,
    'Cheese': app.placeholder, 'Butter': app.placeholder,
    'Ice Cream': app.placeholder, 'White Bread': app.placeholder, 'Croissant': app.placeholder, 
    'Bagels': app.placeholder, 'Baguette': app.placeholder, 
    'Brioche': app.placeholder, 'Multigrain': app.placeholder,
    'Sourdough': app.placeholder, 'Popcorn': app.placeholder, 'Cookies': app.placeholder, 
    'Candy': app.placeholder, 'Chips': app.placeholder, 
    'Chocolate': app.placeholder, 'Ramen': app.placeholder, 
    'Cereal': app.placeholder, 'Cake': app.placeholder}


def isLegalUp(app):
    tilewidth = app.width / 80
    tileheight = app.height / 40
    endPointY = app.charY - 60 
    if (endPointY <= tileheight * 3): 
        return False
    if ((54*tilewidth <= app.charX <= 72*tilewidth) and ((11*tileheight <= endPointY <= 
    14*tileheight) or (19*tileheight <= endPointY <= 22*tileheight) or (27*tileheight <= endPointY <= 
    30*tileheight))):
        return False
    if ((7*tilewidth <= app.charX <= 10*tilewidth) and (10*tileheight <= endPointY <= 25*tileheight)):
        return False
    if ((14*tilewidth <= app.charX <= 20*tilewidth) and (7*tileheight <= endPointY <= 12*tileheight)):
        return False
    if ((25*tilewidth <= app.charX <= 28*tilewidth) and ((7*tileheight <= endPointY <= 
    18*tileheight) or (21*tileheight <= endPointY <= 32*tileheight))):
        return False
    if ((33*tilewidth <= app.charX <= 36*tilewidth) and ((7*tileheight <= endPointY <= 
    18*tileheight) or (21*tileheight <= endPointY <= 32*tileheight))):
        return False
    if ((41*tilewidth <= app.charX <= 44*tilewidth) and ((7*tileheight <= endPointY <= 
    18*tileheight) or (21*tileheight <= endPointY <= 32*tileheight))):
        return False
    if ((25*tilewidth <= app.charX <= 40*tilewidth) and (35*tileheight <= endPointY <= 38*tileheight)):
        return False
    if ((51*tilewidth <= app.charX <= 54*tilewidth) and ((10*tileheight <= endPointY <= 
    15*tileheight) or (18*tileheight <= endPointY <= 23*tileheight) or (26*tileheight <= endPointY <= 31*tileheight))):
        return False
    return True

def isLegalDown(app):
    tilewidth = app.width / 80
    tileheight = app.height / 40
    endPointY = app.charY + 60 
    if (endPointY <= tileheight * 3): 
        return False
    if ((54*tilewidth <= app.charX <= 72*tilewidth) and ((11*tileheight <= endPointY <= 
    14*tileheight) or (19*tileheight <= endPointY <= 22*tileheight) or (27*tileheight <= endPointY <= 
    30*tileheight))):
        return False
    if ((7*tilewidth <= app.charX <= 10*tilewidth) and (10*tileheight <= endPointY <= 25*tileheight)):
        return False
    if ((14*tilewidth <= app.charX <= 20*tilewidth) and (7*tileheight <= endPointY <= 12*tileheight)):
        return False
    if ((25*tilewidth <= app.charX <= 28*tilewidth) and ((7*tileheight <= endPointY <= 
    18*tileheight) or (21*tileheight <= endPointY <= 32*tileheight))):
        return False
    if ((33*tilewidth <= app.charX <= 36*tilewidth) and ((7*tileheight <= endPointY <= 
    18*tileheight) or (21*tileheight <= endPointY <= 32*tileheight))):
        return False
    if ((41*tilewidth <= app.charX <= 44*tilewidth) and ((7*tileheight <= endPointY <= 
    18*tileheight) or (21*tileheight <= endPointY <= 32*tileheight))):
        return False
    if ((25*tilewidth <= app.charX <= 40*tilewidth) and (35*tileheight <= endPointY <= 38*tileheight)):
        return False
    if ((51*tilewidth <= app.charX <= 54*tilewidth) and ((10*tileheight <= endPointY <= 
    15*tileheight) or (18*tileheight <= endPointY <= 23*tileheight) or (26*tileheight <= endPointY <= 31*tileheight))):
        return False
    return True

def isLegalRight(app):
    tilewidth = app.width / 80
    tileheight = app.height / 40
    endPointX = app.charX + 60
    if (endPointX >= 77*tilewidth):
        return False
    if (endPointX <= 0):
        return False
    if (endPointX <= 3*tilewidth) and (app.charY <= 25*tileheight):
        return False
    if ((54*tilewidth <= endPointX <= 72*tilewidth) and ((11*tileheight <= app.charY <= 
    14*tileheight) or (19*tileheight <= app.charY <= 22*tileheight) or (27*tileheight <= app.charY <= 
    30*tileheight))):
        return False
    if ((7*tilewidth <= endPointX <= 10*tilewidth) and (10*tileheight <= app.charY <= 25*tileheight)):
        return False
    if ((14*tilewidth <= endPointX <= 20*tilewidth) and (7*tileheight <= app.charY <= 12*tileheight)):
        return False
    if ((25*tilewidth <= endPointX <= 28*tilewidth) and ((7*tileheight <= app.charY <= 
    18*tileheight) or (21*tileheight <= app.charY <= 32*tileheight))):
        return False
    if ((33*tilewidth <= endPointX <= 36*tilewidth) and ((7*tileheight <= app.charY <= 
    18*tileheight) or (21*tileheight <= app.charY <= 32*tileheight))):
        return False
    if ((41*tilewidth <= endPointX <= 44*tilewidth) and ((7*tileheight <= app.charY <= 
    18*tileheight) or (21*tileheight <= app.charY <= 32*tileheight))):
        return False
    if ((25*tilewidth <= endPointX <= 40*tilewidth) and (35*tileheight <= app.charY <= 38*tileheight)):
        return False
    if ((51*tilewidth <= endPointX <= 54*tilewidth) and ((10*tileheight <= app.charY <= 
    15*tileheight) or (18*tileheight <= app.charY <= 23*tileheight) or (26*tileheight <= app.charY <= 31*tileheight))):
        return False
    return True

def isLegalLeft(app):
    tilewidth = app.width / 80
    tileheight = app.height / 40
    endPointX = app.charX - 60
    if (endPointX >= 77*tilewidth):
        return False
    if (endPointX <= 0):
        return False
    if (endPointX <= 3*tilewidth) and (app.charY <= 25*tileheight):
        return False
    if ((54*tilewidth <= endPointX <= 72*tilewidth) and ((11*tileheight <= app.charY <= 
    14*tileheight) or (19*tileheight <= app.charY <= 22*tileheight) or (27*tileheight <= app.charY <= 
    30*tileheight))):
        return False
    if ((7*tilewidth <= endPointX <= 10*tilewidth) and (10*tileheight <= app.charY <= 25*tileheight)):
        return False
    if ((14*tilewidth <= endPointX <= 20*tilewidth) and (7*tileheight <= app.charY <= 12*tileheight)):
        return False
    if ((25*tilewidth <= endPointX <= 28*tilewidth) and ((7*tileheight <= app.charY <= 
    18*tileheight) or (21*tileheight <= app.charY <= 32*tileheight))):
        return False
    if ((33*tilewidth <= endPointX <= 36*tilewidth) and ((7*tileheight <= app.charY <= 
    18*tileheight) or (21*tileheight <= app.charY <= 32*tileheight))):
        return False
    if ((41*tilewidth <= endPointX <= 44*tilewidth) and ((7*tileheight <= app.charY <= 
    18*tileheight) or (21*tileheight <= app.charY <= 32*tileheight))):
        return False
    if ((25*tilewidth <= endPointX <= 40*tilewidth) and (35*tileheight <= app.charY <= 38*tileheight)):
        return False
    if ((51*tilewidth <= endPointX <= 54*tilewidth) and ((10*tileheight <= app.charY <= 
    15*tileheight) or (18*tileheight <= app.charY <= 23*tileheight) or (26*tileheight <= app.charY <= 31*tileheight))):
        return False
    return True

def isComplete(app):
    tilewidth = app.width / 80
    tileheight = app.height / 40
    if app.tempFoodList == [] and ((0 <= app.charX <= 20*tilewidth) and (33*tileheight <= app.charY <= 40*tileheight)):
        return True
    else: return False

def game_drawBoard(app, canvas):
    drawBoard.drawBoardTwo(app, canvas)
    tilewidth = app.width / 80
    tileheight = app.height / 40
    canvas.create_text(5*tilewidth, 1.5*tileheight, text=f'Lives: {app.char.health}', font=50)
    if app.hardMode == False:
        canvas.create_image(1.5*tilewidth, 1.5*tileheight, image=ImageTk.PhotoImage(app.questSc))
    if app.hardMode == True:
        canvas.create_image(1.5*tilewidth, 1.5*tileheight, image=ImageTk.PhotoImage(app.hardImgIcon))
    for food in app.foodReq:
        canvas.create_rectangle(app.fullDict[food][0], app.fullDict[food][1]-3, app.fullDict[food][2], app.fullDict[food][3]-3, fill='light green')


def game_drawZombie(app, canvas):
    mid = app.tilewidth//2
    for zombie in app.zombieList:
        animation = zombie[4][0]
        canvas.create_image(zombie[0][0] + mid, zombie[0][1] + mid, image=ImageTk.PhotoImage(animation))


def game_drawShopList(app, canvas):
    if app.hardMode == True:
        textOffset = 30
        canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.hardImgDisplay))
        canvas.create_oval(app.width//2+app.offSetW-app.r1, app.height//2-app.offSetH-app.r1, 
        app.width//2+app.offSetW+app.r1, app.height//2-app.offSetH+app.r1, width=3, fill='black') #fix this
        canvas.create_text(app.width//2, app.height//2-app.offSetH+textOffset, text=app.currEvent, font=30)
        canvas.create_text(app.width//2, app.height//2-app.offSetH+2*textOffset, text=app.hardEventsDict[app.currEvent][0], font=20)
        for i in range(len(app.tempFoodList)):
            canvas.create_text(app.width//2, app.height//2-app.offSetH+textOffset*(i+4), 
            text=f'{app.foodReq[app.tempFoodList[i]][0]} {app.tempFoodList[i]}', font=30)
    else:
        textOffset = 30
        canvas.create_rectangle(app.width//2-app.offSetW, app.height//2-app.offSetH, 
        app.width//2+app.offSetW, app.height//2+app.offSetH, width=5, fill='light blue')
        canvas.create_oval(app.width//2+app.offSetW-app.r1, app.height//2-app.offSetH-app.r1, 
        app.width//2+app.offSetW+app.r1, app.height//2-app.offSetH+app.r1, width=3, fill='light blue')
        canvas.create_text(app.width//2, app.height//2-app.offSetH + textOffset, text='Shopping List', font=30)
        for i in range(len(app.tempFoodList)):
            canvas.create_text(app.width//2, app.height//2-app.offSetH+textOffset*(i+2), 
            text=f'{app.foodReq[app.tempFoodList[i]][0]} {app.tempFoodList[i]}', font=30)
        if app.tempFoodList == []:
            canvas.create_text(app.width//2, app.height//2, text='Press X in the safe zone to complete the game!')


def game_drawCharacter(app, canvas):
    r = 20
    #canvas.create_oval(app.charX - r, app.charY-r, app.charX+r, app.charY+r, fill='green')
    canvas.create_image(app.charX, app.charY, image=ImageTk.PhotoImage(app.currImg))


def game_mousePressed(app, event):
    if (0 <= event.x <= 3*(app.width/80)) and (0 <= event.y <= 3*(app.height/40)):
        app.listOn = True
    if app.listOn == True:  
        if (app.width//2+app.offSetW-app.r1 <= event.x <= 
            app.width//2+app.offSetW+app.r1) and (app.height//2-app.offSetH-app.r1 <= event.y <= 
            app.height//2+app.offSetW+app.r1):
                app.listOn = False
    if app.inSplashScreen:
        n = int(app.foodReq[app.currFood][0])
        midW = app.width // 2
        midH = app.height // 2
        if (midW - 0.3*midW<= event.x <= midW + 0.3*midW) and (midH - 0.4*midH <= event.y <= midH + 0.3*midH):
            app.counter += 1
            if app.counter == n:
                app.tempFoodList.remove(app.currFood)
                del app.foodReq[app.currFood]
                app.inSplashScreen = not app.inSplashScreen




def game_keyPressed(app, event):
    if app.paused == True:
        if (event.key == 'r'):
            startpage.runStartPage()
    if (event.key == 'p'):
        app.paused = not app.paused
    if (event.key == 'Up'):
        if app.inSplashScreen == True: return
        app.prevMove = [app.charX, app.charY, app.currImg, app.currDir]
        app.currImg = app.imageList[0]
        app.currDir[0], app.currDir[1] = 0, -1
        app.charX += app.currDir[0] * app.char.speed
        app.charY += app.currDir[1] * app.char.speed
        if not isLegalUp(app):
            app.charX, app.charY = app.prevMove[0], app.prevMove[1]
            app.currImg = app.prevMove[2]
            app.currDir = app.prevMove[3]   
    if (event.key == 'Down'):
        if app.inSplashScreen == True: return
        app.prevMove = [app.charX, app.charY, app.currImg, app.currDir]
        app.currImg = app.imageList[1]
        app.currDir[0], app.currDir[1] = 0, +1
        app.charX += app.currDir[0] * app.char.speed
        app.charY += app.currDir[1] * app.char.speed
        if not isLegalDown(app):
            app.charX, app.charY = app.prevMove[0], app.prevMove[1]
            app.currImg = app.prevMove[2]
            app.currDir = app.prevMove[3]
    if (event.key == 'Right'):
        if app.inSplashScreen == True: return
        app.prevMove = [app.charX, app.charY, app.currImg, app.currDir]
        app.currImg = app.imageList[2]
        app.currDir[0], app.currDir[1] = +1, 0
        app.charX += app.currDir[0] * app.char.speed
        app.charY += app.currDir[1] * app.char.speed
        if not isLegalRight(app):
            app.charX, app.charY = app.prevMove[0], app.prevMove[1]
            app.currImg = app.prevMove[2]
            app.currDir = app.prevMove[3]
    if (event.key == 'Left'):
        if app.inSplashScreen == True: return
        app.prevMove = [app.charX, app.charY, app.currImg, app.currDir]
        app.currImg = app.imageList[3]
        app.currDir[0], app.currDir[1] = -1, 0
        app.charX += app.currDir[0] * app.char.speed
        app.charY += app.currDir[1] * app.char.speed
        if not isLegalLeft(app):
            app.charX, app.charY = app.prevMove[0], app.prevMove[1]
            app.currImg = app.prevMove[2]
            app.currDir = app.prevMove[3]
    if (event.key == 'Space'):
        if app.inSplashScreen == True: return
        app.prevMove = [app.charX, app.charY, app.currImg, app.currDir]
        app.charX += app.currDir[0] * app.char.dash
        app.charY += app.currDir[1] * app.char.dash
        if app.currDir == [0, -1]:
            if not isLegalUp(app):
                app.charX, app.charY = app.prevMove[0], app.prevMove[1]
                app.currImg = app.prevMove[2]
                app.currDir = app.prevMove[3]
        if app.currDir == [0, +1]:
            if not isLegalDown(app):
                app.charX, app.charY = app.prevMove[0], app.prevMove[1]
                app.currImg = app.prevMove[2]
                app.currDir = app.prevMove[3]
        if app.currDir == [-1, 0]:
            if not isLegalLeft(app):
                app.charX, app.charY = app.prevMove[0], app.prevMove[1]
                app.currImg = app.prevMove[2]
                app.currDir = app.prevMove[3]
        if app.currDir == [+1, 0]:
            if not isLegalRight(app):
                app.charX, app.charY = app.prevMove[0], app.prevMove[1]
                app.currImg = app.prevMove[2]
                app.currDir = app.prevMove[3]
    if (event.key == 'x'):
        if app.inSplashScreen:
            app.inSplashScreen = not app.inSplashScreen
            return
        if isComplete(app):
            if app.gamemode == 'Easy':
                app.mode = 'complete'
            if app.gamemode == 'Hard':
                app.hardCounter += 1
                if app.hardCounter == 2:
                    app.mode = 'complete'
                else:
                    app.hardMode = True
                    event = random.choice(app.hardEvents)
                    app.currEvent = event
                    for foodQuant in app.hardEventsDict[event][1]:
                        placeholder = foodQuant[1]
                        app.foodReq[placeholder] = [foodQuant[0]]
                        app.tempFoodList.append(foodQuant[1])
                    app.listOn = True
        for food in app.foodReq:
            if app.currDir == [0, -1]:
                endPointY = app.charY - 60
                if ((app.fullDict[food][0] < app.charX-15 < app.fullDict[food][2]) or (app.fullDict[food][0] < 
                app.charX+15 < app.fullDict[food][2]))  and (app.fullDict[food][1] < endPointY < app.fullDict[food][3]):
                    app.inSplashScreen = True
                    app.currFood = food
                    app.counter = 0
            if app.currDir == [0, +1]:
                endPointY = app.charY + 60
                if ((app.fullDict[food][0] < app.charX-15 < app.fullDict[food][2]) or (app.fullDict[food][0] < 
                app.charX+15 < app.fullDict[food][2]))  and (app.fullDict[food][1] < endPointY < app.fullDict[food][3]):
                    app.inSplashScreen = True
                    app.currFood = food
                    app.counter = 0
            if app.currDir == [-1, 0]:
                endPointX = app.charX - 60
                if ((app.fullDict[food][1] < app.charY-15 < app.fullDict[food][3]) or (app.fullDict[food][1] < 
                app.charY+15 < app.fullDict[food][3]))  and (app.fullDict[food][0] < endPointX < app.fullDict[food][2]):
                    app.inSplashScreen = True
                    app.currFood = food
                    app.counter = 0
            if app.currDir == [+1, 0]:
                endPointX = app.charX + 60
                if ((app.fullDict[food][1] < app.charY-15 < app.fullDict[food][3]) or (app.fullDict[food][1] < 
                app.charY+15 < app.fullDict[food][3]))  and (app.fullDict[food][0] < endPointX < app.fullDict[food][2]):
                    app.inSplashScreen = True   
                    app.currFood = food
                    app.counter = 0


def game_drawPauseBoard(app, canvas):
    midW = app.width // 2
    midH = app.height // 2
    canvas.create_rectangle(midW - 0.3*midW, midH - 0.4*midH, 
    midW + 0.3*midW, midH + 0.3*midH, fill='light blue', width=5)
    canvas.create_image(midW, midH - 0.3*midH, image=ImageTk.PhotoImage(app.gamepaused))
    canvas.create_image(midW, midH+0.1*midH, image=ImageTk.PhotoImage(app.pausedinstructions))

def game_drawFoodScreen(app, canvas, food):
    midW = app.width // 2
    midH = app.height // 2
    #canvas.create_rectangle(midW - 0.3*midW, midH - 0.4*midH, 
    #midW + 0.3*midW, midH + 0.3*midH, fill='light blue', width=5)
    canvas.create_image(midW, midH, image=ImageTk.PhotoImage(app.pictDict[food]))
    canvas.create_text(midW, midH + 0.2*midH, text=f'{app.counter}/{int(app.foodReq[app.currFood][0])} {app.currFood}')

def checkCollision(app, xCoord, yCoord):
    if (int(app.charX) in range(int(xCoord-20), int(xCoord+20)) and (int(app.charY) in range(int(yCoord-20), int(yCoord+20)))):
        return True
    else:
        return False

def isBehind(app, xCoord, yCoord, dir):
    if dir[1] == 0:
        nextPosition  = xCoord + app.zombie.speed * dir[0]
        if (abs(nextPosition - app.charX) > abs(xCoord - app.charX)) and (int(app.charY) in range(int(yCoord-75), int(yCoord+75))):
            return True
        else:
            return False
    else:
        nextPosition = yCoord + app.zombie.speed * dir[1]
        if (abs(nextPosition - app.charY) > abs(yCoord - app.charY)) and (int(app.charX) in range(int(xCoord-75), int(xCoord+75))):
            return True
        else:
            return False



def moveZombie(app, zombie):
        zombie[0][0] += app.zombie.speed * zombie[3][0]
        zombie[0][1] += app.zombie.speed * zombie[3][1]
        if (zombie[3][0] == -1):
            if (zombie[0][0] < zombie[2][0]):
                zombie[3][0], zombie[3][1] = zombie[3][0]*(-1), zombie[3][1]*(-1)
                zombie[0][0] += 3 * app.zombie.speed * zombie[3][0]
                zombie[4][0] = zombie[5][int(not 1)]
            if zombie[0][0] > zombie[1][0]:
                zombie[3][0], zombie[3][1] = zombie[3][0]*(-1), zombie[3][1]*(-1)
                zombie[0][0] += 3 * app.zombie.speed * zombie[3][0]   
                zombie[4][0] = zombie[5][int(not 0)]        
        if (zombie[3][0] == +1):  
            if (zombie[0][0] > zombie[2][0]):
                zombie[3][0], zombie[3][1] = zombie[3][0]*(-1), zombie[3][1]*(-1)
                zombie[0][0] += 3 * app.zombie.speed * zombie[3][0]
                zombie[4][0] = zombie[5][int(not 1)]
            if (zombie[0][0] < zombie[1][0]):
                zombie[3][0], zombie[3][1] = zombie[3][0]*(-1), zombie[3][1]*(-1)
                zombie[0][0] += 3 * app.zombie.speed * zombie[3][0]
                zombie[4][0] = zombie[5][int(not 0)]  
        if (zombie[3][1] == -1):
            if (zombie[0][1] < zombie[2][1]):
                zombie[3][0], zombie[3][1] = zombie[3][0]*(-1), zombie[3][1]*(-1)
                zombie[0][1] += 3 * app.zombie.speed * zombie[3][1]
                zombie[4][0] = zombie[5][int(not 1)]
            if (zombie[0][1] > zombie[1][1]):
                zombie[3][0], zombie[3][1] = zombie[3][0]*(-1), zombie[3][1]*(-1)
                zombie[0][1] += 3 * app.zombie.speed * zombie[3][1]
                zombie[4][0] = zombie[5][int(not 0)]  
        if (zombie[3][1] == +1):
            if (zombie[0][1] > zombie[2][1]):
                zombie[3][0], zombie[3][1] = zombie[3][0]*(-1), zombie[3][1]*(-1)
                zombie[0][1] += 3 * app.zombie.speed * zombie[3][1]
                zombie[4][0] = zombie[5][int(not 1)]
            if (zombie[0][1] < zombie[1][1]):
                zombie[3][0], zombie[3][1] = zombie[3][0]*(-1), zombie[3][1]*(-1)
                zombie[0][1] += 3 * app.zombie.speed * zombie[3][1]
                zombie[4][0] = zombie[5][int(not 0)]  

def game_timerFired(app):
    if app.gamemode == 'Easy':
            for zombie in app.zombieList:
                if checkCollision(app, zombie[0][0], zombie[0][1]):
                    app.char.hit(app.char.health)
                    if app.char.health == 0:
                        app.mode = 'difficulty'
                moveZombie(app, zombie)
    if app.gamemode == 'Hard':
            for zombie in app.zombieList:
                if checkCollision(app, zombie[0][0], zombie[0][1]):
                    app.char.hit(app.char.health)
                    if app.char.health == 0:
                        app.mode = 'difficulty'
                if isBehind(app, zombie[0][0], zombie[1][0], zombie[3]):
                    zombie[3][0], zombie[3][1] = zombie[3][0]*(-1), zombie[3][1]*(-1)
                    zombie[4][0] = zombie[5][int(not zombie[5].index(zombie[4][0]))]
                moveZombie(app, zombie)




def game_redrawAll(app, canvas):
    game_drawBoard(app, canvas)
    game_drawCharacter(app, canvas)
    game_drawZombie(app, canvas)
    if app.paused == True:
        game_drawPauseBoard(app, canvas)
    if app.listOn == True:
            game_drawShopList(app, canvas)
    if app.inSplashScreen == True:
        game_drawFoodScreen(app, canvas, app.currFood)

################################
#COMPLETE
################################

def complete_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='light blue')


def complete_keyPressed(app, event):
    if event.key == 'r':
        startpage.runStartPage()









def runGame():
    runApp(width=1680, height=960)


runGame()