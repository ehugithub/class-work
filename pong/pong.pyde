def setup():
  size(1366,700)
  background(255)

location = PVector(683, 355)
velocity = PVector(40, 40)

#class paddle:

left = 0
right = 0
def score_point():
    if location.x > width - 30:
        left += 1
    elif location.x < 20:
         right += 1

def  draw():
    global velocity
    global location
    global left
    global right
    background(255)
    textSize(150)
    fill(0)
    scorepoint()
    text('{}     {}'.format(left,right), 450, 200)
    
    noStroke()
    fill(0)
    ellipse(location.x,location.y,40,40)
    location.add(velocity)
    if location.x > width - 30 or location.x < 20:
        velocity.x *= -1
    if location.y > height - 30 or location.y < 20:
        velocity.y *= -1 '''
