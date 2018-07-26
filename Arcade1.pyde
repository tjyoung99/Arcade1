from random import * 
from Arcade2 import *
from Trav import* 
from words import *
<<<<<<< HEAD
add_library('minim') 
from startmenu import *
from meh import *
started = False 
counter=0

def setup(): 
    size(600,600)
    man1()
    photo()
    logo()
    
    global player 
    minim = Minim (this)
    player = minim.loadFile("videogame.mp3")
    player.play()
    
=======
from startmenu import *
add_library('minim') 
started = False 
counter=0

def setup():
    global player 
    size(600,600)
    man1()
    # minim = Minim (this)
    # player = minim.loadFile("videogame.mp3")
    # player.play()
    

>>>>>>> 118f9c2e9979b5ee9a6e5e97cfa5c4da577fb624
def draw():
    background(255)
    global started
    hangman()
<<<<<<< HEAD
    man(counter)
    gameover(counter)
=======
    apple()
    man(counter)
    
>>>>>>> 118f9c2e9979b5ee9a6e5e97cfa5c4da577fb624
    
    if started:
        themeSetup()
        platform()
        logo()
        photo()
        answers()
        man(counter)
<<<<<<< HEAD
=======
        Exit()
           
>>>>>>> 118f9c2e9979b5ee9a6e5e97cfa5c4da577fb624
    else:
        startup()


def mouseClicked():
    global started
    started = True
                        
def mousePressed():
    if mousePressed and (mouseX >= 550 and mouseX <= 6000) and (mouseY >= 550 and mouseY <= 600):
       exit()
       
    
def keyReleased():
    global counter
    if randkey=="apple":
        for letters in range (len (noapple)):
            if key == noapple[letters]:
                counter=counter+1
    if randkey=="drake":
        for letters in range (len (nodrake)):
            if key == nodrake[letters]:
                counter=counter+1
    if randkey=="beige":
        for letters in range (len (nobeige)):
            if key == nobeige[letters]:
                counter=counter+1
    if randkey=="googler":
        for letters in range (len (nogoogler)):
            if key == nogoogler[letters]:
                counter=counter+1
    if randkey=="wings":
        for letters in range (len (nowings)):
            if key == nowings[letters]:
                counter=counter+1
    if randkey=="march":
        for letters in range (len (nomarch)):
            if key == nomarch[letters]:
                counter=counter+1

<<<<<<< HEAD
   
=======
    
<<<<<<< HEAD
=======

    
>>>>>>> 118f9c2e9979b5ee9a6e5e97cfa5c4da577fb624
>>>>>>> 853a16a5f4471619a1b5fc7a1272c72a0df6bc84
