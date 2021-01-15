from rect_tetris import RectTetris
from rect_in_size import RectForWindow

class FoundTetris():

    tetris_1 = []
    tetris_2 = []
    tetris_save = []
    move_select = True
    back_tetris_save = []
    random_spawn_tetris = 0
    fps = 0
    fps_counter = 0 
    update_value = 0
    list_for_rects = []
    minim_music = None
    music_for_tetris = None
    quantity_tetris_save = 0

    for _ in range(0,25):
        list_for_rects.append([])

    def load_all(self, music_for_tetris):

        self.random_spawn_tetris = int(random(0,2))

        self.music_for_tetris = music_for_tetris
        #self.minim_music = Minim(this)
        #self.music_for_tetris = self.minim_music.loadFile('sound_for_tetris.wav')

        if self.random_spawn_tetris == 0:
            for i in range(0,5):
                self.tetris_1.insert(0,(RectTetris(width/2, (i*25)-25/2, 25, 25, 25)))
                self.tetris_save.insert(0,(RectTetris(0, 0, 0, 0, 0)))

            w = width/self.tetris_1[0].w + 1
            h = height/self.tetris_1[0].h
            for y in range(0,h):
                for x in range(0,w):
                    self.list_for_rects[y].append(RectForWindow(0+self.tetris_1[0].w/2+self.tetris_1[0].w*x, 1+self.tetris_1[0].h/2+self.tetris_1[0].h*y, self.tetris_1[0].w, self.tetris_1[0].h, False, 0))

        elif self.random_spawn_tetris == 1:
            self.tetris_2.insert(0,(RectTetris(width/2, 25/2+1, 25, 25, 25)))
            self.tetris_2.insert(0,(RectTetris(width/2+25, 25/2+1, 25, 25, 25)))
            self.tetris_2.insert(0,(RectTetris(width/2+25*2, 25*2-25/2, 25, 25, 25)))
            self.tetris_2.insert(0,(RectTetris(width/2+25*3, 25*2-25/2, 25, 25, 25)))
            for _ in range(0,len(self.tetris_2)):
                self.tetris_save.insert(0,(RectTetris(0, 0, 0, 0, 0)))

            w = width/self.tetris_2[0].w + 1
            h = height/self.tetris_2[0].h
            for y in range(0,h):
                for x in range(0,w):
                    self.list_for_rects[y].append(RectForWindow(0+self.tetris_2[0].w/2+self.tetris_2[0].w*x, 1+self.tetris_2[0].h/2+self.tetris_2[0].h*y, self.tetris_2[0].w, self.tetris_2[0].h, False, 0))

    def run(self):
        background(255,255,255)

        #func section
        self.draw_rect()
        self.distance_tetris_1()
        self.distance_tetris_2()
        self.distance_between_height_and_tetris_1()
        self.distance_between_height_and_tetris_2()
        self.walls_for_tetris()
        self.show_fps()
        self.get_true_on_rect()
        self.delete_piece_of_tetris_save()
        #func section

        for object_tetris in self.tetris_1:
            object_tetris.show()

        for object_tetris in self.tetris_2:
            object_tetris.show()

        for object_tetris in self.tetris_save:
            object_tetris.show()

