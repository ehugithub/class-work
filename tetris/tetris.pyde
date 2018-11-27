import random
def setup():
   size(1366,700)

position = PVector(1121, 35)
left = False
right = False
def create_shape():
   global shape
   global left
   global right
   num = random.randrange(1,4)
   
   return rect(position.x,position.y, 70, 70)
def draw():
   global position
   delay(800)
   background(0)
   line(1016, 0, 1016, height)
   stroke(128)
   for i in range(1016,  width, 35):
       line(i, 0 , i, height)
   for i in range(0, height, 35):
       line(1016, i, width, i)
   create_shape()
   position.y += 35
   # print(left, right)
def keyPressed():
   if keyCode == LEFT:
       position.x -= 35
   elif keyCode == RIGHT:
       position.x += 35
