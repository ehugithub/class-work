import random
import copy
from itertools import count
def setup():
    size(666,700)
shape_list = []
newshape = False
num = random.randrange(1,8)
tempx = tempy = tempangle = None
class block:
    _ids = count(0)
    def __init__(self, shapenum, x, y, angle):
        self.shapenum = shapenum
        self.angle = angle
        self.x = x
        self.y = y
        self.id = next(self._ids)
    def randnum(self):
        self.shapenum = random.randrange(1,8)
    def create_shape(self):
        strokeWeight(3)
        strokeCap(PROJECT)
        stroke(0, 0, 0)
        global shape
        rotate(radians(self.angle))
        if self.shapenum == 1:
            # 'I' block
            fill(0, 255, 255)
            rect(-35, -35 , 35, 140)
            line(-35, 0 , 0, 0)
            line(-35, 35, 0, 35)
            line(-35, 70, 0, 70)
        elif self.shapenum == 2:
            # Square block
            fill(255, 255, 0)
            rect(-35 ,-35 , 70, 70)
            line(0,-35 , 0, 35)
            line(-35, 0, 35, 0)
        elif self.shapenum == 3:
            # 'T' block
            fill(255, 0, 255)
            beginShape()
            vertex(-35, -35 )
            vertex(-35, 0)
            vertex(-35 - 35, 0)
            vertex(-35 - 35, 35)
            vertex(35, 35)
            vertex(35, 0)
            vertex(0, 0)
            vertex(0, -35 )
            endShape(CLOSE)
            line(-35, 0, 0, 0)
            line(-35, 0, -35, 35)
            line(0,0, 0,35)
        elif self.shapenum == 4:
            #'L' block
            fill(255, 165, 0) 
            beginShape()
            vertex(35, -35)
            vertex(35, 0)
            vertex(-35, 0)
            vertex(-35, 35)
            vertex(70,35)
            vertex(70,-35 )
            endShape(CLOSE)
            line(0, 0, 0, 35)
            line(35, 0, 35, 35)
            line(35, 0, 70, 0)
        elif self.shapenum == 5:
            # 'J' block
            fill(0, 0, 255)
            beginShape()
            vertex(-35, -35)
            vertex(-35, 35)
            vertex(70, 35)
            vertex(70, 0)
            vertex(0, 0)
            vertex(0, -35)
            endShape(CLOSE)
            line(-35, 0, 0, 0)
            line(0,0, 0, 35)
            line(35, 0, 35, 35)
        elif self.shapenum == 6:
            # 'S' block
            fill(0, 255, 0)
            beginShape()
            vertex(-35, -35 )
            vertex(-35, 0)
            vertex(-35 - 35, 0)
            vertex(-35 - 35, 35)
            vertex(0, 35)
            vertex(0, 0)
            vertex(35, 0)
            vertex(35, -35 )
            endShape(CLOSE)
            line(-35, 0, 0, 0)
            line(-35, 0, -35, 35)
            line(0, -35 , 0, 0)
        elif self.shapenum == 7:
            # 'Z' block
            fill(255, 0, 0)
            beginShape()
            vertex(-35, -35 )
            vertex(-35, 0)
            vertex(0, 0)
            vertex(0, 35)
            vertex(70, 35)
            vertex(70, 0)
            vertex(35, 0)
            vertex(35, -35 )
            endShape(CLOSE)
            line(0, -35, 0, 0)
            line(0, 0, 35, 0)
            line(35, 0, 35, 35)
            line(35, -35 + 35, 35, -35 + 70)
    def stay(self):
        if self.shapenum == 1:
            if self.angle % 360 == 0:
                self.x = constrain(self.x, 316, width - 35)
                self.y = constrain(self.y, 0, height - 140)
            elif self.angle % 360 == 90:
                self.x = constrain(self.x, 386,  width - 70)
                self.y = constrain(self.y, 0, height - 35)
            elif self.angle % 360 == 180:
                self.x = constrain(self.x, 281, width - 70)
                self.y = constrain(self.y, 0, height - 70)
            elif self.angle % 360 == 270:
                self.x = constrain(self.x, 316, width - 140)
                self.y = constrain(self.y, 0, height - 70)
        elif self.shapenum == 2:
            self.x = constrain(self.x, 316, width - 70)
            self.y = constrain(self.y, 0, height - 70)
        elif self.shapenum == 3:
            if self.angle % 360 == 0:
                self.x = constrain(self.x, 351, width - 70)
                self.y = constrain(self.y, 0, height - 70)
            elif self.angle % 360 == 90:
                self.x = constrain(self.x, 316, width - 70)
                self.y = constrain(self.y, 0, height - 70)
            elif self.angle % 360 == 180:
                self.x = constrain(self.x, 316, width - 105)
                self.y = constrain(self.y, 0, height - 70)
            elif self.angle % 360 == 270:
                self.x = constrain(self.x, 316, width - 70)
                self.y = constrain(self.y, 0, height - 105)
        elif self.shapenum == 4 or self.shapenum == 5:
            if self.angle % 360 == 0:
                self.x = constrain(self.x, 316, width - 105)
                self.y = constrain(self.y, 0, height - 70)
            elif self.angle % 360 == 90:
                self.x = constrain(self.x, 316, width - 70)
                self.y = constrain(self.y, 0, height - 105)
            elif self.angle % 360 == 180:
                self.x = constrain(self.x, 351, width - 70)
                self.y = constrain(self.y, 0, height - 70)
            elif self.angle % 360 == 270:
                self.x = constrain(self.x, 316, width - 70)
                self.y = constrain(self.y, 0, height - 70)
        elif self.shapenum == 6:
            if self.angle % 360 == 0 or self.angle % 360 == 90:
                self.x = constrain(self.x, 351, width - 70)
                self.y = constrain(self.y, 0, height - 70)
            elif self.angle % 360 == 270:
                self.x = constrain(self.x, 316, width - 70)
                self.y = constrain(self.y, 0, height - 105)
            elif self.angle % 360 == 180:
                self.x = constrain(self.x, 316, width - 105)
                self.y = constrain(self.y, 0, height - 70)
        elif self.shapenum == 7:
            if self.angle % 360 == 0:
                self.x = constrain(self.x, 316, width - 105)
                self.y = constrain(self.y, 0, height - 70)
            elif self.angle % 360 == 90:
                self.x = constrain(self.x, 316, width - 70)
                self.y = constrain(self.y, 0, height - 105)
            elif self.angle % 360 == 180:
                self.x = constrain(self.x, 351, width - 70)
                self.y = constrain(self.y, 0, height - 70)
            elif self.angle % 360 == 270:
                self.x = constrain(self.x, 316, width - 70)
                self.y = constrain(self.y, 0, height - 70)
    def highlight(self):
        if self.shapenum == 1:
            if self.angle % 360 == 0:
                translate(self.x + 35, 595)
            elif self.angle % 360 == 90:
                translate(self.x + 35, 700)
            elif tetro.angle % 360 == 180 or self.angle % 360 == 270:
                translate(self.x + 35, 665)
        elif self.shapenum == 2:
            translate(self.x + 35, 665)
        elif self.shapenum == 3:
            if self.angle % 360 != 270:
                translate(self.x + 35, 665)
            else:
                translate(self.x + 35, 630)
        elif self.shapenum == 4 or self.shapenum == 5:
            if self.angle % 360 != 90:
                translate(self.x + 35, 665)
            else:
                translate(self.x + 35, 630)
        elif self.shapenum == 6:
            if self.angle % 360 !=270:
                translate(self.x + 35, 665)
            else:
                translate(self.x + 35, 635)
        elif self.shapenum == 7:
            if self.angle % 360 != 90:
                translate(self.x + 35, 665)
            else:
                translate(self.x + 35, 630)
        tetro.create_shape()
    def copyshape(self):
        shape_list.append(copy.deepcopy(tetro))
    def reached_end(self):
        global newshape
        self.copyshape()
        self.randnum()
        self.x = 421
        self.y = 35
        newshape = True
        self.angle = 0
