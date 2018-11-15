def setup():
  size(1366, 700)
  smooth()
  background(255)

location = PVector(683.0, 350.0)
velocity = PVector(10.0, 10.0)

keypress = [False] * 4
left = right = speed = 0
left_pos = right_pos = 300.00
new_game = True
single_player = None
difficulty = 0

def start_game():
    global new_game
    global single_player
    global difficulty
    global left
    global right
    left = right = 0
    velocity.set([0,0])
    background(255)
    if single_player != True:
        fill(128)
        rect(300, 340, 300, 100)
        rect(800, 340, 300, 100)
        textSize(40)
        fill(0)
        text('Single Player', 320, 410)
        text('Multiplayer', 830, 410)
    
    if mousePressed == True and mouseY > 340 and mouseY < 440 and mouseX > 300 and mouseX < 600:
        single_player = True
        background(255)
    elif mousePressed == True and mouseY > 340 and mouseY < 440 and mouseX > 800 and mouseX < 1100:
        new_game = False
        velocity.set([10.0,10.0])
    
    if single_player == True:
        fill(0)
        textSize(100)
        text('Select Difficulty', 350, 300)
        fill(128)
        rect(40, 370, 300, 100)
        rect(540, 370, 300, 100)
        rect(1040, 370, 300, 100)
        rect(540, 570, 300, 100)
        textSize(40)
        fill(0)
        text('Easy', 140, 420)
        text('Medium', 600, 420)
        text('Hard', 1140, 420)
        text('Impossible', 580, 630)
    
    if mousePressed == True and mouseY > 370 and mouseY < 470 and mouseX > 40 and mouseX < 340:
        difficulty = 1
        new_game = False
        velocity.set([10.0, 10.0])
    elif mousePressed == True and mouseY > 370 and mouseY < 470 and mouseX > 540 and mouseX < 840:
        difficulty = 2
        new_game = False
        velocity.set([10.0, 10.0])
    elif mousePressed == True and mouseY > 370 and mouseY < 470 and mouseX > 1040 and mouseX < 1340:
        difficulty = 3
        new_game = False
        velocity.set([10.0, 10.0])
    elif mousePressed == True and mouseY > 570 and mouseY < 670 and mouseX > 540 and mouseX < 840:
        difficulty = 10
        new_game = False
        velocity.set([10.0, 10.0])
        
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
    global difficulty
    global new_game
    frameRate(100)
    background(255)
    
    if new_game == True:
        start_game()
    if left == 11:
        fill(255,0,0)
        textSize(80)
        text('Red wins! Click to play again', 150, 330)
        velocity.set([0.0, 0.0])
        if mousePressed == True:
            new_game = True
    elif right == 11:
        fill(0,0,255)
        textSize(80)
        text('Blue wins! Click to play again', 150, 330)
        velocity.set([0.0, 0.0])
        if mousePressed == True:
            new_game = True
    fill(0)
    textSize(150)
    text('{}     {}'.format(left, right), 450, 200)
    ellipse(location.x, location.y, 40, 40)
    location.add(velocity)
    
    left_pos = constrain(left_pos, 0, 500)
    right_pos = constrain(right_pos, 0, 500)
    
    if location.y > height - 20 or location.y < 20:
        velocity.y *= -1
    if location.x > width + 50:
        left += 1
        score_point()
        left_pos = right_pos = 300
    elif location.x < -50:
        right += 1
        score_point()
        left_pos = right_pos = 300
    
    #Paddles
    noStroke()
    fill(255,0,0)
    rect(10, left_pos, 15, 200)
    fill(0,0,255)
    rect(1341, right_pos, 15, 200)
        
    if location.x > 1331 and location.y > right_pos and location.y < right_pos + 200 or location.x < 40 and location.y > left_pos and location.y < left_pos + 200:
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

    if keypress[0]:
        left_pos -= 10
    if keypress[1]:
        left_pos += 10
    if keypress[2]:
        right_pos -= 10
    if keypress[3]:
        right_pos += 10
    
    if single_player == True:
        if location.y > left_pos + 150:
            left_pos += difficulty * 5
        elif location.y < left_pos + 150:
            left_pos -= difficulty * 5
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
