import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
active = True
x = 0
y_offest = 0
y = 250
x_rec = 600
x_rec_offset = -0.1
points = 0
pointrecived = 0
import random
y_rec = random.randint(-200,200)
while active:
    player = pygame.draw.circle(screen,(0,0,200), (250, y), 25, 1)
    object = pygame.draw.rect(screen, (200,0,0), pygame.Rect(x_rec, y_rec, 60, 300))
    if x > x_rec - 225 and pointrecived == 0:
        points += 1
        pointrecived = 1
    if player.colliderect(object): 
        points = 0
        x = 0
        y_offest = 0
        y = 250
        x_rec = 600
        y_rec = random.randint(-200,200)
        x_rec_offset = -0.1
    pygame.display.update()
    screen.fill((0,0,0))
    y += y_offest
    y_offest += 0.0001
    x_rec_offset -= 0.000001
    x_rec += x_rec_offset
    print(points)
    if x_rec < -80:
        pointrecived = 0
        y_rec = random.randint(-200,200)
        x_rec = 600
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                y -= 15
                y_offest = -0.1