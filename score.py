import pygame


class Score:
    def __init__(self):
        self.white = 255, 255, 255
        self.count = 0
        self.font = pygame.font.SysFont(None, 50)
        self.text = self.font.render(f"Score : {self.count}", 1, self.white)

    def show_score(self, screen):
        screen.blit(self.text, (10, 10))

    def score_up(self):
        self.count += 1
        self.text = self.font.render(f"Score : {self.count}", 1, self.white)
