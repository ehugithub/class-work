import random
import time

def setup():
    size(1366,700)

r = g = b = None
switch = 1


def mousePressed():
    global switch
    if switch == 1:
        switch = 0
    else:
        switch = 1

def draw():
    global r
    global g
    global b
    global switch
    global background
    if switch == 1:
        continue
    else:
        pass
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    background(r,g,b)
    
    time.sleep(0.5)
    
    fill(255)
    textSize(200)
    text('{},{},{}'.format(r,g,b), 100, height/2 + 100)
