import random
def setup():
    size(666,700)

position = PVector(421, 35)
left = False
right = False
def create_shape(x,y):
    global shape
    global left
    global right
    num = random.randrange(1,4)
    return rect(x,y, 70, 70)
def draw():
    global position
    # delay(800)
    background(0)
    line(316, 0, 316, height)
    stroke(128)
    position.x = constrain(position.x, 316, width - 70)
    for i in range(316,  width, 35):
        line(i, 0 , i, height)
    for i in range(0, height, 35):
        line(316, i, width, i)
    create_shape(position.x,position.y)
    position.y += 1
def keyPressed():
    if keyCode == LEFT:
        position.x -= 35
    elif keyCode == RIGHT:
        position.x += 35
    elif keyCode == UP:
        pushMatrix()
        translate(position.x, position.y)
        rotate(PI/4.0)
        fill(255,0,0)
        create_shape(0,0)
        fill(255)
        popMatrix()
