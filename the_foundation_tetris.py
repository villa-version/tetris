from rect_tetris import RectTetris

class FoundTetris():

    tetris_1 = []
    tetris_save = []

    def load_all(self):

        for i in range(0,5):
            self.tetris_1.append(RectTetris(width/2, 0+i*25, 25, 25, 25))

    def run(self):
        background(255,255,255)

        for object_tetris in self.tetris_1:
            object_tetris.show(False)

        for object_tetris in self.tetris_save:
            object_tetris.show(True)
            print(str(self.tetris_save[0].y))
#            for i in range(0,len(self.tetris_1)):
#                self.tetris_1[i].y = height/2+i*25

    def distance(self):
        if height - self.tetris_1[len(self.tetris_1)-1].y <= self.tetris_1[len(self.tetris_1)-1].speed:
            for i in range(0, len(self.tetris_1)):
                self.tetris_1[i].y = height - i*self.tetris_1[i].h-self.tetris_1[i].h/2
                if len(self.tetris_save) != len(self.tetris_1):                    
                    self.tetris_save.append(self.tetris_1[i])
    
    def pressed(self):
        if key == 'a':
            for object_tetris in self.tetris_1:
                object_tetris.x = object_tetris.x - object_tetris.speed
        elif key == 'd':
            for object_tetris in self.tetris_1:
                object_tetris.x = object_tetris.x + object_tetris.speed
