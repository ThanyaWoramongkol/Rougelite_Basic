import pygame
from setting import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from ui import UI
from enemie import Enemy
from weapon import Weapon

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
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        # attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

        # user interface
        self.ui = UI()

    def create_map(self):
        layout = {
            'boundary': import_csv_layout('./Map/map_1_floorblock.csv'),
            'entities' : import_csv_layout('./Map/map_Entities.csv') #add by TaiKie
        }

        # generate map
        for style, layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            # อันบนเห็นขอบแมพเป็นสีดำ อันล่างไม่เห็น
                            # Tile((x, y), [self.visible_sprites, self.obstacles_sprites], 'invisible')
                            Tile((x, y), [self.obstacles_sprites], 'invisible')

                        #enemies parts
                        if style == 'entities':
                            if col == '394':
                                #add by TaiKie
                                self.player = Player(
                                    (x, y),
                                    [self.visible_sprites],
                                    self.obstacles_sprites,
                                    self.create_attack,
                                    self.destroy_attack)
                            else:
                                if col == '390' : monster_name = 'slime'
                                elif col == '391' : monster_name = 'flying creature'
                                elif col == '392' : monster_name = 'goblin'
                                Enemy(monster_name,
                                      (x, y),
                                      [self.visible_sprites,self.attackable_sprites],
                                      self.obstacles_sprites,
                                      self.damage_player,
                                      self.add_exp)



        # Debugging
        print("Map created successfully")
        print(f"Number of visible sprites: {len(self.visible_sprites)}")

    def get_enemy_count(self):
        # Count the number of instances of the Enemy class in visible_sprites
        enemy_count = sum(1 for sprite in self.visible_sprites.sprites() if isinstance(sprite, Enemy))
        return enemy_count

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites, self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        target_sprite.get_damage(self.player,attack_sprite.sprite_type)

    def damage_player(self,amount,attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()


        # if self.player.health <= 0:
        #     self.display_surface.fill((255, 0, 0))  # Red background for the game-over screen
        #     # Render a message or other elements for the game-over screen
        #     game_over_text = UI_FONT.render("Game Over", True, (255, 255, 255))
        #     screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGTH // 2))
        #     pygame.display.update()

    def add_exp(self, amount):
        self.player.exp += amount

    def run(self):
        self.display_surface.fill((255, 255, 255))  # Fill the screen with a white background

        # Draw the map
        self.display_surface.blit(self.floor_surf, self.floor_rect.topleft)

        # Draw other game objects on top of the map
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()
        self.ui.display(self.player)
        # debug(self.player.status)

        pygame.display.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # gennaral setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self,player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centerx - self.half_height

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

    def enemy_update(self, player): #add by TaiKie
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
