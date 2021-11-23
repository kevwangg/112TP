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
            app.tempFoodList.append(food) #adds a random amount (between 1 and 5) of any food from each of the 6 food lists
    elif (0.6*app.width<=event.x<=0.8*app.width) and (0.3*app.height<=event.y<=0.6*app.height):
        app.mode = 'charSelect'
        app.gamemode = 'Hard'
        app.zombie = hardZombie
        for i in range(6):
            food1 = random.choice(app.listList[i])
            food2 = random.choice(app.listList[i])
            while food1 == food2: #rerolls if the food choice is the same
                food2 = random.choice(app.listList[i])
            app.foodReq[food1] = [random.randint(1, 5)]
            app.foodReq[food2] = [random.randint(1, 5)]
            app.tempFoodList.extend([food1, food2]) #adds a random amount (between 1 and 5) of any two food from each of the 6 food lists

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
    elif (0.4*app.width<=event.x<=0.6*app.width) and (0.3*app.height<=event.y<=0.9*app.height):
        app.mode = 'game'
        app.char = Annie
    elif (0.7*app.width<=event.x<=0.9*app.width) and (0.3*app.height<=event.y<=0.9*app.height):
        app.mode = 'game'
        app.char = Frank





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
Frank = Player('Frank', 8, 8, 1)

class Zombie(object):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

easyZombie = Zombie('Easy Zombie', 5)
hardZombie = Zombie('Hard Zombie', 10)

