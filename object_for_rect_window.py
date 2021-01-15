class ObjectForRectWindow():

    def __init__(self, x, y, w, h, bool, index_tetris_save):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.bool = bool
        self.index_tetris_save = index_tetris_save

    def show(self):
        fill(255,255,255)
        rect(self.x, self.y, self.w, self.h)
