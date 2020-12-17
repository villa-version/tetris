class Object():

    step = 200

    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed

    def show(self):
        rectMode(CENTER)
        rect(self.x, self.y, self.w, self.h)

    def move(self):
        if millis() >= self.step:
            self.step = millis() + 200
            self.y = self.y + self.speed