def appStarted(app):
    tilewidth = app.width // 80
    tileheight = app.height // 40
    
    #Game settings
    app.paused = False
    app.mode = 'difficulty'
    app.gamemode = None
    app.char = None
    app.zombie = None
    app.counter = 0
    app.gameComplete = False
    app.hardMode = False
    app.inSplashScreen = False
    app.timerDelay = 200
    app.timerCounter = 0
    app.secondsCounter = 0
    app.minutesCounter = 0
    app.listOn = True

    #Menu screen images
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
    app.harryStats = app.loadImage('harrystats.png')
    app.annieStats = app.loadImage('anniestats.png')
    app.frankStats = app.loadImage('frankstats.png')
    app.close = app.loadImage('close.png')
    app.quest = app.loadImage('quest.png')
    app.questSc = app.scaleImage(app.quest, 3)

    #Food
    app.fullFoodList = ['Lettuce', 'Cabbage', 'Carrot', 'Cucumber','Spinach', 'Green Beans', 'Broccoli', 'Onion', 'Mushroom', 'Tomato','Eggplant',
    'Apple', 'Orange', 'Pear', 'Avocado','Grapes', 'Bananas', 'Blueberries', 'Strawberries', 'Watermelon', 'Lemon','Peach', 'Cantaloupe', 
    'Ham', 'Bacon','Sausage', 'Beef', 'Chicken Breast', 'Chicken Wings','Fish', 'Turkey','Tofu', 'Milk', 'Yogurt','Cheese', 'Butter','Ice Cream', 
    'White Bread', 'Croissant', 'Donuts', 'Baguette', 'Bagel', 'Multigrain','Brioche', 'Popcorn', 'Cookies',  'Candy', 'Chips', 'Chocolate', 'Ramen', 'Cereal'
    , 'Cake']
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
    'Donuts': (20*tilewidth, 7*tileheight, 22*tilewidth, 10*tileheight), 'Baguette': (14*tilewidth, 12*tileheight, 16*tilewidth, 14*tileheight), 
    'Bagel': (18*tilewidth, 12*tileheight, 20*tilewidth, 14*tileheight), 'Multigrain': (14*tilewidth, 3*tileheight, 17*tilewidth, 5*tileheight),
    'Brioche': (19*tilewidth, 3*tileheight, 22*tilewidth, 5*tileheight), 'Popcorn': (23*tilewidth, 22*tileheight, 25*tilewidth, 25*tileheight), 'Cookies': (36*tilewidth, 27*tileheight, 38*tilewidth, 30*tileheight), 
    'Candy': (31*tilewidth, 15*tileheight, 33*tilewidth, 18*tileheight), 'Chips': (44*tilewidth, 9*tileheight, 46*tilewidth, 12*tileheight), 
    'Chocolate': (36*tilewidth, 8*tileheight, 38*tilewidth, 11*tileheight), 'Ramen': (39*tilewidth, 23*tileheight, 41*tilewidth, 26*tileheight), 
    'Cereal': (28*tilewidth, 10*tileheight, 30*tilewidth, 13*tileheight), 'Cake': (24*tilewidth, 32*tileheight, 32*tilewidth, 34*tileheight)}
    app.vegList = ['Lettuce', 'Cabbage', 'Carrot', 'Cucumber','Spinach', 'Green Beans', 'Broccoli', 'Onion', 'Mushroom', 'Tomato','Eggplant']
    app.fruitList = ['Apple', 'Orange', 'Pear', 'Avocado','Grapes', 'Bananas', 'Blueberries', 'Strawberries', 'Watermelon', 'Lemon','Peach', 'Cantaloupe']
    app.meatList = ['Ham', 'Bacon','Sausage', 'Beef', 'Chicken Breast', 'Chicken Wings','Fish', 'Turkey','Tofu']
    app.dairyList = ['Milk', 'Yogurt','Cheese', 'Butter','Ice Cream']
    app.breadList = ['White Bread', 'Croissant', 'Donuts', 'Baguette', 'Bagel', 'Multigrain','Brioche']
    app.snackList = ['Popcorn', 'Cookies',  'Candy', 'Chips', 'Chocolate', 'Ramen', 'Cereal']
    app.cake = 'Cake'
    app.listList = [app.vegList, app.fruitList, app.meatList, app.dairyList, app.breadList, app.snackList]
    app.foodReq = dict()
    app.locations = [(0.3*app.width, 0.3*app.height), (0.5*app.width, 0.3*app.height), (0.7*app.width, 0.3*app.height), 
    (0.4*app.width, 0.6*app.height), (0.6*app.width, 0.6*app.height)]
    app.locationsDict = {(0.3*app.width, 0.3*app.height): [range(19*tilewidth, 29*tilewidth), range(12*tileheight, 20*tileheight)], 
    (0.5*app.width, 0.3*app.height): [range(35*tilewidth, 45*tilewidth), range(12*tileheight, 20*tileheight)], 
    (0.7*app.width, 0.3*app.height): [range(50*tilewidth, 60*tilewidth), range(12*tileheight, 20*tileheight)], 
    (0.4*app.width, 0.6*app.height): [range(25*tilewidth, 35*tilewidth), range(25*tileheight, 33*tileheight)],
    (0.6*app.width, 0.6*app.height): [range(41*tilewidth, 51*tilewidth), range(25*tileheight, 33*tileheight)]}
    app.tempDict = dict()
    app.pickedLocations = set()
    app.tempFoodList = []
    app.currFood = None


    #Map
    app.fullMap = app.loadImage('betterMap.png')
    app.fullMapScaled = app.scaleImage(app.fullMap, 0.5)

    #Character 
    app.charX = 0.7 * app.width
    app.charY = 0.9 * app.height
    app.currDir = [0, -1]
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


    

    #Hard mode
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

    #Zombie
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
    [[73*app.tilewidth,30*app.tileheight], [73*app.tilewidth,30*app.tileheight], [73*app.tilewidth, 6*app.tileheight], [0, -1], [app.zombieUpSc], [app.zombieUpSc, app.zombieDownSc]]]
    app.directionsDict = {0:[(-1, 0), (0, -1)], 1:[(+1, 0), (0, -1)], 2:[(+1, 0), (0, +1)], 3:[(-1, 0), (0, +1)]}
    app.hardModeZombieDict = {(-1, 0): [app.zombieLeftSc, isLegalLeft, (-20, 0)],
    (+1, 0): [app.zombieRightSc, isLegalRight, (+20, 0)],
    (0, -1): [app.zombieUpSc, isLegalUp, (0, -20)], 
    (0, +1): [app.zombieDownSc, isLegalDown, (0, +20)]}

    #More food
    app.placeholderBanana = app.loadImage('placeholderbanana.png') #art by Zoey Lin
    app.placeholder = app.scaleImage(app.placeholderBanana, 5)
    app.banan = app.loadImage('banana.png') #art by Zoey Lin
    app.banana = app.scaleImage(app.banan, 5)
    app.blub = app.loadImage('blueberries.png') #art by Zoey Lin
    app.blueberries = app.scaleImage(app.blub, 5)
    app.strawb = app.loadImage('strawberries.png') #art by Zoey Lin
    app.strawberries = app.scaleImage(app.strawb, 5)
    app.lem = app.loadImage('lemons.png') #art by Zoey Lin
    app.lemon = app.scaleImage(app.lem, 5)
    app.apl = app.loadImage('apple.png') #art by Zoey Lin
    app.apple = app.scaleImage(app.apl, 5)
    app.avo = app.loadImage('avocado.png') #art by Zoey Lin
    app.avocado = app.scaleImage(app.avo, 5)
    app.canta = app.loadImage('cantaloupe.png') #art by Zoey Lin
    app.cantaloupe = app.scaleImage(app.canta, 5)
    app.per = app.loadImage('pear.png') #art by Zoey Lin
    app.pear = app.scaleImage(app.per, 5)
    app.orang = app.loadImage('orange.png') #art by Zoey Lin
    app.orange = app.scaleImage(app.orang, 5)
    app.grap = app.loadImage('grapes.png') #art by Zoey Lin
    app.grape = app.scaleImage(app.grap, 5)
    app.ice = app.loadImage('icecream.png') #art by Kevin Wang
    app.icecream = app.scaleImage(app.ice, 5)
    app.fsh = app.loadImage('fish.png') #art by Kevin Wang
    app.fish = app.scaleImage(app.fsh, 5)
    app.chickwing = app.loadImage('chickenwings.png') #art by Kevin Wang
    app.chickenwings = app.scaleImage(app.chickwing, 5)
    app.ram = app.loadImage('ramen.png') #art by Kevin Wang
    app.ramen = app.scaleImage(app.ram, 5)
    app.eggpl = app.loadImage('eggplant.png') #art by Zoey Lin
    app.eggplant = app.scaleImage(app.eggpl, 5)
    app.peche = app.loadImage('peach.png') #art by Zoey Lin
    app.peach = app.scaleImage(app.peche, 5)
    app.chese = app.loadImage('cheese.png') #art by Kevin Wang
    app.cheese = app.scaleImage(app.chese, 5)
    app.bague = app.loadImage('baguette.png') #art by Kevin Wang
    app.baguette = app.scaleImage(app.bague, 5)
    app.chip = app.loadImage('chips.png') #art by Kevin Wang
    app.chips = app.scaleImage(app.chip, 5)
    app.cak = app.loadImage('cake.png') #art by Kevin Wang
    app.cake = app.scaleImage(app.cak, 5)
    app.donut = app.loadImage('donuts.png') #art by Kevin Wang
    app.donuts = app.scaleImage(app.donut, 5)
    app.whitebred  = app.loadImage('whitebread.png') #art by Kevin Wang
    app.whitebread = app.scaleImage(app.whitebred, 5)
    app.multigran = app.loadImage('multigrain.png') #art by Kevin Wang
    app.multigrain = app.scaleImage(app.multigran, 5)
    app.bef = app.loadImage('beef.png') #art by Kevin Wang
    app.beef = app.scaleImage(app.bef, 5)
    app.bac = app.loadImage('bacon.png') #art by Kevin Wang
    app.bacon = app.scaleImage(app.bac, 5)
    app.ha = app.loadImage('ham.png') #art by Kevin Wang
    app.ham = app.scaleImage(app.ha, 5)
    app.btsbutter = app.loadImage('butter.png') #art by Kevin Wang
    app.butter = app.scaleImage(app.btsbutter, 5)
    app.sausa = app.loadImage('sausage.png') #art by Kevin Wang
    app.sausage = app.scaleImage(app.sausa, 5)
    app.cand = app.loadImage('candy.png') #art by Kevin Wang
    app.candy = app.scaleImage(app.cand, 5)
    app.cookie = app.loadImage('cookies.png') #art by Kevin Wang
    app.cookies = app.scaleImage(app.cookie, 5) 
    app.cerea = app.loadImage('cereal.png') #art by Kevin Wang
    app.cereal = app.scaleImage(app.cerea, 5)
    app.choco = app.loadImage('chocolate.png') #art by Kevin Wang
    app.chocolate = app.scaleImage(app.choco, 5)
    app.croiss = app.loadImage('croissants.png') #art by Kevin Wang
    app.croissant = app.scaleImage(app.croiss, 5)
    app.milk = app.loadImage('milk.png') #art by Kevin Wang
    app.milkSc = app.scaleImage(app.milk, 5)
    app.yog = app.loadImage('yogurt.png') #art by Kevin Wang
    app.yogurt = app.scaleImage(app.yog, 5)
    app.pop = app.loadImage('popcorn.png')
    app.popcorn = app.scaleImage(app.pop, 5)
    app.placeholder = app.scaleImage(app.pop, 5)
    app.pictDict = {'Lettuce': app.placeholder,  'Cabbage': app.placeholder
    , 'Carrot': app.placeholder, 'Cucumber': app.placeholder,
    'Spinach': app.placeholder, 'Green Beans': app.placeholder, 
    'Broccoli': app.placeholder, 'Onion': app.placeholder, 
    'Mushroom': app.placeholder, 'Tomato': app.placeholder,
    'Eggplant': app.eggplant, 'Apple': app.apple, 'Orange': app.orange, 
    'Pear': app.pear, 'Avocado': app.avocado,
    'Grapes': app.grape, 'Bananas': app.banana, 
    'Blueberries': app.blueberries, 'Strawberries': app.strawberries, 
    'Watermelon': app.placeholder, 'Lemon': app.lemon,
    'Peach': app.peach, 'Cantaloupe': app.cantaloupe,
    'Ham': app.ham, 'Bacon': app.bacon,
    'Sausage': app.sausage, 'Beef': app.beef, 
    'Chicken Breast': app.placeholder, 'Chicken Wings': app.chickenwings,
    'Fish': app.fish, 'Turkey': app.placeholder,
    'Tofu': app.placeholder, 'Milk': app.milkSc, 'Yogurt': app.yogurt,
    'Cheese': app.cheese, 'Butter': app.butter,
    'Ice Cream': app.icecream, 'White Bread': app.whitebread, 'Croissant': app.croissant, 
    'Donuts': app.donuts, 'Baguette': app.baguette, 
    'Bagel': app.placeholder, 'Multigrain': app.multigrain,
    'Brioche': app.placeholder, 'Popcorn': app.popcorn, 'Cookies': app.cookies, 
    'Candy': app.candy, 'Chips': app.chips, 
    'Chocolate': app.chocolate, 'Ramen': app.ramen, 
    'Cereal': app.cereal, 'Cake': app.cake}

    #Victory and Game Over
    app.youwin = app.loadImage('youwin.png')
    app.yourtime = app.loadImage('yourtime.png')
    app.besttime = app.loadImage('besttime.png')
    app.gameover = app.loadImage('gameover.png')
    app.wininstructions1 = app.loadImage('pressrto.png')
    app.wininstructions2 = app.loadImage('startanewgame.png')


