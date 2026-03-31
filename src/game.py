import pygame
import sys
import random
import time
import src.constants as constants
from src.entities import Paddle, Ball
from src.renderer import Renderer
from src.audio import AudioManager

class PongGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.LARGURA_TELA, constants.ALTURA_TELA))
        pygame.display.set_caption("Ping Pong")
        self.clock = pygame.time.Clock()
        self.renderer = Renderer(self.screen)
        self.audio = AudioManager()
        self.reset_game()

    def reset_game(self):
        self.state = constants.GameState.MENU
        self.p1 = Paddle(15, constants.ALTURA_TELA // 2 - constants.ALTURA_RAQUETE // 2, constants.VELOCIDADE_JOGADOR)
        self.p2 = Paddle(constants.LARGURA_TELA - 15 - constants.LARGURA_RAQUETE, constants.ALTURA_TELA // 2 - constants.ALTURA_RAQUETE // 2, constants.VELOCIDADE_IA)
        
        self.balls = [Ball()] 
        self.score1 = 0
        self.score2 = 0
        self.last_powerup_time = time.time()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if self.state == constants.GameState.MENU:
                    self.state = constants.GameState.JOGANDO
                    self.score1, self.score2 = 0, 0
                    self.balls = [Ball()]
                    self.balls[0].reset(random.choice([-1, 1]))
                    self.audio.start_bg_music()
                elif self.state == constants.GameState.FIM_DE_JOGO:
                    self.state = constants.GameState.MENU

    def spawn_distractions(self, original_ball):
        for _ in range(3):
            random_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            distraction = Ball(color=random_color, is_real=False)
            distraction.rect.center = original_ball.rect.center
            distraction.vel_x = original_ball.vel_x * random.uniform(0.8, 1.2)
            distraction.vel_y = original_ball.vel_y * random.uniform(-1.5, 1.5)
            self.balls.append(distraction)

    def update(self):
        if self.state == constants.GameState.JOGANDO:
            keys = pygame.key.get_pressed()
            self.p1.move(keys[pygame.K_UP], keys[pygame.K_DOWN])
            
            real_ball = next((b for b in self.balls if b.is_real), self.balls[0])
            self.p2.auto_move(real_ball.rect.centery)

            current_time = time.time()
            
            for ball in self.balls[:]:
                if ball.update():
                    self.audio.play("hit_wall")

                if ball.rect.colliderect(self.p1.rect) and ball.vel_x < 0:
                    ball.bounce()
                    self.audio.play("hit_paddle")
                    
                    if current_time - self.last_powerup_time >= 5:
                        self.spawn_distractions(ball)
                        self.last_powerup_time = current_time

                if ball.rect.colliderect(self.p2.rect) and ball.vel_x > 0:
                    ball.bounce()
                    self.audio.play("hit_paddle") 

                if ball.rect.left < 0:
                    if ball.is_real:
                        self.score2 += 1
                        self.audio.play("score") 
                        self.balls = [Ball()] 
                        self.balls[0].reset(1)
                        break
                    else:
                        self.balls.remove(ball)
                elif ball.rect.right > constants.LARGURA_TELA:
                    if ball.is_real:
                        self.score1 += 1
                        self.audio.play("score")
                        self.balls = [Ball()] 
                        self.balls[0].reset(-1)
                        break
                    else:
                        self.balls.remove(ball)

            if self.score1 >= constants.PONTOS_PARA_VENCER or self.score2 >= constants.PONTOS_PARA_VENCER:
                self.state = constants.GameState.FIM_DE_JOGO

    def run(self):
        while True:
            self.handle_events()
            self.update()
            
            if self.state == constants.GameState.MENU:
                self.renderer.draw_menu()
            elif self.state == constants.GameState.JOGANDO:
                if not pygame.mixer.music.get_busy():
                    self.audio.start_bg_music()
                self.renderer.draw_game(self.p1, self.p2, self.balls, self.score1, self.score2)
            elif self.state == constants.GameState.FIM_DE_JOGO:
                winner = "Jogador 1" if self.score1 >= constants.PONTOS_PARA_VENCER else "Jogador 2"
                self.renderer.draw_game_over(winner)

            pygame.display.flip()
            self.clock.tick(constants.FPS)
