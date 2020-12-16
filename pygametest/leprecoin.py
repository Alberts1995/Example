from random import randint

import pygame


class Pepe:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y

        self.image = pygame.transform.scale(pygame.image.load("images/pepe.png"), (64, 64))


class Coin:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y

        self.image = pygame.transform.scale(pygame.image.load("images/coin.png"), (32, 32))


if __name__ == "__main__":
    FPS = 48
    CLOCK = pygame.time.Clock()

    pygame.init()
    
    window = pygame.display.set_mode((800, 600))

    running = True
    pepe = Pepe(368, 268)
    coin = Coin(randint(0, 768), randint(0, 568))
    while running:
        # Logic
        pepe_rect = pygame.Rect(pepe.x, pepe.y, 64, 64)
        coin_rect = pygame.Rect(coin.x, coin.y, 32, 32)

        if pepe_rect.colliderect(coin_rect):
            coin = Coin(randint(0, 768), randint(0, 568))

        # Render
        window.fill((0, 0, 0))

        window.blit(pepe.image, (pepe.x, pepe.y, 64, 64))
        window.blit(coin.image, (coin.x, coin.y, 32, 32))

        CLOCK.tick(FPS)
        pygame.display.update()

        # Key handle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            pepe.y -= 10
        if keys[pygame.K_DOWN]:
            pepe.y += 10
        if keys[pygame.K_LEFT]:
            pepe.x -= 10
        if keys[pygame.K_RIGHT]:
            pepe.x += 10
