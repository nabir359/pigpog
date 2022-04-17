from pygame import *
from random import randint

window = display.set_mode((800, 600))
#создай окно игры
backround = transform.scale(image.load('IQTgpn.jpg'),(800, 600))


clock= time.Clock()


game = True

while game:
    window.blit(backround,(0,0))
    for e in event.get():
        if e.type  == QUIT:
            game = False

    display.update()
    clock.tick()