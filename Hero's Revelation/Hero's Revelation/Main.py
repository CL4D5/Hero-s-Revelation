import pygame
from pygame.locals import *
import time

pygame.init()

clock = pygame.time.Clock()

FPS = 60

dt = clock.tick(FPS)

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
            self.rect.x -= self.acc * dt
            print("Moving left")
        if keys[K_RIGHT]:
            self.rect.x += self.acc * dt
            print("Moving right")
        if keys[K_UP]:
            self.rect.y -= self.acc * dt
            print("Moving up")
        if keys[K_DOWN]:
            self.rect.y += self.acc * dt
            print("Moving down")

        if keys[K_a]:
            self.rect.x -= self.acc * dt
            print("Moving left")
        if keys[K_d]:
            self.rect.x += self.acc * dt
            print("Moving right")
        if keys[K_w]:
            self.rect.y -= self.acc * dt
            print("Moving up")
        if keys[K_s]:
            self.rect.y += self.acc * dt
            print("Moving down")

        if self.rect.x < 0:
            self.rect.x = 0
            print("Hit the left wall")
        if self.rect.x > width - 30:
            self.rect.x = width - 30
            print("Hit the right wall")
        if self.rect.y < 0:
            self.rect.y = 0
            print("Hit the top wall")
        if self.rect.y > height - 50:
            self.rect.y = height - 50
            print("Hit the bottom wall")

width = 800
height = 600
win = pygame.display.set_mode((width, height), RESIZABLE)
pygame.display.set_caption("Heros Revalation")

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
    