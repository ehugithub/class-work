import random
def setup():
  size(1366,700)
  background(255)

location = PVector(683, 350)
velocity = PVector(10, 10)

'''class paddle:
    
    rect(    '''

left = 0
right = 0
def score_point():
    global right
    global left
    global location
    if location.x > width + 20:
        right += 1
        location = PVector(width/2, height/2)
        delay(300)
    elif location.x < -20:
        left+= 1
        location = PVector(width/2, height/2)
        delay(300)
def  draw():
    global velocity
    global location
    background(255)
    textSize(150)
    fill(0)
    score_point()
    text('{}     {}'.format(left,right), 450, 200)
    
    noStroke()
    fill(0)
    ellipse(location.x,location.y,40,40)
    location.add(velocity)
    if location.x > width + 20 or location.x < -20:
        velocity.x *= -1
    if location.y > height - 20 or location.y < 20:
        velocity.y *= -1 '''
