import pygame
import settings
import random

from player import Player
from apple import Apple
from enemy import Enemy

pygame.init()

surface = pygame.display.set_mode( settings.SIZE ) # Return a Surface
pygame.display.set_caption("Juego del bootcamp.")

# Player es un objeto de la clase Player
player = Player(200, 300)
enemy = Enemy(400, 400)
apples = []

for _ in range(0, settings.ENEMIES):

    pos_x = random.randint(0, settings.WIDTH - 20)
    pos_y = random.randint(0, settings.HEIGHT - 20)
    apple = Apple(pos_x, pos_y)
    
    apples.append(apple)

game = True
clock = pygame.time.Clock()

min_apples = 5

while game:
    clock.tick(settings.FPS)

    # Iteramos sobre todos los eventos que puedan ocurrir en la venta.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_UP]:
        player.move_up()
    
    if key_pressed[pygame.K_DOWN]:
        player.move_down()

    if key_pressed[pygame.K_LEFT]:
        player.move_left()

    if key_pressed[pygame.K_RIGHT]:
        player.move_right()


    surface.fill(settings.BACKGROUND)
    
    enemy.draw(surface)
    player.draw(surface)

    for apple in apples:
        apple.draw(surface)

    for apple in apples:
        if player.eat(apple):
            apples.remove(apple)

    enemy.move()
    enemy.change_direction()

    if len(apples) < min_apples:
        enemy.increment_speed()
        min_apples -= 1

    if len(apples) == 0:
        enemy.stop()

    if pygame.sprite.collide_rect(player, enemy):
        game = False

    pygame.display.update()