#Checks the bottom of every obstacle
def isLegalUp(app, xCoord, yCoord):
    tilewidth = app.width / 80
    tileheight = app.height / 40
    #endPointY = app.charY - 60 
    if (yCoord <= tileheight * 3): 
        return False
    if ((54*tilewidth <= xCoord <= 72*tilewidth) and ((11*tileheight <= yCoord <= 
    14*tileheight) or (19*tileheight <= yCoord <= 22*tileheight) or (27*tileheight <= yCoord <= 
    30*tileheight))):
        return False
    if ((7*tilewidth <= xCoord <= 10*tilewidth) and (10*tileheight <= yCoord <= 25*tileheight)):
        return False
    if ((14*tilewidth <= xCoord <= 20*tilewidth) and (7*tileheight <= yCoord <= 12*tileheight)):
        return False
    if ((25*tilewidth <= xCoord <= 28*tilewidth) and ((7*tileheight <= yCoord <= 
    18*tileheight) or (21*tileheight <= yCoord <= 32*tileheight))):
        return False
    if ((33*tilewidth <= xCoord <= 36*tilewidth) and ((7*tileheight <= yCoord <= 
    18*tileheight) or (21*tileheight <= yCoord <= 32*tileheight))):
        return False
    if ((41*tilewidth <= xCoord <= 44*tilewidth) and ((7*tileheight <= yCoord <= 
    18*tileheight) or (21*tileheight <= yCoord <= 32*tileheight))):
        return False
    if ((25*tilewidth <= xCoord <= 40*tilewidth) and (35*tileheight <= yCoord <= 38*tileheight)):
        return False
    if ((51*tilewidth <= xCoord <= 54*tilewidth) and ((10*tileheight <= yCoord <= 
    15*tileheight) or (18*tileheight <= yCoord <= 23*tileheight) or (26*tileheight <= yCoord <= 31*tileheight))):
        return False
    return True


