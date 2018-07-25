a=False
p=False
l=False
e=False
b=False
def squarea(x,w):
    global a, p, l, e
    if a:
        noFill()
    else:
        fill(0)
    if keyPressed:
        if key == 'a' :
            a=True   
    rect(x, 475, w, 30)

def squarep(x,w):
    global a, p, l, e
    if p:
        noFill()
    else:
        fill(0)
    if keyPressed:
        if key == 'p' :
            p=True   
    rect(x, 475, w, 30)
    
    
def squarel(x,w):
    global a, p, l, e
    if l:
        noFill()
    else:
        fill(0)
    if keyPressed:
        if key == 'l' :
            l=True   
    rect(x, 475, w, 30)
    
def squaree(x,w):
    global a, p, l, e
    if e:
        noFill()
    else:
        fill(0)
    if keyPressed:
        if key == 'e' :
            e=True   
    rect(x, 475, w, 30)
    
#def squareb():
    #global a, b, p, l, e
    #if b:
     #   stroke()
   # else:
     #   noStroke()
    #if keyPressed:
      #  if key == 'b' :
       #     b=True   
   # ellipse (330, 120, 40, 40)
