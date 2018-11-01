import random
def setup():
  size(1366, 700)
  smooth()
  background(255)

location = PVector(683, 350)
velocity = PVector(10, 10)

class Paddle:
    pass

left = 0
right = 0
left_pos = right_pos = 300.00

def score_point():
    global right
    global left
    global location
    if location.x > width + 200:
        right += 1
        location = PVector(width / 2, height / 2)
    elif location.x < -200:
        left += 1
        location = PVector(width / 2, height / 2)

def draw():
    global velocity
    background(255)
    
    fill(255)
    fill(0)
    score_point()
    textSize(150)
    text('{}     {}'.format(left, right), 450, 200)
    
    ellipse(location.x, location.y, 40, 40)
    location.add(velocity)
    
    if location.y > height - 20 or location.y < 20:
        velocity.y *= -1
        
    rect(10, left_pos, 15, 200)
    rect(1341, right_pos, 15, 200)
    
def keyPressed():
    global left_pos
    global right_pos
    smooth()
    if key == 'a':
        left_pos -= 10
    elif key == 'd':
        left_pos += 10
    elif keyCode == LEFT:
        right_pos -= 10
    elif keyCode == RIGHT:
        right_pos += 10
