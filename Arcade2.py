from random import * 
from Hangman2 import *
from Trav import *
from words import *

keywords = {
        "apple" : "Fruits",
        "drake" : "Celebrities",
        "beige" : "Colors",
        "googler" : "Jobs",
        "wings" : "Foods",
        "march" : "Months",
            }

def man1():
    global parts
    fill(0)
    head=createShape(ELLIPSE,330, 120, 40, 40) #hangman head
    leftarm=createShape(LINE,330,170, 310, 190)  #left hand
    rightarm=createShape(LINE,330,170, 350, 190) #right hand
    leftleg=createShape(LINE,330, 235 ,310, 270) #left leg
    rightleg=createShape(LINE,330, 240, 350, 270) #right leg
    body=createShape(LINE,330, 140, 330, 240)  #hangman body
    parts=[head,leftarm,rightarm,leftleg,rightleg,body]

parts=[]

randkey = choice(keywords.keys())

def answers():
 if randkey=="apple":
    apple()
    win5()
 elif randkey=="drake":
    drake()
    win1()
 elif randkey=="beige":
    beige()
    win4()
 elif randkey=="googler":
    googler()
    win6()
 elif randkey=="wings":
    wings()
    win2()
 elif randkey=="march":
    march() 
    win3()

def themeSetup():
    topic = keywords[randkey]
    guessingWords = randkey
    fill(0)
    text(topic, 80, 250)
    textSize(32)

    text("Topic", 66, 220)
    fill(0)
    text(guessingWords, 260, 500)

def platform():
    line(250, 100, 250, 200) #first middle line
    line(300, 100, 250, 100) #right line ( where hangman head is placed)
    line(250, 300, 250, 200) #lengthens the  first middle line
    line(220, 300, 280, 300) #last line of the platform
                      
def logo():
    fill(randint(0,255),randint(0,255),randint(0,255))
    textSize (20)
    text ("OOGLE MAN", 250, 50)
        
def photo():
    img = loadImage("google-logo.png")
    image(img, 190, 20, width/10, height/10)  

def man(counter):
    global parts
    for part in range (counter):
        shape(parts[part])

def hangman():
    themeSetup()
    platform()
    logo()
    photo()
