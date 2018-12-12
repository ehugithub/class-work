import random
import copy
from itertools import count
def setup():
    size(666,700)
shape_list = []
newshape = False
angle = 0
position = PVector(421, 35)
left = False
right = False
num = random.randrange(1,8)

class block:
    _ids = count(0)
    def __init__(self, shapenum, posx, posy):
        self.shapenum = shapenum
        self.x= posx
        self.y= posy
        self.id = next(self._ids)
    def randnum(self):
        self.shapenum = random.randrange(1,8)
    def create_shape(self):
        strokeWeight(3)
        strokeCap(PROJECT)
        stroke(0, 0, 0)
        global shape
        global left
        global right
        if self.shapenum == 1:
            # 'I' block
            fill(0, 255, 255)
            rect(self.x, self.y , 35, 140)
            line(self.x, self.y + 35 , self.x + 35, self.y + 35)
            line(self.x, self.y + 70, self.x + 35, self.y + 70)
            line(self.x, self.y + 105, self.x + 35, self.y + 105)
        elif self.shapenum == 2:
            # Square block
            fill(255, 255, 0)
            rect(self.x ,self.y , 70, 70)
            line(self.x + 35,self.y , self.x + 35, self.y + 70)
            line(self.x, self.y + 35, self.x + 70, self.y + 35)
        elif self.shapenum == 3:
            # 'T' block
            fill(255, 0, 255)
            beginShape()
            vertex(self.x, self.y )
            vertex(self.x, self.y + 35)
            vertex(self.x - 35, self.y + 35)
            vertex(self.x - 35, self.y + 70)
            vertex(self.x + 70, self.y + 70)
            vertex(self.x + 70, self.y + 35)
            vertex(self.x + 35, self.y + 35)
            vertex(self.x + 35, self.y )
            endShape(CLOSE)
            line(self.x, self.y + 35, self.x + 35, self.y + 35)
            line(self.x, self.y + 35, self.x, self.y + 70)
            line(self.x + 35,self.y + 35, self.x + 35,self.y + 70)
        elif self.shapenum == 4:
            #'L' block
            fill(255, 165, 0) 
            beginShape()
            vertex(self.x + 70, self.y )
            vertex(self.x + 70, self.y + 35)
            vertex(self.x, self.y + 35)
            vertex(self.x, self.y + 70)
            vertex(self.x + 105,self.y + 70)
            vertex(self.x + 105,self.y )
            endShape(CLOSE)
            line(self.x + 35, self.y + 35, self.x + 35, self.y + 70)
            line(self.x + 70, self.y + 35, self.x + 70, self.y + 70)
            line(self.x + 70, self.y + 35, self.x + 105, self.y + 35)
        elif self.shapenum == 5:
            # 'J' block
            fill(0, 0, 255)
            beginShape()
            vertex(self.x, self.y )
            vertex(self.x, self.y + 70)
            vertex(self.x + 105, self.y + 70)
            vertex(self.x + 105, self.y + 35)
            vertex(self.x + 35, self.y + 35)
            vertex(self.x + 35, self.y )
            endShape(CLOSE)
            line(self.x, self.y + 35, self.x + 35, self.y + 35)
            line(self.x + 35,self.y + 35, self.x + 35, self.y + 70)
            line(self.x + 70, self.y + 35, self.x + 70, self.y + 70)
        elif self.shapenum == 6:
            # 'S' block
            fill(0, 255, 0)
            beginShape()
            vertex(self.x, self.y )
            vertex(self.x, self.y + 35)
            vertex(self.x - 35, self.y + 35)
            vertex(self.x - 35, self.y + 70)
            vertex(self.x + 35, self.y + 70)
            vertex(self.x + 35, self.y + 35)
            vertex(self.x + 70, self.y + 35)
            vertex(self.x + 70, self.y )
            endShape(CLOSE)
            line(self.x, self.y + 35, self.x + 35, self.y + 35)
            line(self.x, self.y + 35, self.x, self.y + 70)
            line(self.x + 35, self.y , self.x + 35, self.y + 35)
        elif self.shapenum == 7:
            # 'Z' block
            fill(255, 0, 0)
            beginShape()
            vertex(self.x, self.y )
            vertex(self.x, self.y + 35)
            vertex(self.x + 35, self.y + 35)
            vertex(self.x + 35, self.y + 70)
            vertex(self.x + 105, self.y + 70)
            vertex(self.x + 105, self.y + 35)
            vertex(self.x + 70, self.y + 35)
            vertex(self.x + 70, self.y )
            endShape(CLOSE)
            line(self.x + 35, self.y, self.x + 35, self.y + 35)
            line(self.x + 35, self.y + 35, self.x + 70, self.y + 35)
            line(self.x + 70, self.y + 35, self.x + 70, self.y + 70)
            line(self.x + 70, self.y+ 35, self.x + 70, self.y+ 70)
    def stay(self):
        if self.shapenum == 1:
            if angle % 360 == 0:
                position.x= constrain(position.x, 316, width - 35)
            elif angle % 360 == 90:
                position.x= constrain(position.x, 386,  width - 70)
            elif angle % 360 == 180:
                position.x= constrain(position.x, 281, width - 70)
            elif angle & 360 == 270:
                position.x= constrain(position.x, 316, width - 140)
        elif self.shapenum == 2:
            position.x= constrain(position.x, 316, width - 70)
        elif self.shapenum == 3:
            if angle % 360 == 0:
                position.x = constrain(position.x, 351, width - 70)
            elif angle % 360 == 90:
                position.x= constrain(position.x, 316, width - 70)
            elif angle % 360 == 180:
                position.x= constrain(position.x, 316, width - 105)
            elif angle % 360 == 270:
                position.x= constrain(position.x, 316, width - 70)
        elif self.shapenum == 4 or self.shapenum == 5:
            if angle % 360 == 0:
                position.x= constrain(position.x, 316, width - 105)
            elif angle % 360 == 90:
                position.x= constrain(position.x, 316, width - 70)
            elif angle % 360 == 180:
                position.x= constrain(position.x, 351, width - 70)
            elif angle % 360 == 270:
                position.x= constrain(position.x, 316, width - 70)
        elif self.shapenum == 6:
            if angle % 360 == 0:
                position.x= constrain(position.x, 351, width - 70)
            elif angle % 360 == 90 or angle % 360 == 270:
                position.x= constrain(position.x, 316, width - 70)
            elif angle % 360 == 180:
                position.x= constrain(position.x, 316, width - 105)
        elif self.shapenum == 7:
            if angle % 360 == 0:
                position.x= constrain(position.x, 316, width - 105)
            elif angle % 360 == 90 or angle % 360 == 270:
                position.x= constrain(position.x, 316, width - 70)
            elif angle % 360 == 180:
                position.x= constrain(position.x, 351, width - 70)
    def highlight(self):
        pushMatrix()
        translate(position.x + 35, 670)
        rotate(radians(angle))
        tetro.create_shape()
        popMatrix()
    def copyshape(self):
        shape_list.append(copy.deepcopy(tetro))
tetro = block(num, -35, -35)
def draw():
    global position, angle, num, newshape, shape_list
    strokeWeight(1)
    background(0)
    line(316, 0, 316, height)
    stroke(128)
    for i in range(316,  width, 35):
        line(i, 0 , i, height)
    for i in range(0, height, 35):
        line(316, i, width, i)
        
    tetro.stay()
    pushMatrix()
    translate(position.x + 35, position.y + 35)
    rotate(radians(angle))
    tetro.create_shape()
    popMatrix()
    
    tetro.highlight()
    
    position.y += 1
    if position.y >= height - 70:
        angle = 0
        position.set([421, 35])
        tetro.randnum()
        tetro.copyshape()
        newshape = True
    if newshape == True:
        for i in shape_list:
            i.create_shape()
    if mousePressed:
        print(getattr(shape_list[3], "shapenum"))
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
    elif key== ' ':
        position.y += 35
