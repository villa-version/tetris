from object_for_rect_window import ObjectForRectWindow

class RectForWindow(ObjectForRectWindow):

    def __init__(self, x, y, w, h, bool, index_tetris_save):
        ObjectForRectWindow.__init__(self, x, y, w, h, bool, index_tetris_save)

    def show(self):
        ObjectForRectWindow.show(self)
