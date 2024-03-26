import pygame
from pygame.locals import *
import time

pygame.init()

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 50))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.acc = 0.5

    def draw(self, window):
        window.blit(self.surf, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            self.rect.x -= self.acc
            print("Moving left")
        if keys[K_RIGHT]:
            self.rect.x += self.acc
            print("Moving right")
        if keys[K_UP]:
            self.rect.y -= self.acc
            print("Moving up")
        if keys[K_DOWN]:
            self.rect.y += self.acc
            print("Moving down")

        if keys[K_a]:
            self.rect.x -= self.acc
            print("Moving left")
        if keys[K_d]:
            self.rect.x += self.acc
            print("Moving right")
        if keys[K_w]:
            self.rect.y -= self.acc
            print("Moving up")
        if keys[K_s]:
            self.rect.y += self.acc
            print("Moving down")

width = 800
height = 600
win = pygame.display.set_mode((width, height), RESIZABLE)
pygame.display.set_caption("Heros Revalation")

clock = pygame.time.Clock()

FPS = 60

running = True

bg = (0, 0, 0)

bl = Block()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    win.fill(bg)
    bl.draw(win)
    bl.move()
    pygame.display.update()

    clock.tick(FPS)
    