###############################################################################################
###############################################################################################

    def show_fps(self):
        self.fps_counter = self.fps_counter + 1
        if millis() - self.update_value >= 1000:
            print(str(self.fps_counter))
            self.update_value = millis()
            self.fps = self.fps_counter
            self.fps_counter = 0
        fill(0,0,0)
        textSize(24)
        text(self.fps, width-50, height/5)    

    def distance_between_height_and_tetris_2(self):
        if len(self.tetris_2) != 0:
            if height - self.tetris_2[0].y <= self.tetris_2[0].speed:
                for i in range(0,len(self.tetris_2)):
                    self.tetris_save[i].y = self.tetris_2[i].y
                    self.tetris_save[i].x = self.tetris_2[i].x
                    self.tetris_save[i].w = self.tetris_2[i].w
                    self.tetris_save[i].h = self.tetris_2[i].h
                    self.move_select = False
                self.music_for_tetris.play()
                self.change_points_tetris_2()
                self.spawn_tetris_save()
            else:
                self.move_select = True


    def distance_between_height_and_tetris_1(self):
        if len(self.tetris_1) != 0:
            if height - self.tetris_1[0].y <= self.tetris_1[0].speed:
                for i in range(0, len(self.tetris_1)):
                    self.tetris_save[i].y = height - i*self.tetris_1[i].h-self.tetris_1[i].h/2
                    self.tetris_save[i].x = self.tetris_1[i].x
                    self.tetris_save[i].w = self.tetris_1[i].w
                    self.tetris_save[i].h = self.tetris_1[i].h
                    self.move_select = False
                self.music_for_tetris.play()
                self.spawn_tetris_save()
                self.change_points_tetris_1()
            else:
                self.move_select = True


    def spawn_tetris_save(self):
        if len(self.tetris_1) != 0:
            for _ in range(0,len(self.tetris_1)):
                self.tetris_save.insert(0,(RectTetris(0, 0, 0, 0, 0)))
        elif len(self.tetris_2) != 0:
            for _ in range(0,len(self.tetris_2)):
                self.tetris_save.insert(0,(RectTetris(0, 0, 0, 0, 0)))


    def change_points_tetris_1(self):
        for i in range(0,len(self.tetris_1)):
            self.tetris_1[i].y = (25*(len(self.tetris_1)-1-i))-25/2
            self.tetris_1[i].x = width/2

    def change_points_tetris_2(self):
        self.tetris_2[3].y = 25/2+1
        self.tetris_2[2].y = 25/2+1
        self.tetris_2[1].y = 25*2-25/2
        self.tetris_2[0].y = 25*2-25/2

        self.tetris_2[3].x = width/2
        self.tetris_2[2].x = width/2+25
        self.tetris_2[1].x = width/2+25*2
        self.tetris_2[0].x = width/2+25*3


    def draw_rect(self):
        if len(self.tetris_1) != 0:
            for i in range(0,len(self.list_for_rects)):
                for item in self.list_for_rects[i]:
                    item.show()

        elif len(self.tetris_2) != 0:
            for i in range(0,len(self.list_for_rects)):
                for item in self.list_for_rects[i]:
                    item.show()


    def pressed_to_move_tetris_1(self):
        if len(self.tetris_1) != 0:
            if self.move_select:
                if key == 'a':
                    for object_tetris in self.tetris_1:
                        object_tetris.x = object_tetris.x - object_tetris.speed
                elif key == 'd':
                    for object_tetris in self.tetris_1:
                        object_tetris.x = object_tetris.x + object_tetris.speed


    def pressed_to_move_tetris_2(self):
        if len(self.tetris_2) != 0:
            if self.move_select:
                if key == 'a':
                    for object_tetris in self.tetris_2:
                        object_tetris.x = object_tetris.x - object_tetris.speed
                elif key == 'd':
                    for object_tetris in self.tetris_2:
                        object_tetris.x = object_tetris.x + object_tetris.speed


    def distance_tetris_1(self):
        if len(self.tetris_1) != 0:
            for i in range(0,len(self.tetris_save)):
                for j in range(0,len(self.tetris_1)):
                    if (self.tetris_1[j].x == self.tetris_save[i].x and
                        self.tetris_save[i].y - self.tetris_1[j].y <= self.tetris_1[0].speed):
                        for i in range(0,len(self.tetris_1)):
                            self.tetris_save[i].y = self.tetris_1[i].y
                            self.tetris_save[i].x = self.tetris_1[i].x
                            self.tetris_save[i].w = self.tetris_1[i].w
                            self.tetris_save[i].h = self.tetris_1[i].h
                        self.move_select = False
                        self.spawn_tetris_save()
                        self.change_points_tetris_1()
                        break


    def distance_tetris_2(self):
        if len(self.tetris_2) != 0:
            for i in range(0,len(self.tetris_save)): 
                for j in range(0,len(self.tetris_2)):
                    if (self.tetris_2[j].x == self.tetris_save[i].x and
                        self.tetris_save[i].y - self.tetris_2[j].y <= self.tetris_2[0].speed):
                        for i in range(0,len(self.tetris_2)):
                            self.tetris_save[i].y = self.tetris_2[i].y
                            self.tetris_save[i].x = self.tetris_2[i].x
                            self.tetris_save[i].w = self.tetris_2[i].w
                            self.tetris_save[i].h = self.tetris_2[i].h
                        self.move_select = False
                        self.spawn_tetris_save()
                        self.change_points_tetris_2()
                        break


    def walls_for_tetris(self):
        if len(self.tetris_1) != 0:
            if self.tetris_1[0].x > width:
                for i in range(0,len(self.tetris_1)):
                    self.tetris_1[i].x = 0+25/2
            elif self.tetris_1[0].x < 0:
                for i in range(0,len(self.tetris_1)):
                    self.tetris_1[i].x = width-25/2


    def get_true_on_rect(self):
        for obj in self.list_for_rects:
            for item in obj:
                for j in range(0,len(self.tetris_save)):
                    if self.tetris_save[j].x == item.x and self.tetris_save[j].y == item.y:
                        item.bool = self.get_true()
                        item.index_tetris_save = j
                        self.quantity_tetris_save += 1


    def delete_piece_of_tetris_save(self):
        for obj in self.list_for_rects:
            for item in obj:
                if self.quantity_tetris_save == len(obj):
                    if item.bool == self.get_true() and item.index_tetris_save <= 0:
                        while i < len(self.tetris_save):
                            if i == item.index_tetris_save:
                                del[i]
                            else:
                                i = i+1


    def get_true(self):
        return True
