import pygame
import random
import src.constants as constants

class Paddle:
    def __init__(self, x, y, speed):
        self.rect = pygame.Rect(x, y, constants.LARGURA_RAQUETE, constants.ALTURA_RAQUETE)
        self.speed = speed

    def move(self, up: bool, down: bool):
        if up and self.rect.top > 0:
            self.rect.y -= self.speed
        if down and self.rect.bottom < constants.ALTURA_TELA:
            self.rect.y += self.speed

    def auto_move(self, target_y):
        if self.rect.centery < target_y:
            self.rect.y += self.speed
        elif self.rect.centery > target_y:
            self.rect.y -= self.speed
        
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > constants.ALTURA_TELA:
            self.rect.bottom = constants.ALTURA_TELA

class Ball:
    def __init__(self, color=constants.COR_ELEMENTOS, is_real=True):
        self.rect = pygame.Rect(0, 0, constants.TAMANHO_BOLA, constants.TAMANHO_BOLA)
        self.color = color  
        self.is_real = is_real
        self.vel_x = 0
        self.vel_y = 0
        self.reset(1)

    def reset(self, direction_x):
        self.rect.center = (constants.LARGURA_TELA // 2, constants.ALTURA_TELA // 2)
        self.vel_x = constants.VELOCIDADE_INICIAL_BOLA * direction_x
        self.vel_y = constants.VELOCIDADE_INICIAL_BOLA * random.choice([-1, 1])

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.top <= 0 or self.rect.bottom >= constants.ALTURA_TELA:
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
        
        limit = constants.VELOCIDADE_INICIAL_BOLA * 2
        if abs(self.vel_y) > limit:
            self.vel_y = limit if self.vel_y > 0 else -limit
        if abs(self.vel_y) < 2:
            self.vel_y = 2 if self.vel_y > 0 else -2
