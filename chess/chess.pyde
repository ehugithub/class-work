def setup():
    background(255)
    noStroke()
    size(1366, 700)
grid = [[0] * 8 for x in range(8)]

class piece:
    pass
    
def draw():
    count = 0
    column = 0
    row = 0
    for i in grid:
        for j in i:
            if row % 2:
                if count % 2:
                    fill(232, 235, 239)
                else:
                    fill(125, 135, 150)
            elif not row % 2:
                if count % 2:
                    fill(125, 135, 150)
                else:
                    fill(232, 235, 239)
            rect(column * 100 + 250, row * 100, 100, 100)
            column += 1
            if column == 8:
                column = 0
                row += 1
            count += 1
    
    
    
    num = unichr(2654).encode('utf-8')
    # num = ord("\u2654")

    
    text(num, 100, 100)
