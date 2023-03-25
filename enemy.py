import pygame
import settings
import random

class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface( settings.ENEMY_SIZE )
        self.rect = self.image.get_rect()

        self.rect.x = pos_x
        self.rect.y = pos_y

        self.speed = settings.ENEMY_SPEED

        self.image.fill( settings.ENEMY_BACKGROUND )
        self.direction = random.choice(
            ['left', 'right', 'up', 'down']
        )


    def draw(self, surface):
        surface.blit(self.image, self.rect)


    def move(self):

        if self.direction == 'left':
            self.rect.x -= self.speed
            
            if self.rect.x <= 0:
                self.direction = 'right'

        elif self.direction == 'right':
            self.rect.x += self.speed

            if self.rect.x >= settings.WIDTH - 20:
                self.direction = 'left'

        elif self.direction == 'up':
            self.rect.y -= self.speed

            if self.rect.y <= 0:
                self.direction = 'down'

        elif self.direction == 'down':
            self.rect.y += self.speed

            if self.rect.y >= settings.HEIGHT - 20:
                self.direction = 'up'

    
    def change_direction(self):
        if random.randint(0, 100) > 98:
            self.direction = random.choice(['left', 'right', 'up', 'down'] )

    
    def increment_speed(self):
        self.speed += 1


    def stop(self):
        self.speed = 0