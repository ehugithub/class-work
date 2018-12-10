import random

def setup():
    size(666, 700)
    background(0)

grid = [False] * 200

def draw():
    global grid
    fill(0)
    stroke(128)
    row = 0
    column = 0
    for num in grid:
        rect(column * 35, row * 35, 35, 35)
        column += 1
        if column % 10 == 0:
            row += 1
            column = 0
    