tetro = block(3, 421, 35, 0)
def draw():
    global position, angle, num, newshape, shape_list
    global tempx, tempy, tempangle
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
    translate(tetro.x + 35, tetro.y + 35)
    tetro.create_shape()
    popMatrix()
    
    pushMatrix()
    # tetro.highlight()
    popMatrix()
    
    tetro.y += 1
    
    
    if tetro.shapenum == 1:
        if tetro.angle % 360 == 0 and tetro.y >= height - 140:
            tetro.reached_end()
        elif tetro.angle % 360 == 90 and tetro.y >= height - 35:
            tetro.reached_end()
        elif tetro.angle % 360 == 180 and tetro.y >= height - 70:
            tetro.reached_end()
        elif tetro.angle % 360 == 270 and tetro.y >= height - 70:
            tetro.reached_end()
    elif tetro.shapenum == 2:
        if tetro.y >= height - 70:
            tetro.reached_end()
    elif tetro.shapenum == 3:
        if tetro.angle % 360 == 0 or tetro.angle % 360 == 90 or tetro.angle % 360 == 180: 
            if tetro.y >= height - 70:
                tetro.reached_end()
        elif tetro.angle % 360 == 270 and tetro.y >= height - 105:
            tetro.reached_end()
    elif tetro.shapenum == 4 or tetro.shapenum == 5:
        if tetro.angle % 360 == 0 or tetro.angle % 360 == 180:
            if tetro.y >= height - 70:
                tetro.reached_end()
        elif tetro.angle % 360 == 90 and tetro.y >= height - 105:
            tetro.reached_end()
        elif tetro.angle % 360 == 270 and tetro.y >= height - 70:
            tetro.reached_end()
    elif tetro.shapenum == 6 or tetro.shapenum == 7:
        if tetro.angle % 360 == 0 or tetro.angle % 360 == 180:
            if tetro.y >= height - 70:
                tetro.reached_end()
        elif tetro.angle % 360 == 90 and tetro.y >= height - 105:
            tetro.reached_end()
        elif tetro.angle % 360 == 90 and tetro.y >= height - 35:
            tetro.reached_end()
    
    if newshape == True:
        for i in shape_list:
            pushMatrix()
            translate(i.x + 35, i.y + 35)
            i.create_shape()
            popMatrix()
    tetro.stay()

def keyPressed():
    global angle
    if keyCode == LEFT:
        tetro.x -= 35
    elif keyCode == RIGHT:
        tetro.x += 35
    elif keyCode == UP:
        tetro.angle += 90
    elif keyCode == DOWN:
        tetro.angle -= 90
    elif key == ' ':
        tetro.y += 35 
