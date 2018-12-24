import copy
def setup():
    global font, clickcount
    clickcount = 0
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

class piece:
    pass
    
def draw():
    global font
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
                '''try:
                    if grid[mouseY//87][(mouseX - 300) // 87] == grid[row][column]:
                        fill(50, 205, 50)
                except IndexError:
                    pass'''
                if mouseY//87 == row and (mouseX - 300)/87 == column:
                    fill(50, 205, 50)
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
    global clickcount
    if not clickcount:
        clickcount += 1
    elif clickcount:
        clickcount = 0
