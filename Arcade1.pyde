from random import * 
from Arcade2 import *
from Trav import* 
from words import *

counter=0
def setup(): 
    size(600,600)
    man1()
   
    
def draw():
    background(255)
    hangman()
    man(counter)
    apple()
    # drake()
    # beige()
    

   
def keyReleased():
    global counter
    for letters in range (len (noapple)):
        if key == noapple[letters]:
            counter=counter+1
    
    # if key =='b':
    #     counter=counter+1
    # if key =='c':
    #     counter=counter+1
    # if key =='d':
    #     counter=counter+1
    # if key =='f':
    #     counter=counter+1
    # if key =='g':
    #     counter=counter+1
    # if key =='h':
    #     counter=counter+1
    # if key =='i':
    #     counter=counter+1
    # if key =='j':
    #     counter=counter+1
    # if key =='k':
    #     counter=counter+1
    # if key =='m':
    #     counter=counter+1
    # if key =='n':
    #     counter=counter+1
    # if key =='o':
    #     counter=counter+1
    # if key =='q':
    #     counter=counter+1
    # if key =='r':
    #     counter=counter+1
    # if key =='s':
    #     counter=counter+1
    # if key =='t':
    #     counter=counter+1
    # if key =='u':
    #     counter=counter+1
    # if key =='v':
    #     counter=counter+1
    # if key =='w':
    #     counter=counter+1
    # if key =='x':
    #     counter=counter+1
    # if key =='y':
    #     counter=counter+1
    # if key =='z':
    #     counter=counter+1

    

    

   

    
    
