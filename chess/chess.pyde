import copy
def setup():
    global font, select_piece, move_piece
    select_piece = move_piece = False
    background(255)
    size(1366, 700)
    font = createFont("https://drive.google.com/uc?export=download&id=0BwTQLXGKzDbZUmFkdEl0RW9IX2c", 48)
grid = [[4, 2, 3, 5, 6, 3, 2, 4],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [7, 7, 7, 7, 7, 7, 7, 7],
        [10, 8, 9, 11, 12, 9, 8, 10]]
tempX = tempY = tempPiece = None
    
def draw():
    global font, tempX, tempY, tempPiece, move_piece
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
            if select_piece:
                try:
                    if grid[tempY//87][(tempX - 300)//87] == 10:
                        if tempY//87 == row and (tempX - 300)/87 == column:
                            fill(164, 148, 128)
                        elif (tempY//87 == row or (tempX - 300)/87 == column):
                            # why i didn't loop through specific column/row, then if any is a piece, break the loop, no idea
                            if grid[tempY//87 - 1][(tempX - 300)//87] and (tempX - 300)//87 == column and tempY//87 > row:
                                    pass
                            elif not grid[row][column]:
                                    fill(50, 205, 50)
                            elif 0 < grid[row][column] < 7:
                                fill(179, 25, 0)
                    elif grid[tempY//87][(tempX - 300)/87] == 8:
                        if tempY//87 == row and (tempX - 300)/87 == column:
                            fill(164, 148, 128)
                        elif ((abs(tempY//87 - row) == 2 and abs((tempX - 300)//87 - column) == 1) or (abs(tempY//87 - row) == 1 and abs((tempX - 300)//87 - column) == 2)):
                            if not grid[row][column]:
                                fill(50, 205, 50)
                            elif 0 < grid[row][column] < 7:
                                fill(179, 25, 0)
                    elif grid[tempY//87][(tempX - 300)/87] == 7:
                        if tempY//87 == row and (tempX - 300)/87 == column:
                            fill(164, 148, 128)
                            # fill(250, 218, 94)
                        if tempY//87 == 6:
                            if grid[tempY//87 - 1][(tempX - 300)//87] and (tempX - 300)//87 == column and tempY//87 > row:
                                    pass
                            elif (tempY//87 - 2 == row and (tempX - 300)//87 == column or tempY//87 - 1 == row and (tempX - 300)/87 == column) and not grid[row][column]:
                                fill(50, 205, 50)
                        else:
                            if (tempY//87 - 1 == row and (tempX - 300)/87 == column) and not grid[row][column]:
                                fill(50, 205, 50)
                    elif grid[tempY//87][(tempX - 300)/87] == 9:
                        if tempY//87 == row and (tempX - 300)/87 == column:
                            fill(164, 148, 128)
                        elif (abs(tempY//87 - row) == abs((tempX - 300)/87 - column)):
                            if not grid[row][column]:
                                fill(50, 205, 50)
                            elif 0 < grid[row][column] < 7:
                                fill(179, 25, 0)
                    elif grid[tempY//87][(tempX - 300)/87] == 11:
                        if tempY//87 == row and (tempX - 300)/87 == column:
                            fill(164, 148, 128)
                        elif ((abs(tempY//87 - row) == abs((tempX - 300)/87 - column)) or (tempY//87 == row or (tempX - 300)/87 == column)):
                            if not grid[row][column]:
                                fill(50, 205, 50)
                            elif 0 < grid[row][column] < 7:
                                fill(179, 25, 0)
                    elif grid[tempY//87][(tempX - 300)/87] == 12:
                        if tempY//87 == row and (tempX - 300)/87 == column:
                            fill(164, 148, 128)
                        elif (tempY//87 - 1 == row - 1 or tempY//87 - 1 == row or tempY//87 - 1 == row - 2) and ((tempX - 300)//87 == column + 1 or (tempX - 300)//87 == column or (tempX - 300)//87 == column - 1):
                            if not grid[row][column]:
                                fill(50, 205, 50)
                            elif 0 < grid[row][column] < 7:
                                fill(179, 25, 0)
                except:
                    pass
            rect(column * 87 + 300, row * 87, 87, 87)
            column += 1
            if column == 8:
                column = 0
                row += 1
            count += 1
    if move_piece:
        try:
            grid[mouseY//87][(mouseX - 300)//87] = tempPiece
            grid[tempY//87][(tempX - 300)/87] = 0
        except:
            pass
        move_piece = False
    
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
    global select_piece, move_piece, tempX, tempY, tempPiece
    loadPixels()
    location = get(mouseX, mouseY)
    if red(pixels[mouseX + mouseY * width]) == 179 and green(pixels[mouseX + mouseY * width]) == 25 and blue(pixels[mouseX + mouseY * width]) == 0:
        move_piece = True
    if (red(location) == 50 and green(location) == 205 and blue(location) == 50) or (red(location) == 179 and green(location) == 25 and blue(location) == 0):
        move_piece = True
    try:
        if not select_piece and grid[mouseY//87][(mouseX - 300)//87]:
            select_piece = True
            tempPiece = copy.copy(grid[mouseY//87][(mouseX - 300)//87])
            tempX = copy.copy(mouseX)
            tempY = copy.copy(mouseY)
        elif select_piece:
            select_piece = False
    except:
        pass
