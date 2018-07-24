from random import * 
from Arcade2 import *
person = "tiffany" 
def setup(): 
    size(600,600)
    background(255)
    hangman()
    
def draw():
    man()
    textSize(32)
    text("apple",25,35)
    squarea(25,18)
    squarep(43,20)
    squarep(63,20)
    squarel(83,10)
    squaree(93,20)



    
