<<<<<<< HEAD
# from Arcade2 import *

# alphabet{
#          "a":false,
#          "b":false,
#          "c":false,
#          "d":false,
#          "e":false,
#          "g":false,
#          "h":false,
#          "i":false,
#          "k":false,
#          "l":false,
#          "m":false,
#          "n":false,
#          "o":false,
#          "p":false,
#          "r":false,
#          "s":false,
#          "w":false,
# }
      
# def squarea(x,w):
#     global alphabet
#     if alphabet["a"]:
#         noFill()
#     else:
#         fill(0)
#     if keyPressed:
#         if key == 'a' :
#             alphabet=True
#     rect(x, 475, w, 30)

# def squarep(x,w):
#      global alphabet
#      if p:
#          noFill()
#      else:
#          fill(0)
#      if keyPressed:
#          if key == 'p' :
#              alphabet=True   
#      rect(x, 475, w, 30)
    
    
# def squarel(x,w):
#      global alphabet
#      if l:
=======
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

# def squarep(x,w):
#      global alphabet
#      if alphabet["p"]:
>>>>>>> 2f0452cb1f9bb2ff4a4aa0764803b3767f19c119
#          noFill()
#      else:
#          fill(0)
#      if keyPressed:
<<<<<<< HEAD
#          if key == 'l' :
#              aplhabet=True   
#      rect(x, 475, w, 30)
    
# def squaree(x,w):
#      global alphabet
=======
#          if key == 'p' :
#              alphabet["p"]=True   
#      rect(x, 475, w, 30)
    
# def squarel(x,w):
#      global alphabet
#      if :
#          noFill()
#      else:
#          fill(0)
#      if keyPressed:
#          if key == 'l' :
#              alphabet=True   
#      rect(x, 475, w, 30)
    
# def squaree(x,w):
#      global alphabet 
>>>>>>> 2f0452cb1f9bb2ff4a4aa0764803b3767f19c119
#      if e:
#          noFill()
#      else:
#          fill(0)
#      if keyPressed:
#          if key == 'e' :
#              alphabet=True   
#      rect(x, 475, w, 30)
    
<<<<<<< HEAD
=======
# def squareb():
#     global alphabet
#     if b:
#         stroke()
#     else:
#         noStroke()
#     if keyPressed:
#         if key == 'b' :
#             alphabet=True   
#     ellipse (330, 120, 40, 40)
>>>>>>> 2f0452cb1f9bb2ff4a4aa0764803b3767f19c119
