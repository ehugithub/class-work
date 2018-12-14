add_library('sound')
def setup():
    size(666,700)
    sf = SoundFile(this, "theme.mp3")
    sf.loop()

class block:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y

grid = [([0] * 10) for x in range(20)]
x = 0
def draw():
    background(0)
    global x
    row = 0
    column = 0
    stroke(255, 255, 255, 128)
    fill(0)
    for i in grid:
        for x in i:
            if x == 1:
                fill(255, 0, 0)
            else:
                fill(0)
            rect(column * 35, row * 35, 35, 35)
            column += 1
            if column >= 10:
                row += 1
                column = 0
    if frameCount % 60 == 0:
        pass
