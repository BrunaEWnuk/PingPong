import pygame
import sys
import random
import src.constants as constants
from src.entities import Paddle, Ball
from src.renderer import Renderer

class PongGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.LARGURA_TELA, constants.ALTURA_TELA))
        pygame.display.set_caption("Ping Pong")
        self.clock = pygame.time.Clock()
        self.renderer = Renderer(self.screen)
        self.reset_game()

    def reset_game(self):
        self.state = constants.GameState.MENU
        self.p1 = Paddle(15, constants.ALTURA_TELA // 2 - constants.ALTURA_RAQUETE // 2, constants.VELOCIDADE_JOGADOR)
        self.p2 = Paddle(constants.LARGURA_TELA - 15 - constants.LARGURA_RAQUETE, constants.ALTURA_TELA // 2 - constants.ALTURA_RAQUETE // 2, constants.VELOCIDADE_IA)
        self.ball = Ball()
        self.score1 = 0
        self.score2 = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if self.state == constants.GameState.MENU:
                    self.state = constants.GameState.JOGANDO
                    self.score1, self.score2 = 0, 0
                    self.ball.reset(random.choice([-1, 1]))
                elif self.state == constants.GameState.FIM_DE_JOGO:
                    self.state = constants.GameState.MENU

    def update(self):
        if self.state == constants.GameState.JOGANDO:
            keys = pygame.key.get_pressed()
            self.p1.move(keys[pygame.K_UP], keys[pygame.K_DOWN])
            self.p2.auto_move(self.ball.rect.centery)
            self.ball.update()

            if self.ball.rect.colliderect(self.p1.rect) and self.ball.vel_x < 0:
                self.ball.bounce()
            if self.ball.rect.colliderect(self.p2.rect) and self.ball.vel_x > 0:
                self.ball.bounce()

            if self.ball.rect.left < 0:
                self.score2 += 1
                self.ball.reset(1)
            elif self.ball.rect.right > constants.LARGURA_TELA:
                self.score1 += 1
                self.ball.reset(-1)

            if self.score1 >= constants.PONTOS_PARA_VENCER or self.score2 >= constants.PONTOS_PARA_VENCER:
                self.state = constants.GameState.FIM_DE_JOGO

    def run(self):
        while True:
            self.handle_events()
            self.update()
            
            if self.state == constants.GameState.MENU:
                self.renderer.draw_menu()
            elif self.state == constants.GameState.JOGANDO:
                self.renderer.draw_game(self.p1, self.p2, self.ball, self.score1, self.score2)
            elif self.state == constants.GameState.FIM_DE_JOGO:
                winner = "Jogador 1" if self.score1 >= constants.PONTOS_PARA_VENCER else "Robot"
                self.renderer.draw_game_over(winner)

            pygame.display.flip()
            self.clock.tick(constants.FPS)
