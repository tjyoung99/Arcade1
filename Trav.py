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
         
# beige = {
#          "b": False,
#          "e": False,
#          "i": False,
#          "g": False,
#          "e": False,
#          }


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
    
# def squaree(x,w):
#      global alphabet

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

#      if e:
#          noFill()
#      else:
#          fill(0)
#      if keyPressed:
#          if key == 'e' :
#              alphabet=True   
#      rect(x, 475, w, 30)
    

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
