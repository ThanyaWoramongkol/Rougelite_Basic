import pygame
from setting import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from ui import UI

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # floor setup || if created YSortCamera -> move this into section  and draw level
        self.floor_surf = pygame.image.load('./Map/level_1.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0, 0))
        floor_offset_pos = self.floor_rect.topleft
        # created map!? | self.display_surface.blit(mapping(picture), start_position)
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        # sprite group
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

        # user interface
        self.ui = UI()

    def create_map(self):
        layout = {
            'boundary': import_csv_layout('./Map/map_1_floorblock.csv')
        }

        # generate map
        for style, layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x, y), [self.visible_sprites, self.obstacles_sprites], 'invisible')
        # player position
        self.player = Player((631, 360), [self.visible_sprites], self.obstacles_sprites)

        # Debugging
        print("Map created successfully")
        print(f"Number of visible sprites: {len(self.visible_sprites)}")

    def run(self):
        self.display_surface.fill((255, 255, 255))  # Fill the screen with a white background

        # Draw the map
        self.display_surface.blit(self.floor_surf, self.floor_rect.topleft)

        # Draw other game objects on top of the map
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        self.ui.display(self.player)

        pygame.display.update()

