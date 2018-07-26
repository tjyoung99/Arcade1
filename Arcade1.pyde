from random import * 
from Arcade2 import *
from Trav import* 
from words import *
add_library('minim') 


def setup(): 
    size(600,600)
    
    global player 
    minim = Minim (this)
    player = minim.loadFile("videogame.mp3")
    player.play()

        
def draw():
    background(255)
    hangman()
    man()
    apple()

    