#Checks the top of every obstacle
def isLegalDown(app, xCoord, yCoord):
    tilewidth = app.width / 80
    tileheight = app.height / 40
    #endPointY = app.charY + 60 
    if (yCoord <= tileheight * 3): 
        return False
    if ((54*tilewidth <= xCoord <= 72*tilewidth) and ((11*tileheight <= yCoord <= 
    14*tileheight) or (19*tileheight <= yCoord <= 22*tileheight) or (27*tileheight <= yCoord <= 
    30*tileheight))):
        return False
    if ((7*tilewidth <= xCoord <= 10*tilewidth) and (10*tileheight <= yCoord <= 25*tileheight)):
        return False
    if ((14*tilewidth <= xCoord <= 20*tilewidth) and (7*tileheight <= yCoord <= 12*tileheight)):
        return False
    if ((25*tilewidth <= xCoord <= 28*tilewidth) and ((7*tileheight <= yCoord <= 
    18*tileheight) or (21*tileheight <= yCoord <= 32*tileheight))):
        return False
    if ((33*tilewidth <= xCoord <= 36*tilewidth) and ((7*tileheight <= yCoord <= 
    18*tileheight) or (21*tileheight <= yCoord <= 32*tileheight))):
        return False
    if ((41*tilewidth <= xCoord <= 44*tilewidth) and ((7*tileheight <= yCoord <= 
    18*tileheight) or (21*tileheight <= yCoord <= 32*tileheight))):
        return False
    if ((25*tilewidth <= xCoord <= 40*tilewidth) and (35*tileheight <= yCoord <= 38*tileheight)):
        return False
    if ((51*tilewidth <= xCoord <= 54*tilewidth) and ((10*tileheight <= yCoord <= 
    15*tileheight) or (18*tileheight <= yCoord <= 23*tileheight) or (26*tileheight <= yCoord <= 31*tileheight))):
        return False
    return True


