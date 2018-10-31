import random

def setup():
    size(1366,700)

r = g = b = None
switch = True

def mousePressed():
    global switch
    if switch == True:
        switch = False
    else:
        switch = True
def draw():
    global r
    global g
    global b
    global switch
    global background
    '''if switch == True:
        loop()
    else:
        noLoop() '''
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    background(r,g,b)
    
    delay(500)
    
    fill(255)
    textSize(200)
    text('{},{},{}'.format(r,g,b), 100, height/2 + 100)
