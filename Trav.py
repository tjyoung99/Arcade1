from Arcade2 import *

apple = {
         "a": False,
         "e": False,
         "l": False,
         "p": False,
            }
drake = {
         "d": False,
         "r": False,
         "a": False,
         "k": False,
         "e": False,
         }
         
def square1 (letter, x,w):
    global apple
    if apple[letter]:
        noFill()
    else:
        fill(0)
    if keyPressed:
        if key == letter :
            apple[letter]=True   
    rect(x, 475, w, 30)
    
