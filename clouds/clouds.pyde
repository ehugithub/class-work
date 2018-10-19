def setup():
    vector = PVector(30, 30)
    size(1366, 768)
vector = PVector(40, 20)
vector2 = PVector(25, 50)
def draw():
    global vector
    global vector2
    ellipse(vector.x, vector2.y, 20, 20)
    #ellipse(vector2.x, vector2.y, 12, 12)
    vector2 += vector
    #ellipse(vector2.x, vector2.y, 24, 24)
x = 0
'''
def draw():
    global x
    global switch
    noStroke()
    if x >= 1366:
        switch = 1
    elif x <= 0:
        switch = 0
    if switch == 1:
        x -= 10
    else:
        x += 10
    fill(240)
    background(0,191,255)
    ellipse(x,120,100,50)
    ellipse(x + 50, 150, 110, 50)
    ellipse(x - 60, 150, 120, 50)
    ellipse(x - 30, 180, 110, 55)
    
    fill(0, 128, 0)
    rect(0, height-100, width, 100)'''
