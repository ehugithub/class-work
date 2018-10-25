def setup():
    background(0,191,255)
    size(1366, 768)
x = 0
sun = 0
moon = -10000
def draw():
    global x
    global sun
    global moon
    global switch
    global background
    noStroke()
    if x >= 1311:
        switch = 1
    elif x <= 55:
        switch = 0
    if switch == 1:
        x -= 2
    else:
        x += 2
    fill(240)
    
    if sun <= 1466:
        background(0,191,255)
    else:
        background(10,15,68)
    
    fill(255,255,0)
    ellipse(sun, 200, 200, 200)
    sun += 1
    
    fill(254,252,215)
    ellipse(moon, 100, 200, 200)
    moon += 1

    if sun == 1466:
        moon = -10
    elif moon == 1466:
        sun = -10
        
    fill(196,188,188)
    stroke(1)
    triangle(0, 768, 1366, 768, width/2, 100)
    triangle(600, 768, 1366, 768, 4*width/5, 50)
    triangle(-500, 768, 866, 768, width/5, 200)
    fill(240,248,245)
    triangle(580, 200, 784, 200, width/2, 100)
    triangle(204, 250, 325, 250, width/5, 200)
    triangle(1023, 150, 1130, 150, 4*width/5, 50)
    
    noStroke()
    fill(216,237,242)
    ellipse(x,120,100,50)
    ellipse(x + 50, 150, 110, 50)
    ellipse(x - 60, 150, 120, 50)
    ellipse(x - 30, 180, 110, 55)
    
    fill(0, 128, 0)
    rect(0, height-100, width, 100)
