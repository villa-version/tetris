from object import Object

class RectTetris(Object):

    def __init__(self, x, y, w, h, speed):
        Object.__init__(self, x, y, w, h, speed)

    def show(self):
        Object.show(self)
        Object.move(self)
