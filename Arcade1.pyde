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
    

   
def keyReleased():
    global counter
    if key =='b':
        counter=counter+1
    if key =='c':
        counter=counter+1
    if key =='d':
        counter=counter+1
    if key =='f':
        counter=counter+1
    if key =='g':
        counter=counter+1
    if key =='h':
        counter=counter+1
    if key =='i':
        counter=counter+1
    if key =='j':
        counter=counter+1
    if key =='k':
        counter=counter+1
    if key =='m':
        counter=counter+1
    if key =='n':
        counter=counter+1
    if key =='o':
        counter=counter+1
    if key =='q':
        counter=counter+1
    if key =='r':
        counter=counter+1
    if key =='s':
        counter=counter+1
    if key =='t':
        counter=counter+1
    if key =='u':
        counter=counter+1
    if key =='v':
        counter=counter+1
    if key =='w':
        counter=counter+1
    if key =='x':
        counter=counter+1
    if key =='y':
        counter=counter+1
    if key =='z':
        counter=counter+1
    if key =='a':
        noFill()
    else:
        fill(0)
    rect(260, 475, 18, 30)

    

   

    
    
