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
        self.image=None
        self.rect=None

    def createLayer(self):
        pygame.display.set_caption("Select an Image for New Layer")
        Tk().withdraw()
        filename = askopenfilename()
        self.image = pygame.image.load(filename)

        self.image = pygame.transform.scale(self.image, (self.surface.get_width() - 50, self.surface.get_height() - 50))
        image_rect = self.image.get_rect()
        image_rect.center = (self.surface.get_width() / 2, self.surface.get_height() / 2)

        #attribute to store position of the image
        self.rect = self.image.get_rect()
        self.rect.center = (self.surface.get_width() / 2, self.surface.get_height() / 2)

        pygame.display.set_caption(os.path.basename(filename))
        pygame.display.update()

        self.surface.blit(self.image, image_rect)

        pygame.display.update()
    
    # def adjustOpacity(self, alpha_percentage):
    #     # Convert the percentage to an alpha value between 0 and 255
    #     alpha_value = int(alpha_percentage * 255 / 100)
        
    #     # Create a copy of the image to avoid modifying the original image
    #     image_copy = self.image.copy()

    #     # Set the alpha value of the image copy
    #     image_copy.set_alpha(alpha_value)

    #     # Replace the image with the image copy
    #     self.image = image_copy

    #      # Re-draw the image onto the surface
    #     self.surface.blit(self.image, self.rect)

    #     # Update the display
    #     pygame.display.update()

    def adjustOpacity(self, alpha_percentage):
       # Convert the percentage to an alpha value between 0 and 255
        alpha_value = int(alpha_percentage * 255 / 100)

         # Create a copy of the image to avoid modifying the original image
        image_copy = self.image.copy()

       # Create a new image with the same size and color depth as the original image
        new_image = pygame.Surface(image_copy.get_size(), pygame.SRCALPHA)

    # Iterate over each pixel in the image copy
        for x in range(image_copy.get_width()):
            for y in range(image_copy.get_height()):
            # Get the color of the pixel
              color = image_copy.get_at((x, y))

            # Change the alpha value of the color
              color.a = alpha_value

            # Set the color of the pixel in the new image
              new_image.set_at((x, y), color)

    # Replace the image with the new image
        self.image = new_image

    # Clear the surface
        self.surface.fill((0, 0, 0))

    # Re-draw the image onto the surface
        self.surface.blit(self.image, self.rect)

    # Re-draw the buttons
        self.surface.blit(self.button_surface, self.button_rect)
        self.surface.blit(self.button_surface_layer, self.button_rect_layer)

    # Update the display
        pygame.display.update()











            



   
