def setup():
  size(1366,700)
  background(255)

location = PVector(683, 355)
velocity = PVector(20, 30)

def  draw():
    global velocity
    global location
    noStroke()
    background(255)
    fill(0)
    ellipse(location.x,location.y,40,40)
    location.add(velocity)
    if ((location.x > width - 30) or (location.x < 20)):
        velocity.x *= -1
    if ((location.y > height - 30) or (location.y < 20)):
        velocity.y *=  -1
