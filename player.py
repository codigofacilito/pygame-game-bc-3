import pygame
import settings

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
       
        self.speed = settings.PLAYER_SPEED
        self.lifes = 3
        self.score = 0

        self.image = pygame.Surface( settings.PLAYER_SIZE )
        self.rect = self.image.get_rect()

        self.rect.x = pos_x
        self.rect.y = pos_y

        self.image.fill( settings.PLAYER_BACKGROUND )

    # El parámetro surface es donde se pinta
    def draw(self, surface):
        surface.blit(self.image, self.rect)


    def move_up(self):
        self.rect.y -= self.speed


    def move_down(self):
        self.rect.y += self.speed


    def move_left(self):
        self.rect.x -= self.speed

    
    def move_right(self):
        self.rect.x += self.speed

    
    def eat(self, apple):
        if pygame.sprite.collide_rect(self, apple):
            self.score += 1
            return True
        else:
            return False