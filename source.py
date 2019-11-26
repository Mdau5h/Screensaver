import pygame
from random import choice, randint, uniform
from math import cos, sin, pi

BACKGROUND = (0, 0, 0)
GRAY = (125, 125, 125)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 255, 255)
PINK = (255, 0, 255)
YELLOW = (225, 225, 0)

colors = [GRAY, RED, GREEN, BLUE, LIGHT_BLUE, PINK, YELLOW]
poly_color = choice(colors)

dot_number = 10

FPS = 120
width = 800
height = 600

points = [[randint(0, width), randint(0, height)] for _ in range(dot_number)]
angles = [uniform(0, 2*pi) for _ in range(dot_number)]
speed = 10

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((width, height))
screen = pygame.Surface((width, height))

run = True
while run:
    window.blit(screen, (0, 0))
    screen.fill(BACKGROUND)
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.aalines(screen, poly_color, True, points)
    for i in range(dot_number):
        points[i][0] += speed * cos(angles[i])
        points[i][1] += speed * sin(angles[i])

        if points[i][0] < 1 or points[i][0] > width:
            angles[i] = pi - angles[i]
            poly_color = choice(colors)
        if points[i][1] < 1 or points[i][1] > height:
            angles[i] = 2*pi - angles[i]
            poly_color = choice(colors)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
