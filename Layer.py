import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pygame
import io
from PIL import Image
from tkinter import Tk
from PIL import ImageGrab



class Layer:
    def __init__(self, surface):
        self.surface = surface

    def createLayer(self):
        pygame.display.set_caption("Select an Image for New Layer")
        Tk().withdraw()
        filename = askopenfilename()
        image = pygame.image.load(filename)

        image = pygame.transform.scale(image, (self.surface.get_width() - 50, self.surface.get_height() - 50))
        image_rect = image.get_rect()
        image_rect.center = (self.surface.get_width() / 2, self.surface.get_height() / 2)

        pygame.display.set_caption(os.path.basename(filename))
        pygame.display.update()

        self.surface.blit(image, image_rect)

        pygame.display.update()











            



   
