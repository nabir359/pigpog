from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x,size_y, player_speed):
         super().__init__()
         self.image = transform.scale(image.load(player_image), (size_x, size_y))  
         self.speed = player_speed
         self.rect = self.image.get_rect()
         self.rect.x = player_x
         self.rect.y = player_y 
         self.direction ='right'

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 635:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.x > 10:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < 635:
            self.rect.y += self.speed

rakatka1 = Player('png hhug.jpg', 10, 400, 4,90,90)
rakatka2= Player('png hhug.jpg', 390, 400,4, 90, 90)
ball = GameSprite('ball.jpg',220,250,2,30,30)
#создай окно игры
backround = transform.scale(image.load('fon.jpg'),(800, 600))
window = display.set_mode((800, 600))

FPS=60
clock= time.Clock()
game = True

while game:
    window.blit(backround,(0,0))
    for e in event.get():
        if e.type  == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
