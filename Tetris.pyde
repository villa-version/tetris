from the_foundation_tetris import FoundTetris

tetris = None


def setup():
    size(1024,600)
    global tetris
    tetris = FoundTetris()

    tetris.load_all()


def draw():

    tetris.run()
    tetris.distance()


def keyPressed():
    tetris.pressed()
#    tetris.turn_tetris()
