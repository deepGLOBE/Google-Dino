import random

import pygame
import os
import sys

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60

font = pygame.font.SysFont('aria',40)

sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()




from Kartinki import *

def restart():
    global dinoplayer_group, cactus_group, earth_group, dino
    dinoplayer_group = pygame.sprite.Group()
    cactus_group = pygame.sprite.Group()
    dino = Dino()
    dinoplayer_group.add(dino)








def gamelvl():
    sc.fill('dimgray')
    sc.blit(earth_image,(0, HEIGHT - 60))
    dinoplayer_group.draw(sc)
    dinoplayer_group.update()
    cactus_group.draw(sc)
    cactus_group.update()
    text_font = font.render(f'score {dino.score}', True, 'white')
    sc.blit(text_font,(900,0))

    pygame.display.update()


class Kaktus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = kaktus_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH,WIDTH + 500)
        self.rect.bottom = HEIGHT - 60
        self.speed = 10


    def update(self, *args, **kwargs):
        self.rect.x -= self.speed


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = dino_image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.bottom = HEIGHT - 60
        self.jump = False
        self.jump_step = -22
        self.timer_spawn = 0
        self.score = 0

    def update(self, *args, **kwargs):
        global  FPS
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.jump = True
        if self.jump:
            if self.jump_step <= 22:
                self.rect.y -= self.jump_step
                self.jump_step += 1
                self.score += 1
            else:
                self.jump = False
                self.jump_step = -22
        self.timer_spawn += 1
        if key[pygame.K_q]:
            self.timer_spawn += 10
        if key[pygame.K_r]:
            restart()

        if self.timer_spawn / FPS > 2:
            kaktus = Kaktus()
            cactus_group.add(kaktus)
            self.timer_spawn = 0
            if pygame.sprite.spritecollide(self, cactus_group, True):
                self.kill()
                FPS = 3


















































restart()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    gamelvl()
    clock.tick(FPS)































