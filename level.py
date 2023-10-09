import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        
        # get the surface
        self.dispay_surface = pygame.display.get_surface()

        # สร้างพื้น
        self.floor_surf = pygame.image.load('./Rougelite_Basic/Map/level_1.png')
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
        floor_offset_pos = self.floor_rect.topleft
        self.dispay_surface.blit(self.floor_surf, floor_offset_pos)
        
        # sprite group
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()
    
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites])
    
    def run(self):
        """Make game sprites run"""
        self.visible_sprites.draw(self.dispay_surface)