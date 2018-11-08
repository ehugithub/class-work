import random
def setup():
    global stars
    size(640, 480)
    stars = []
    for x in range(100):
        stars.append([random.randint(0, width), random.randint(0, height)])

def draw():
    background(0)
    
    if frameCount % 60 == 0:
        stars.append([-1, random.randint(0, height)])

    # draw stars
    noStroke()
    fill(255)
    index = 0

    while index < len(stars):
        ellipse(stars[index][0], stars[index][1], 5, 5)
        index += 1

    for n, i in enumerate(stars):
        stars[n][0] += 0.1
        if stars[n][0] > width:
            stars.pop(n)
