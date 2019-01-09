import random

def setup():
    size(1366,700)

r = g = b = None

def draw():
    global r, g, b, background
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    background(r,g,b)
    
    delay(500)
    
    fill(255)
    textSize(200)
    text('{},{},{}'.format(r,g,b), 100, height/2 + 100)
