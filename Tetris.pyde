from the_foundation_tetris import FoundTetris

tetris = None


def setup():
    size(1024,600)
    rectMode(CENTER)
    global tetris
    tetris = FoundTetris()

    tetris.load_all()


def draw():

    tetris.run()

def keyPressed():
    tetris.pressed_to_move_tetris_1()
    tetris.pressed_to_move_tetris_2()
#    tetris.turn_tetris()
