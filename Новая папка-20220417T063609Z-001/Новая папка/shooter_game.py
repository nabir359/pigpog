#Создай собственный Шутер!




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

window = display.set_mode((800, 600))
#создай окно игры
backround = transform.scale(image.load('galaxy.jpg'),(800, 600))



clock= time.Clock()
FPS = 60
font.init()
font2 = font.SysFont('impact',35)
score = 0



class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed
        
    def fire(self):
        pass    




lost = 0    
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >500:
            self.rect.x =randint(80, 620)
            self.rect.y = 0
            lost=lost + 1

class bullet(GameSprite):
    def apdate(self):
        pass






monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('ufo.png' , randint(80,620),-40,50,50,randint(1, 2))
    monsters.add(monster)

player = Player('rocket.png', 20,450,50,100, 10)
Enemy = Enemy('ufo.png', 20,200,2,100,50)

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()


finish = False


game = True

while game:
    for e in event.get():
        if e.type  == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                Player.fire()


    if finish != True:
        
        window.blit(backround,(0,0))
        text_lose= font2.render('Счет:'+str(score), 1 ,(255,255,255))
        window.blit(text_lose, (10,20))
        text_lose= font2.render('Пропущено:'+str(lost), 1 ,(255,255,255))
        window.blit(text_lose, (10,50))
        player.reset()
        player.update()
        monsters.update()
        monsters.draw(window)
        Enemy.reset()
        display.update()
    clock.tick(FPS)





