from Arcade2 import *

apple = {
         "a": False,
         "e": False,
         "l": False,
         "p": False,
         "p": False,
            }
noapple=["b","c","d","g","f","h","i","j","k","m","n","o","q","r","s","t","u",
         "v","w","x","y","z"]
drake = {
         "d": False,
         "r": False,
         "a": False,
         "k": False,
         "e": False,
         }
         
nodrake=["b","c","f","g","h","i","j","p","l","m","n","o","q","s","t","u",
         "v","w","x","y","z"]
beige = {
         "b": False,
         "e": False,
         "i": False,
         "g": False,
         "e": False,
         }
nobeige=["a","c","f","d","h","k","j","p","l","m","n","o","q","r","s","t","u",
         "v","w","x","y","z"]


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
    
def square2 (letter, x,w):
    global drake
    if drake[letter]:
        noFill()
    else:
        fill(0)
    if keyPressed:
        if key == letter :
            drake[letter]=True   
    rect(x, 475, w, 30)

# def square3(letter, x,w):
#      global beige
#      if beige[letter]:

#          noFill()
#      else:
#          fill(0)
#      if keyPressed:

#          if key == letter :
#              beige[letter]=True   
#      rect(x, 475, w, 30)
    
