<<<<<<< HEAD
from Arcade2 import * 
add_library('minim') 
from random import *
=======
from Arcade2 import *

>>>>>>> 118f9c2e9979b5ee9a6e5e97cfa5c4da577fb624
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

googler={"g": False,
         "o": False,
         "o": False,
         "g": False,
         "l": False,
         "e": False,
         "r": False,
         }
nogoogler=["a","c","f","d","h","k","j","p","i","m","n","b","q","s","t","u",
         "v","w","x","y","z"]

wings = {
         "w": False,
         "i": False,
         "n": False,
         "g": False,
         "s": False,
         }
nowings=["a","c","f","d","h","k","j","p","l","m","o","q","r","b","t","u",
         "v","e","x","y","z"]

march = {
         "m": False,
         "a": False,
         "r": False,
         "c": False,
         "h": False,
         }
nomarch=["w","s","f","d","g","k","j","p","l","n","o","q","i","b","t","u",
         "v","e","x","y","z"]
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

def square3(letter, x,w):
     global beige
     if beige[letter]:

         noFill()
     else:
         fill(0)
     if keyPressed:
         if key == letter :
             beige[letter]=True   
     rect(x, 475, w, 30)
    
def square4(letter, x,w):
     global googler
     if googler[letter]:

         noFill()
     else:
         fill(0)
     if keyPressed:

         if key == letter :
             googler[letter]=True   
     rect(x, 475, w, 30)
    
def square5(letter, x,w):
     global wings
     if wings[letter]:

         noFill()
     else:
         fill(0)
     if keyPressed:

         if key == letter :
             wings[letter]=True   
     rect(x, 475, w, 30)
     
def square6(letter, x,w):
     global march
     if march[letter]:

         noFill()
     else:
         fill(0)
     if keyPressed:

         if key == letter :
             march[letter]=True   
     rect(x, 475, w, 30)
<<<<<<< HEAD
def gameover (counter):
    if counter == 6:
        fill(0)
        rect(0, 0, 600, 600)
        textSize(60)
        fill(randint(0,255),randint(0,255),randint(0,255))
        text("GAME OVER", 125, 300)
   
    
    
=======
     
>>>>>>> 118f9c2e9979b5ee9a6e5e97cfa5c4da577fb624
