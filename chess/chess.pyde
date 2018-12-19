def setup():
    global pawn
    pawn = loadImage("pawn.png")
    size(1366, 700)
grid = ([[0] * 8] for x in range(8))
class piece:
    pass
    
def draw():
    global pawn
    image(pawn, 200, 200)
