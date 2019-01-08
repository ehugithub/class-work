import copy
def setup():
    global font, clickcount
    clickcount = False
    background(255)
    size(1366, 700)
    font = createFont("https://drive.google.com/uc?export=download&id=0BwTQLXGKzDbZUmFkdEl0RW9IX2c",48)
grid = [[4, 2, 3, 5, 6, 3, 2, 4],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [7, 7, 7, 7, 7, 7, 7, 7],
        [10, 8, 9, 11, 12, 9, 8, 10]]
tempX = tempY = None
def select_piece():
    pass
    
def draw():
    global font, tempX, tempY
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
            if clickcount:
                try:
                    if grid[tempY//87][(tempX - 300)/87] == 10:
                        if tempY//87 == row and (tempX - 300)/87 == column:
                            fill(164, 148, 128)
                        elif (tempY//87 == row or (tempX - 300)/87 == column) and not grid[row][column]:
                            fill(50, 205, 50)
                    elif grid[tempY//87][(tempX - 300)/87] == 8:
                        if tempY//87 == row and (tempX - 300)/87 == column:
                            fill(164, 148, 128)
                        elif (abs(tempY//87 - row) == 2 and abs((tempX - 300)/87 - column) == 1) and not grid[row][column]:
                            fill(50, 205, 50)
                    elif grid[tempY//87][(tempX - 300)/87] == 7:
                        if tempY//87 == row and (tempX - 300)/87 == column:
                            fill(164, 148, 128)
                            # fill(250, 218, 94)
                        elif tempY//87 - 2 == row and (tempX - 300)/87 == column or tempY//87 - 1 == row and (tempX - 300)/87 == column:
                            fill(50, 205, 50)
                except:
                    pass
            rect(column * 87 + 300, row * 87, 87, 87)
            column += 1
            if column == 8:
                column = 0
                row += 1
            count += 1
    
    
    
    textFont(font, 87)
    fill(0)
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                text(u'\u265F', column * 87 + 300, (row + 1) * 87) # black Pawn
            elif grid[row][column] == 2:
                text(u'\u265E', column * 87 + 300, (row + 1) * 87) # black Knight
            elif grid[row][column] == 3:
                text(u'\u265D', column * 87 + 300, (row + 1) * 87) # black Bishop
            elif grid[row][column] == 4:
                text(u'\u265C', column * 87 + 300, (row + 1) * 87) # black Rook
            elif grid[row][column] == 5:
                text(u'\u265B', column * 87 + 300, (row + 1) * 87) # black Queen
            elif grid[row][column] == 6:
                text(u'\u265A', column * 87 + 300, (row + 1) * 87) # black King
            elif grid[row][column] == 7:
                text(u'\u2659', column * 87 + 300, (row + 1) * 87) # white Pawn
            elif grid[row][column] == 8:
                text(u'\u2658', column * 87 + 300, (row + 1) * 87) # white Knight
            elif grid[row][column] == 9:
                text(u'\u2657', column * 87 + 300, (row + 1) * 87) # white Bishop
            elif grid[row][column] == 10:
                text(u'\u2656', column * 87 + 300, (row + 1)* 87) # white Rook
            elif grid[row][column] == 11:
                text(u'\u2655', column * 87 + 300, (row + 1) * 87) # white Queen
            elif grid[row][column] == 12:
                text(u'\u2654', column * 87 + 300, (row + 1) * 87) # white King
def mouseClicked():
    global clickcount, tempX, tempY
    if not clickcount:
        clickcount = True
        tempX = copy.copy(mouseX)
        tempY = copy.copy(mouseY)
    elif clickcount:
        clickcount = False
