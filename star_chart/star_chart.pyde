import random
def setup():
    size(640, 480)
stars_x = []
stars_y = []

for x in range(100):
    stars_x.append(random.randint(0, 640))
    stars_y.append(random.randint(0, 480))


def draw():
    background(0)
    
    if frameCount % 60 == 0:
        stars_x.append(-1)
        stars_y.append(random.randint(0,480))
    
    
    # draw stars
    noStroke()
    fill(255)
    index = 0
    while index < len(stars_x):
        ellipse(stars_x[index], stars_y[index], 5, 5)
        index += 1
    
    for n, i in enumerate(stars_x):
        stars_x[n] += 0.1
        if stars_x[n] > 640:
            stars_x.pop(n)
            stars_y.pop(n)
