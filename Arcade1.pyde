from random import * 
from Arcade2 import *
from Trav import* 
from words import *
add_library('minim') 
from startmenu import *
started = False 
counter=0

def setup(): 
    size(600,600)
    man1()
    photo()
    logo()    
    global player 
    # minim = Minim (this)
    # player = minim.loadFile("videogame.mp3")
    # player.play()
    
def draw():
    background(255)
    global started
    hangman()
    gameover(counter)
    man(counter)

    
    if started:
        themeSetup()
        platform()
        logo()
        photo()
        answers()
        man(counter)
        Exit()
           

    else:
        wallpaper()
        startup()
        logo() 
        photo()   


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
