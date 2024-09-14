import pygame

class Window():
    def __init__(self,w,h):
        self.win = pygame.display.set_mode((w,h))