#Checks the left side of every obstacle
def isLegalRight(app, xCoord, yCoord):
    tilewidth = app.width / 80
    tileheight = app.height / 40
    #endPointX = app.charX + 60
    if (xCoord >= 77*tilewidth):
        return False
    if (xCoord <= 0):
        return False
    if (xCoord <= 3*tilewidth) and (yCoord<= 25*tileheight):
        return False
    if ((54*tilewidth <= xCoord <= 72*tilewidth) and ((11*tileheight <= yCoord <= 
    14*tileheight) or (19*tileheight <= yCoord <= 22*tileheight) or (27*tileheight <= yCoord <= 
    30*tileheight))):
        return False
    if ((7*tilewidth <= xCoord <= 10*tilewidth) and (10*tileheight <= yCoord <= 25*tileheight)):
        return False
    if ((14*tilewidth <= xCoord <= 20*tilewidth) and (7*tileheight <= yCoord <= 12*tileheight)):
        return False
    if ((25*tilewidth <= xCoord <= 28*tilewidth) and ((7*tileheight <= yCoord <= 
    18*tileheight) or (21*tileheight <= yCoord <= 32*tileheight))):
        return False
    if ((33*tilewidth <= xCoord <= 36*tilewidth) and ((7*tileheight <= yCoord <= 
    18*tileheight) or (21*tileheight <= yCoord <= 32*tileheight))):
        return False
    if ((41*tilewidth <= xCoord <= 44*tilewidth) and ((7*tileheight <= yCoord <= 
    18*tileheight) or (21*tileheight <= yCoord <= 32*tileheight))):
        return False
    if ((25*tilewidth <= xCoord <= 40*tilewidth) and (35*tileheight <= yCoord <= 38*tileheight)):
        return False
    if ((51*tilewidth <= xCoord <= 54*tilewidth) and ((10*tileheight <= yCoord <= 
    15*tileheight) or (18*tileheight <= yCoord <= 23*tileheight) or (26*tileheight <= yCoord <= 31*tileheight))):
        return False
    return True


#Checks the right side of every obstacle
def isLegalLeft(app, xCoord, yCoord):
    tilewidth = app.width / 80
    tileheight = app.height / 40
    #endPointX = app.charX - 60
    if (xCoord >= 77*tilewidth):
        return False
    if (xCoord <= 0):
        return False
    if (xCoord <= 3*tilewidth) and (yCoord <= 25*tileheight):
        return False
    if ((54*tilewidth <= xCoord <= 72*tilewidth) and ((11*tileheight <= yCoord <= 
    14*tileheight) or (19*tileheight <= yCoord <= 22*tileheight) or (27*tileheight <= yCoord <= 
    30*tileheight))):
        return False
    if ((7*tilewidth <= xCoord <= 10*tilewidth) and (10*tileheight <= yCoord <= 25*tileheight)):
        return False
    if ((14*tilewidth <= xCoord <= 20*tilewidth) and (7*tileheight <= yCoord <= 12*tileheight)):
        return False
    if ((25*tilewidth <= xCoord <= 28*tilewidth) and ((7*tileheight <= yCoord <= 
    18*tileheight) or (21*tileheight <= yCoord <= 32*tileheight))):
        return False
    if ((33*tilewidth <= xCoord <= 36*tilewidth) and ((7*tileheight <= yCoord <= 
    18*tileheight) or (21*tileheight <= yCoord <= 32*tileheight))):
        return False
    if ((41*tilewidth <= xCoord <= 44*tilewidth) and ((7*tileheight <= yCoord <= 
    18*tileheight) or (21*tileheight <= yCoord <= 32*tileheight))):
        return False
    if ((25*tilewidth <= xCoord <= 40*tilewidth) and (35*tileheight <= yCoord <= 38*tileheight)):
        return False
    if ((51*tilewidth <= xCoord <= 54*tilewidth) and ((10*tileheight <= yCoord <= 
    15*tileheight) or (18*tileheight <= yCoord <= 23*tileheight) or (26*tileheight <= yCoord <= 31*tileheight))):
        return False
    return True

#Checks if the game is complete
def isComplete(app):
    tilewidth = app.width / 80
    tileheight = app.height / 40
    if app.tempFoodList == [] and ((0 <= app.charX <= 20*tilewidth) and (33*tileheight <= app.charY <= 40*tileheight)):
        return True
    else: return False

#Creates the screen of foods when the player interacts with a light green rectangle
def createFoodScreen(app, food):
    location = random.choice(app.locations)
    app.tempDict[food] = location
    app.pickedLocations.add(location)
    i = 0
    while i < 4:
        otherFood = random.choice(app.fullFoodList)
        while otherFood in app.tempDict:
            otherFood = random.choice(app.fullFoodList)
        otherLocation = random.choice(app.locations)
        while otherLocation in app.pickedLocations:
            otherLocation = random.choice(app.locations)
        app.tempDict[otherFood] = otherLocation
        app.pickedLocations.add(otherLocation)
        i += 1    

