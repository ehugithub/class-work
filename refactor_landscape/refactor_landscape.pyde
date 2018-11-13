"""
1. Take your landscapes and refactor it by grouping related lines of code into functions.
   Your draw loop should look something like the code below, but, with functions relevant
   to YOUR landscape.
2. Turn the functions into functions that take arguments for x and y co-ordinates so they can
   be reused to draw multiple items in different locations. For example:
   
   def draw_sun(x, y):
      noStroke()
      fill(255,255,0)
      ellipse(x, y,200,200)
   
   # called by:
   draw_sun(620, height/12)  # or wherever you want to draw the sun
"""
def setup():
    size(1366, 700)
sun_pos = 100
def draw():
    background(0,191,255)
    draw_sun()
    
    draw_mountains()

def draw_sun():
    global sun_pos
    noStroke()
    fill(255,255,0)
    ellipse(sun_pos, height/12, 200,200)
    sun_pos += 5
def draw_mountains():
    fill(196,188,188)
    stroke(1)
    triangle(0, 768, 1366, 768, width/2, 100)
    triangle(600, 768, 1366, 768, 4*width/5, 50)
    triangle(-500, 768, 866, 768, width/5, 200)
    fill(240,248,245)
    triangle(580, 200, 784, 200, width/2, 100)
    triangle(204, 250, 325, 250, width/5, 200)
    triangle(1023, 150, 1130, 150, 4*width/5, 50)
