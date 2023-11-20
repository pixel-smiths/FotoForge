import pygame
pygame.init()

class Tool:
    def __init__(self, name, icon):
        self.name = name
        self.icon = icon
        self.left = 0
        self.top = 0
        # add attributes for rectangle and index (see Toolbar.py)
        self.rect = None
        self.index = None
    
    def draw(self, surface):
        # draw tool
        surface.blit(self.icon, self.rect)