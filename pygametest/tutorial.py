from time import time

import pygame


pygame.init()
window = pygame.display.set_mode((800, 600))

run = True
last_time = time()
FPS_FONT = pygame.font.SysFont("arial", 24)
FPS = 48
CLOCK = pygame.time.Clock()
SPEED = 1
p1 = 10
left_pressed = False
right_pressed = False
while run:
    delay = time() - last_time
    last_time = time()

    if left_pressed:
        p1 -= SPEED
    if right_pressed:
        p1 += SPEED

    window.fill((0, 0, 0))

    fps_text = FPS_FONT.render("%.2f FPS" % (1 / delay), True, (0, 255, 0))
    window.blit(fps_text, (0, 0))

    pygame.draw.rect(window, (255, 0, 0), (p1, 50, 100, 100), 1)
    
    rect = pygame.Rect((10, 200, 50, 80))
    pygame.draw.rect(window, (0, 0, 255), rect)

    CLOCK.tick(FPS)
    pygame.display.update()

    keys = pygame.key.get_pressed()
    left_pressed = keys[pygame.K_LEFT]
    right_pressed = keys[pygame.K_RIGHT]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
