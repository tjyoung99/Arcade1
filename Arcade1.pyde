from random import * 
from Arcade2 import *
from Trav import* 
from words import *
from startmenu import *
started = False 
counter=0

def setup(): 
    size(600,600)
    background(255,0,0)
   
    
def draw():
    background(255)
<<<<<<< HEAD
    global started
    if started:
        themeSetup()
        platform()
        logo()
        photo()
        man(counter)
        man1()
        delete()
    
        
    else:
        startup()
        photo()
        logo()

def words():
    apple()
    
def mouseClicked():
    global started
    started = True
                        
    # drake()
    # beige()
=======
    hangman()
    man(counter)
    if randkey=="apple":
        apple()
    if randkey=="drake":
        drake()
    if randkey=="beige":
        beige()
    if randkey=="googler":
        googler()
    if randkey=="wings":
        wings()
    if randkey=="march":
        march()
>>>>>>> 88f49d09b68b1aeceaa4f72d787e5d4191282050
    

   
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

    
    
