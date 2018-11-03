import random
def setup():
  size(1366, 700)
  smooth()
  background(255)

location = PVector(683.0, 350.0)
velocity = PVector(10.0, 10.0)

keypress = [False] * 4

left = right = speed = 0
left_pos = right_pos = 300.00

def score_point():
    global location
    location = PVector(width / 2, height / 2)
    velocity.x = 10.0
    velocity.y = 10.0
    delay(300)

def draw():
    global left_pos
    global right_pos
    global left
    global right
    frameRate(100)
    background(255)
    fill(255)
    fill(0)
    textSize(150)
    text('{}     {}'.format(left, right), 450, 200)
    
    ellipse(location.x, location.y, 40, 40)
    location.add(velocity)
    
    if location.y > height - 20 or location.y < 20:
        velocity.y *= -1

    left_pos = constrain(left_pos, 0, 500)
    right_pos = constrain(right_pos, 0, 500)
    
    if location.x > width + 50:
        left += 1
        score_point()
    elif location.x < -50:
        right += 1
        score_point()
    rect(10, left_pos, 15, 200)
    rect(1341, right_pos, 15, 200)
    
    if location.x > 1331 and location.y + 25 > right_pos and location.y < right_pos + 175 or location.x < 40 and location.y + 25 > left_pos and location.y < left_pos + 175:
        if velocity.x > 0:
            velocity.x += 0.25
        elif velocity.x < 0:
            velocity.x -= 0.25
        if velocity.y > 0:
            velocity.y += 0.25
        elif velocity.y < 0:
            velocity.y -= 0.25
        velocity.x *= -1
        if location.x > 1331:
            location.x = 1331
        else:
            location.x = 40
    
    if keypress[0] == True:
        left_pos -= 10
    elif keypress[1] == True:
        left_pos += 10
    elif keypress[2] == True:
        right_pos -= 10
    elif keypress[3] == True:
        right_pos += 7

def keyPressed():
    if key == 'a':
        keypress[0] = True
    elif key == 'd':
        keypress[1] = True
    elif keyCode == LEFT:
        keypress[2] = True
    elif keyCode == RIGHT:
        keypress[3] = True
        
def keyReleased():
    if key == 'a':
        keypress[0] = False
    elif key == 'd':
        keypress[1] = False
    elif keyCode == LEFT:
        keypress[2] = False
    elif keyCode == RIGHT:
        keypress[3] = False
