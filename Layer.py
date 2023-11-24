import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pygame
import io
from PIL import Image
from tkinter import Tk
from PIL import ImageGrab
import pygame_gui

# Define a dictionary to store the visibility status of each image
# image_visibility = {}

def draw_buttons(screen, button_surface, button_rect, button_surface_layer, button_rect_layer):
    screen.blit(button_surface, button_rect)
    screen.blit(button_surface_layer, button_rect_layer)

class Layer:
    def __init__(self, surface):
        self.surface = surface
        self.image=None
        self.rect=None



    def createLayer(self, image_names, manager,button_surface, button_rect, button_surface_layer, button_rect_layer):
        pygame.display.set_caption("Select an Image for New Layer")
        Tk().withdraw()
        filename = askopenfilename()

    # Calculate the position of the new UILabel
        label_top = 100 + len(image_names) * 20  # 20px height for each label
    # Create a new UILabel for the image name
        image_name_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, label_top), (780, 20)), text=os.path.basename(filename), manager=manager)
    
    # Add the image name to the list
        image_names.append(os.path.basename(filename))

        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (self.surface.get_width() - 50, self.surface.get_height() - 50))
        image_rect = self.image.get_rect()
        image_rect.center = (self.surface.get_width() / 2, self.surface.get_height() / 2)

         # Store the button surfaces and rectangles in the Layer instance
        self.button_surface = button_surface
        self.button_rect = button_rect
        self.button_surface_layer = button_surface_layer
        self.button_rect_layer = button_rect_layer

    #attribute to store position of the image
        self.rect = self.image.get_rect()
        self.rect.center = (self.surface.get_width() / 2, self.surface.get_height() / 2)

        pygame.display.set_caption(os.path.basename(filename))
        pygame.display.update()

        self.surface.blit(self.image, image_rect)
        pygame.display.update()


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
    #    # Convert the percentage to an alpha value between 0 and 255
    #     alpha_value = int(alpha_percentage * 255 / 100)

    #      # Create a copy of the image to avoid modifying the original image
    #     image_copy = self.image.copy()

    #    # Create a new image with the same size and color depth as the original image
    #     new_image = pygame.Surface(image_copy.get_size(), pygame.SRCALPHA)

    # # Iterate over each pixel in the image copy
    #     for x in range(image_copy.get_width()):
    #         for y in range(image_copy.get_height()):
    #         # Get the color of the pixel
    #           color = image_copy.get_at((x, y))

    #         # Change the alpha value of the color
    #           color.a = alpha_value

    #         # Set the color of the pixel in the new image
    #           new_image.set_at((x, y), color)

    # # Replace the image with the new image
    #     self.image = new_image

    # Clear the surface
        self.surface.fill((0, 0, 0))

    # Re-draw the image onto the surface
        self.surface.blit(self.image, self.rect)

    # Re-draw the buttons
        self.surface.blit(self.button_surface, self.button_rect)
        self.surface.blit(self.button_surface_layer, self.button_rect_layer)

        # Redraw the buttons
        draw_buttons(self.surface, self.button_surface, self.button_rect, self.button_surface_layer, self.button_rect_layer)

    # Update the display
        pygame.display.update()










            



   










            



   










            



   










            



   










            



   










            



   
