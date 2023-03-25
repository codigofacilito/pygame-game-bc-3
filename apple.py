import pygame
import settings

class Apple(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface( settings.APPLE_SIZE )
        self.rect = self.image.get_rect()
        
        self.rect.x = pos_x
        self.rect.y = pos_y

        self.image.fill(settings.APPLE_BACKGROUND)


    def draw(self, surface):
        surface.blit(self.image, self.rect)