def game_mousePressed(app, event):
    if (0 <= event.x <= 3*(app.width/80)) and (0 <= event.y <= 3*(app.height/40)):
        app.listOn = True
    if app.listOn == True:  
        if (app.width//2+app.offSetW-app.r1 <= event.x <= 
            app.width//2+app.offSetW+app.r1) and (app.height//2-app.offSetH-app.r1 <= event.y <= 
            app.height//2+app.offSetW+app.r1):
                app.listOn = False
    if app.inSplashScreen: #Generates the counter of the food
        n = int(app.foodReq[app.currFood][0])
        midW = app.width // 2
        midH = app.height // 2
        if (event.x in app.locationsDict[app.tempDict[app.currFood]][0]) and (event.y in app.locationsDict[app.tempDict[app.currFood]][1]):
            app.counter += 1
            if app.counter == n:
                app.tempFoodList.remove(app.currFood)
                del app.foodReq[app.currFood]
                app.tempDict = dict()
                app.pickedLocations = set()
                app.inSplashScreen = not app.inSplashScreen 
                #Automatically closes food screen if the amount of food required is collected


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
        if not isLegalUp(app, app.charX, app.charY-60): #Returns character to previous position if move isn't legal
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
        if not isLegalDown(app, app.charX, app.charY+60): #Returns character to previous position if move isn't legal
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
        if not isLegalRight(app, app.charX+60, app.charY): #Returns character to previous position if move isn't legal
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
        if not isLegalLeft(app, app.charX-60, app.charY): #Returns character to previous position if move isn't legal
            app.charX, app.charY = app.prevMove[0], app.prevMove[1]
            app.currImg = app.prevMove[2]
            app.currDir = app.prevMove[3]
    if (event.key == 'Space'):
        if app.inSplashScreen == True: return
        app.prevMove = [app.charX, app.charY, app.currImg, app.currDir]
        app.charX += app.currDir[0] * app.char.dash
        app.charY += app.currDir[1] * app.char.dash
        if app.currDir == [0, -1]:
            if not isLegalUp(app, app.charX, app.charY-60): #Returns character to previous position if move isn't legal
                app.charX, app.charY = app.prevMove[0], app.prevMove[1]
                app.currImg = app.prevMove[2]
                app.currDir = app.prevMove[3]
        if app.currDir == [0, +1]:
            if not isLegalDown(app, app.charX, app.charY+60): #Returns character to previous position if move isn't legal
                app.charX, app.charY = app.prevMove[0], app.prevMove[1]
                app.currImg = app.prevMove[2]
                app.currDir = app.prevMove[3]
        if app.currDir == [-1, 0]:
            if not isLegalLeft(app, app.charX-60, app.charY): #Returns character to previous position if move isn't legal
                app.charX, app.charY = app.prevMove[0], app.prevMove[1]
                app.currImg = app.prevMove[2]
                app.currDir = app.prevMove[3]
        if app.currDir == [+1, 0]:
            if not isLegalRight(app, app.charX+60, app.charY): #Returns character to previous position if move isn't legal
                app.charX, app.charY = app.prevMove[0], app.prevMove[1]
                app.currImg = app.prevMove[2]
                app.currDir = app.prevMove[3]
    if (event.key == 'x'):
        if app.inSplashScreen:
            app.tempDict = dict()
            app.pickedLocations = set()
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
                    createFoodScreen(app, app.currFood)
                    app.counter = 0
            if app.currDir == [0, +1]:
                endPointY = app.charY + 60
                if ((app.fullDict[food][0] < app.charX-15 < app.fullDict[food][2]) or (app.fullDict[food][0] < 
                app.charX+15 < app.fullDict[food][2]))  and (app.fullDict[food][1] < endPointY < app.fullDict[food][3]):
                    app.inSplashScreen = True
                    app.currFood = food
                    createFoodScreen(app, app.currFood)
                    app.counter = 0
            if app.currDir == [-1, 0]:
                endPointX = app.charX - 60
                if ((app.fullDict[food][1] < app.charY-15 < app.fullDict[food][3]) or (app.fullDict[food][1] < 
                app.charY+15 < app.fullDict[food][3]))  and (app.fullDict[food][0] < endPointX < app.fullDict[food][2]):
                    app.inSplashScreen = True
                    app.currFood = food
                    createFoodScreen(app, app.currFood)
                    app.counter = 0
            if app.currDir == [+1, 0]:
                endPointX = app.charX + 60
                if ((app.fullDict[food][1] < app.charY-15 < app.fullDict[food][3]) or (app.fullDict[food][1] < 
                app.charY+15 < app.fullDict[food][3]))  and (app.fullDict[food][0] < endPointX < app.fullDict[food][2]):
                    app.inSplashScreen = True   
                    app.currFood = food
                    createFoodScreen(app, app.currFood)
                    app.counter = 0


#Checks for a collision between the zombie and the player
def checkCollision(app, xCoord, yCoord):
    if (int(app.charX) in range(int(xCoord-20), int(xCoord+20)) and (int(app.charY) in range(int(yCoord-20), int(yCoord+20)))):
        return True
    else:
        return False

#Checks if the player is behind the zombie
def isBehind(app, xCoord, yCoord, dir):
    if dir[1] == 0:
        nextPosition  = xCoord + app.zombie.speed * dir[0]
        if (abs(nextPosition - app.charX) >= abs(xCoord - app.charX)) and (int(app.charY) in range(int(yCoord-50), int(yCoord+50))):
            return True
        else:
            return False
    else:
        nextPosition = yCoord + app.zombie.speed * dir[1]
        if (abs(nextPosition - app.charY) >= abs(yCoord - app.charY)) and (int(app.charX) in range(int(xCoord-50), int(xCoord+50))):
            return True
        else:
            return False

#Moves the zombie back and forth between its set boundaries
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

#Checks which general direction the player is in
def determineQuadrant(app, xCoord, yCoord):
    if (app.charX <= xCoord) and (app.charY <= yCoord):
        return 0
    elif (app.charX > xCoord) and (app.charY <= yCoord):
        return 1
    elif (app.charX > xCoord) and (app.charY > yCoord):
        return 2
    elif (app.charX <= xCoord) and (app.charY > yCoord):
        return 3

#Moves zombie towards player
def hardModeMoveZombie(app, zombie, val):
        zombie[0][0] += app.zombie.speed * val[0]
        zombie[0][1] += app.zombie.speed * val[1]
        zombie[4][0] = app.hardModeZombieDict[val][0]
    

def game_timerFired(app):
    app.timerCounter += app.timerDelay
    if app.timerCounter == 1000:
        app.secondsCounter += 1
        app.timerCounter = 0
    if app.secondsCounter == 60:
        app.secondsCounter = 0
        app.minutesCounter += 1
    if app.hardMode == True:
        for zombie in app.zombieList:
            #Check if player has hit a zombie
            if checkCollision(app, zombie[0][0], zombie[0][1]):
                app.char.hit(app.char.health)
                if app.char.health == 0:
                    app.mode = 'gameover'
            quadrant = determineQuadrant(app, zombie[0][0], zombie[0][1])
            number = random.randrange(2)
            val = app.directionsDict[quadrant][number]
            #Locates the player and moves the player in one of the two possible directions
            #In the shortest possible path to the player
            xCoord = zombie[0][0] + app.hardModeZombieDict[val][2][0]
            yCoord = zombie[0][1] + app.hardModeZombieDict[val][2][1]
            if app.hardModeZombieDict[val][1](app, xCoord, yCoord):
                hardModeMoveZombie(app, zombie, val)
            else:
                val = app.directionsDict[quadrant][not number]
                #If the move is not a legal move, do the opposite of that move so that zombie always remains moving
                hardModeMoveZombie(app, zombie, val)
    elif app.gamemode == 'Easy':
            for zombie in app.zombieList:
                if checkCollision(app, zombie[0][0], zombie[0][1]):
                    app.char.hit(app.char.health)
                    if app.char.health == 0:
                        app.mode = 'gameover'
                moveZombie(app, zombie)
    elif app.gamemode == 'Hard':
            for zombie in app.zombieList:
                if checkCollision(app, zombie[0][0], zombie[0][1]):
                    app.char.hit(app.char.health)
                    if app.char.health == 0:
                        app.mode = 'gameover'
                if isBehind(app, zombie[0][0], zombie[0][1], zombie[3]):
                    #If player is behind zombie, turn zombie around and move in direction towards player
                    zombie[3][0], zombie[3][1] = zombie[3][0]*(-1), zombie[3][1]*(-1)
                    zombie[4][0] = zombie[5][int(not zombie[5].index(zombie[4][0]))]
                moveZombie(app, zombie)


def game_drawBoard(app, canvas):
    drawBoard.drawBoardTwo(app, canvas)
    tilewidth = app.width / 80
    tileheight = app.height / 40
    canvas.create_text(5*tilewidth, 1.5*tileheight, text=f'Lives: {app.char.health}', font=50)
    if app.secondsCounter < 10:
        if app.minutesCounter < 10:
            canvas.create_text(12*tilewidth, 1.5*tileheight, text=f'0{app.minutesCounter}:0{app.secondsCounter}', font='Arial 30')
        else:
           canvas.create_text(12*tilewidth, 1.5*tileheight, text=f'{app.minutesCounter}:0{app.secondsCounter}', font='Arial 30') 
    else:
        if app.minutesCounter < 10:
            canvas.create_text(12*tilewidth, 1.5*tileheight, text=f'0{app.minutesCounter}:{app.secondsCounter}', font='Arial 30')
        else:
            canvas.create_text(12*tilewidth, 1.5*tileheight, text=f'{app.minutesCounter}:{app.secondsCounter}', font='Arial 30')
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
        canvas.create_image(app.width//2+app.offSetW, app.height//2-app.offSetH, image=ImageTk.PhotoImage(app.close))
        canvas.create_text(app.width//2, app.height//2-app.offSetH+textOffset, text=app.currEvent, font=30)
        #canvas.create_text(app.width//2, app.height//2-app.offSetH+2*textOffset, text=app.hardEventsDict[app.currEvent][0], font=20)
        for i in range(len(app.tempFoodList)):
            canvas.create_text(app.width//2, app.height//2-app.offSetH+textOffset*(i+4), 
            text=f'{app.foodReq[app.tempFoodList[i]][0]} {app.tempFoodList[i]}', font=30)
    else:
        textOffset = 30
        canvas.create_rectangle(app.width//2-app.offSetW, app.height//2-app.offSetH, 
        app.width//2+app.offSetW, app.height//2+app.offSetH, width=5, fill='light blue')
        canvas.create_oval(app.width//2+app.offSetW-app.r1, app.height//2-app.offSetH-app.r1, 
        app.width//2+app.offSetW+app.r1, app.height//2-app.offSetH+app.r1, width=3, fill='light blue')
        canvas.create_image(app.width//2+app.offSetW, app.height//2-app.offSetH, image=ImageTk.PhotoImage(app.close))
        canvas.create_text(app.width//2, app.height//2-app.offSetH + textOffset, text='Shopping List', font=30)
        for i in range(len(app.tempFoodList)):
            canvas.create_text(app.width//2, app.height//2-app.offSetH+textOffset*(i+2), 
            text=f'{app.foodReq[app.tempFoodList[i]][0]} {app.tempFoodList[i]}', font=30)
        if app.tempFoodList == []:
            canvas.create_text(app.width//2, app.height//2, text='Press X in the safe zone to complete the game!')


def game_drawCharacter(app, canvas):
    canvas.create_image(app.charX, app.charY, image=ImageTk.PhotoImage(app.currImg))

def game_drawPauseBoard(app, canvas):
    midW = app.width // 2
    midH = app.height // 2
    canvas.create_rectangle(midW - 0.3*midW, midH - 0.4*midH, 
    midW + 0.3*midW, midH + 0.3*midH, fill='light blue', width=5)
    canvas.create_image(midW, midH - 0.3*midH, image=ImageTk.PhotoImage(app.gamepaused))
    canvas.create_image(midW, midH+0.1*midH, image=ImageTk.PhotoImage(app.pausedinstructions))

def game_drawFoodScreen(app, canvas, food):
    tilewidth = app.width / 80
    tileheight = app.height / 40
    midW = app.width // 2
    midH = app.height // 2
    for food in app.tempDict:
        canvas.create_image(app.tempDict[food][0], app.tempDict[food][1], image=ImageTk.PhotoImage(app.pictDict[food]))       
    canvas.create_rectangle(0.4*app.width, 0.85*app.height, 0.6*app.width, 0.9*app.height, fill='light blue', width=3)
    canvas.create_text(0.5*app.width, 0.88*app.height, text=f'{app.counter}/{int(app.foodReq[app.currFood][0])} {app.currFood}')   

    #for val in app.locations:
        #canvas.create_image(val[0], val[1], image=ImageTk.PhotoImage(app.placeholder))
    #canvas.create_rectangle(midW - 0.3*midW, midH - 0.4*midH, 
    #midW + 0.3*midW, midH + 0.3*midH, fill='light blue', width=5)
    #canvas.create_image(midW, midH, image=ImageTk.[PhotoImage(app.pictDict[food]))
    #canvas.create_text(midW, midH + 0.2*midH, text=f'{app.counter}/{int(app.foodReq[app.currFood][0])} {app.currFood}')

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
    midW = app.width//2
    midH = app.height//2
    offsetW = 0.1 * app.width
    offsetH = 0.1 * app.height
    canvas.create_rectangle(0, 0, app.width, app.height, fill='light blue')
    canvas.create_image(midW, 2*offsetH, image=ImageTk.PhotoImage(app.youwin))
    canvas.create_image(midW-offsetW, 4*offsetH, image=ImageTk.PhotoImage(app.yourtime))
    if app.secondsCounter < 10:
        if app.minutesCounter < 10:
            canvas.create_text(midW+offsetW, 4*offsetH, text=f'0{app.minutesCounter}:0{app.secondsCounter}', font='Arial 30')
        else:
           canvas.create_text(midW+offsetW, 4*offsetH, text=f'{app.minutesCounter}:0{app.secondsCounter}', font='Arial 30') 
    else:
        if app.minutesCounter < 10:
            canvas.create_text(midW+offsetW, 4*offsetH, text=f'0{app.minutesCounter}:{app.secondsCounter}', font='Arial 30')
        else:
            canvas.create_text(midW+offsetW, 4*offsetH, text=f'{app.minutesCounter}:{app.secondsCounter}', font='Arial 30')
    canvas.create_image(midW-offsetW, 5*offsetH, image=ImageTk.PhotoImage(app.besttime))
    canvas.create_image(midW, 7*offsetH, image=ImageTk.PhotoImage(app.wininstructions1))
    canvas.create_image(midW, 7.5*offsetH, image=ImageTk.PhotoImage(app.wininstructions2))
    


def complete_keyPressed(app, event):
    if event.key == 'r':
        startpage.runStartPage()


################################
#GAME OVER
################################

def gameover_redrawAll(app, canvas):
    midW = app.width//2
    midH = app.height//2
    offsetW = 0.1 * app.width
    offsetH = 0.1 * app.height
    canvas.create_rectangle(0, 0, app.width, app.height, fill='light blue')
    canvas.create_image(midW, 2*offsetH, image=ImageTk.PhotoImage(app.gameover))
    canvas.create_image(midW, 7*offsetH, image=ImageTk.PhotoImage(app.wininstructions1))
    canvas.create_image(midW, 7.5*offsetH, image=ImageTk.PhotoImage(app.wininstructions2))
    

def gameover_keyPressed(app, event):
    if event.key == 'r':
        startpage.runStartPage()




def runGame():
    runApp(width=1680, height=960)

runGame()
