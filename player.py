import pygame
from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, i):
        super().__init__(groups)
        self.image = pygame.image.load('./Asset/dungeon/heroes/knight/knight_idle_anim_f0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        # # replace i in parameter with obstacle_sprites
        # self.obstacle_sprites = obstacle_sprites

        # stats (UI)
        self.stats = {'health': 100, 'energy': 60, 'speed': 4}
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.exp = 123
        self.speed = self.stats['speed']

