import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    #เวลาสร้างplayer มันจะให้input มา 4 ตัวเลยใส่ i มารับinputกันerror
    def __init__(self, pos, groups, i):
        super().__init__(groups)
        self.image = pygame.image.load('./Rougelite_Basic/game_sprites/heroes/knight/knight_idle_anim_f0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)