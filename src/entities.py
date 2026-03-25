import pygame
import random
from .constants import *

class Paddle:
    def __init__(self, x, y, speed):
        self.rect = pygame.Rect(x, y, LARGURA_RAQUETE, ALTURA_RAQUETE)
        self.speed = speed

    def move(self, up: bool, down: bool):
        if up and self.rect.top > 0:
            self.rect.y -= self.speed
        if down and self.rect.bottom < ALTURA_TELA:
            self.rect.y += self.speed

    def auto_move(self, target_y):
        if self.rect.centery < target_y:
            self.rect.y += self.speed
        elif self.rect.centery > target_y:
            self.rect.y -= self.speed
        
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTURA_TELA:
            self.rect.bottom = ALTURA_TELA

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, TAMANHO_BOLA, TAMANHO_BOLA)
        self.vel_x = 0
        self.vel_y = 0
        self.reset(1)

    def reset(self, direction_x):
        self.rect.center = (LARGURA_TELA // 2, ALTURA_TELA // 2)
        self.vel_x = VELOCIDADE_INICIAL_BOLA * direction_x
        self.vel_y = VELOCIDADE_INICIAL_BOLA * random.choice([-1, 1])

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.top <= 0 or self.rect.bottom >= ALTURA_TELA:
            self.vel_y *= -1
            self.apply_random_bounce()
            return True
        return False

    def bounce(self):
        self.vel_x *= -1.1
        self.apply_random_bounce()

    def apply_random_bounce(self):
        variation = random.uniform(0.8, 1.2)
        self.vel_y *= variation
        
        limit = VELOCIDADE_INICIAL_BOLA * 2
        if abs(self.vel_y) > limit:
            self.vel_y = limit if self.vel_y > 0 else -limit
        if abs(self.vel_y) < 2:
            self.vel_y = 2 if self.vel_y > 0 else -2
