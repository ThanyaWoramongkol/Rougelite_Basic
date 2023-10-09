import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("./Rougelite_Basic/game_sprites/tiles/wall/wall_1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        