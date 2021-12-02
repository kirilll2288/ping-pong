from pygame import *
 
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("ping_pong")

class GameSprite(sprite.Sprite):
    def __init__(self, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = width
        self.height = height

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Racket1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 445:
            self.rect.y += self.speed
class Racket2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 445:
            self.rect.y += self.speed


class Wall(sprite.Sprite):
    def  __init__(self, color_1, color_2, color_3, wall_width, wall_height, wall_x, wall_y):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


wall1 = Wall(166, 219, 8, 15, 220, 0, 150)
wall2 = Wall(255, 0, 1, 15, 220, 685, 150)
wall1.draw_wall()
wall2.draw_wall()


game = True
FPS = 60
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    wall1.draw_wall()
    wall2.draw_wall()


    display.update()
    clock.tick(60)