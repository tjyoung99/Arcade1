from random import * 
from Arcade2 import *
from Trav import* 
from words import *
<<<<<<< HEAD
add_library('minim') 


def setup(): 
    size(600,600)
    
    global player 
    minim = Minim (this)
    player = minim.loadFile("videogame.mp3")
    player.play()

        
=======
from startmenu import *
started = False 
counter=0

def setup(): 
    size(600,600)
    man1()
   
    
>>>>>>> 7dbfa0b7ed7bdb88488fd9641ccbcac727e33f7e
def draw():
    background(255)
    global started
    hangman()
<<<<<<< HEAD
    man()
    apple()

=======
    man(counter)
    if started:
        themeSetup()
        platform()
        logo()
        photo()
        answers()
        man(counter)
    
    
      
    else:
        startup()
        photo()
        logo()

def mouseClicked():
    global started
    started = True
                        

    
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

    
>>>>>>> 7dbfa0b7ed7bdb88488fd9641ccbcac727e33f7e
    
