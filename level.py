import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *

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
        layouts = {
            'boundary': import_csv_layout('./Rougelite_Basic/Map/map_1_floorblock.csv')
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                    if style == 'boundary':
        # ลบ self.visible_sprites ถ้าไม่อยากเห็นส่วนขอบแมพที่กันเป็นดำ
                        Tile((x,y), [self.visible_sprites,self.obstacles_sprites], 'invisible')
        # วางตำแหน่งของ player
        self.player = Player((631,360), [self.visible_sprites], self.obstacles_sprites)
    
    def run(self):
        """Make game sprites run"""
        self.visible_sprites.draw(self.dispay_surface)