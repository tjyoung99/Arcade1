from Arcade2 import *


def startup():
    fill(255,0,0)
    text ("Start", 260, 300)
    # noFill()
    # rect(250, 300, 80, 60)
    
def wallpaper():
    img = loadImage("mount.png")
    image(img, 0, 0, height, width)

def Exit():
    fill(0)
    rect(550, 550, 50, 50)
    fill(255)
    text ("Exit", 560, 580)
    

    

       



        


        
