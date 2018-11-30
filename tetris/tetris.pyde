import random
def setup():
    size(666,700)
angle = 0
position = PVector(421, 35)
left = False
right = False
num = random.randrange(1,8)
def randnum():
    global num
    num = random.randrange(1,8)
    print(num)
def create_shape(num, x,y):
    strokeWeight(3)
    strokeCap(PROJECT)
    stroke(0, 0, 0)
    global shape
    global left
    global right
    if num == 1:
      # 'I' block
      fill(0, 255, 255)
      rect(x,y, 35, 140)
      line(x, y + 35 , x + 35, y + 35)
      line(x, y + 70, x + 35, y + 70)
      line(x, y + 105, x + 35, y + 105)
    elif num == 2:
      # Square block
      fill(255, 255, 0)
      rect(x, y, 70, 70)
      line(x + 35, y, x + 35, y + 70)
      line(x, y + 35, x + 70, y + 35)
    elif num == 3:
      # 'T' block
      fill(255, 0, 255)
      beginShape()
      vertex(x, y)
      vertex(x, y + 35)
      vertex(x - 35, y + 35)
      vertex(x - 35, y + 70)
      vertex(x + 70, y + 70)
      vertex(x + 70, y + 35)
      vertex(x + 35, y + 35)
      vertex(x + 35, y)
      endShape(CLOSE)
      line(x, y + 35, x + 35, y + 35)
      line(x, y + 35, x, y + 70)
      line(x + 35, y + 35, x + 35, y + 70)
    elif num == 4:
      #'L' block
      fill(255, 165, 0) 
      beginShape()
      vertex(x + 70, y)
      vertex(x + 70, y + 35)
      vertex(x, y + 35)
      vertex(x, y + 70)
      vertex(x + 105, y + 70)
      vertex(x + 105, y)
      endShape(CLOSE)
      line(x + 35, y + 35, x  + 35, y + 70)
      line(x + 70, y + 35, x + 70, y + 70)
      line(x + 70, y + 35, x + 105, y + 35)
    elif num == 5:
      # 'J' block
      fill(0, 0, 255)
      beginShape()
      vertex(x, y)
      vertex(x, y + 70)
      vertex(x + 105, y + 70)
      vertex(x + 105, y + 35)
      vertex(x + 35, y + 35)
      vertex(x + 35, y)
      endShape(CLOSE)
      line(x, y + 35, x + 35, y + 35)
      line(x + 35, y + 35, x + 35, y + 70)
      line(x + 70, y + 35, x + 70, y + 70)
    elif num == 6:
      # 'S' block
      fill(0, 255, 0)
      beginShape()
      vertex(x, y)
      vertex(x, y + 35)
      vertex(x - 35, y + 35)
      vertex(x - 35, y + 70)
      vertex(x + 35, y + 70)
      vertex(x + 35, y + 35)
      vertex(x + 70, y + 35)
      vertex(x + 70, y)
      endShape(CLOSE)
      line(x, y + 35, x + 35, y + 35)
      line(x, y + 35, x, y + 70)
      line(x + 35, y, x + 35, y + 35)
    elif num == 7:
      # 'Z' block
      fill(255, 0, 0)
      beginShape()
      vertex(x, y)
      vertex(x, y + 35)
      vertex(x + 35, y + 35)
      vertex(x + 35, y + 70)
      vertex(x + 105, y + 70)
      vertex(x + 105, y + 35)
      vertex(x + 70, y + 35)
      vertex(x + 70, y)
      endShape(CLOSE)
      line(x + 35, y, x + 35, y + 35)
      line(x + 35, y + 35, x + 70, y + 35)
      line(x + 70, y + 35, x + 70, y + 70)
def draw():
    global position
    global angle
    global num
    strokeWeight(1)
    background(0)
    line(316, 0, 316, height)
    stroke(128)
    position.x = constrain(position.x, 316, width - 70)
    for i in range(316,  width, 35):
        line(i, 0 , i, height)
    for i in range(0, height, 35):
        line(316, i, width, i)
        
    pushMatrix()
    translate(position.x + 35, position.y + 35)
    rotate(radians(angle))
    create_shape(num, -35, -35)
    popMatrix()
    position.y += 1
    
    if position.y >= height - 70:
        position.set([421, 35])
        randnum()
def keyPressed():
    global angle
    if keyCode == LEFT:
        position.x -= 35
    elif keyCode == RIGHT:
        position.x += 35
    elif keyCode == UP:
        angle += 90
    elif keyCode == DOWN:
        angle -= 90
    elif key == ' ':
        position.y += 35
