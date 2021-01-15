from the_foundation_tetris import FoundTetris

tetris = None

add_library("minim")

def setup():
    size(1024,600)
    rectMode(CENTER)
    global tetris
    tetris = FoundTetris()

    minim_music = Minim(this)
    music_for_tetris = minim_music.loadFile('sound_for_tetris.wav')

    tetris.load_all(music_for_tetris)


def draw():

    tetris.run()

def keyPressed():
    tetris.pressed_to_move_tetris_1()
    tetris.pressed_to_move_tetris_2()
#    tetris.turn_tetris()
