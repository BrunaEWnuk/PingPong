import pygame
import src.constants as constants

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font_score = pygame.font.Font(None, 50)
        self.font_text = pygame.font.Font(None, 36)

    def draw_game(self, p1, p2, ball, score1, score2):
        self.screen.fill(constants.COR_FUNDO)
        pygame.draw.aaline(self.screen, constants.COR_ELEMENTOS, (constants.LARGURA_TELA // 2, 0), (constants.LARGURA_TELA // 2, constants.ALTURA_TELA))
        pygame.draw.rect(self.screen, constants.COR_ELEMENTOS, p1.rect)
        pygame.draw.rect(self.screen, constants.COR_ELEMENTOS, p2.rect)
        pygame.draw.ellipse(self.screen, constants.COR_ELEMENTOS, ball.rect)
        
        score_text = self.font_score.render(f"{score1}   {score2}", True, constants.COR_ELEMENTOS)
        self.screen.blit(score_text, score_text.get_rect(center=(constants.LARGURA_TELA // 2, 40)))

    def draw_menu(self):
        self.screen.fill(constants.COR_FUNDO)
        title = self.font_score.render("PONG", True, constants.COR_ELEMENTOS)
        instr = self.font_text.render("Pressione ESPAÇO para Jogar", True, constants.COR_ELEMENTOS)
        self.screen.blit(title, title.get_rect(center=(constants.LARGURA_TELA // 2, constants.ALTURA_TELA // 3)))
        if pygame.time.get_ticks() % 1000 < 500:
            self.screen.blit(instr, instr.get_rect(center=(constants.LARGURA_TELA // 2, constants.ALTURA_TELA // 2)))

    def draw_game_over(self, winner):
        self.screen.fill(constants.COR_FUNDO)
        winner_text = self.font_score.render(f"{winner} Venceu!", True, constants.COR_ELEMENTOS)
        restart_text = self.font_text.render("Pressione ESPAÇO para Menu", True, constants.COR_ELEMENTOS)
        self.screen.blit(winner_text, winner_text.get_rect(center=(constants.LARGURA_TELA // 2, constants.ALTURA_TELA // 3)))
        self.screen.blit(restart_text, restart_text.get_rect(center=(constants.LARGURA_TELA // 2, constants.ALTURA_TELA // 2)))
