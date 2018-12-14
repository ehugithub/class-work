def setup():
    background(0)
    size(666,700)


grid = [([0] * 10) for x in range(20)]
def draw():
    row = 0
    column = 0
    stroke(255,255,255, 128)
    fill(0)
    for i in grid:
        for x in i:
            if x == 1:
                fill(255, 0, 0)
            rect(column * 35, row * 35, 35, 35)
            column += 1
            if column >= 10:
                row += 1
                column = 0
    if frameCount % 60 == 0:
        pass
