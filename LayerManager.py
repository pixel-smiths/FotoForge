import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pygame
from PIL import Image
from tkinter import Tk
from PIL import ImageGrab

class LayerManager:
    # Add these lines after creating the LayerManager instance
      
 
    def __init__(self, surface):
        self.surface = surface
        self.layers = []
        self.active_layer = None
        self.opacity_slider_value = 100  # Default opacity value

    # def add_layer(self):
    #     layer = Layer(self.surface)
    #     self.layers.append(layer)
    #     self.active_layer = layer
    def add_layer(self):
        layer = Layer(self.surface)
        self.layers.append(layer)
        self.active_layer = layer

        # Clear the layer
        self.active_layer.clear_layer()

        # Blit all images onto the new layer with opacity
        for (image, opacity), rect in zip(self.active_layer.images, self.active_layer.rects):
            # Create a copy of the image with the desired opacity
            alpha_surface = pygame.Surface(image.get_size(), pygame.SRCALPHA)
            alpha_surface.fill((255, 255, 255, opacity))
            image_copy = pygame.Surface(image.get_size(), pygame.SRCALPHA)
            image_copy.blit(alpha_surface, (0, 0))
            image_copy.blit(image, (0, 0))

            # Blit the image onto the new layer
  # Clear the layer
        self.surface.fill((255, 255, 255))

        # Blit all images onto the layer with opacity
        for (image, opacity), rect in zip(self.images, self.rects):
            # Create a copy of the image with the desired opacity
            alpha_surface = pygame.Surface(image.get_size(), pygame.SRCALPHA)
            alpha_surface.fill((255, 255, 255, opacity))
            image_copy = pygame.Surface(image.get_size(), pygame.SRCALPHA)
            image_copy.blit(alpha_surface, (0, 0))
            image_copy.blit(image, (0, 0))

            # Blit the image onto the layer
            self.surface.blit(image_copy, rect)
    def update_opacity_slider(self, new_value):
        # Clamp the new value between 0 and 100
        self.opacity_slider_value = max(0, min(new_value, 100))

    def upload_image_to_active_layer(self):
        if self.active_layer is not None:
            # Set the caption of the Pygame window to "Select an Image"
            pygame.display.set_caption("Select an Image for Layer")

            # Open a file system dialog to select an image
            Tk().withdraw()
            filename = askopenfilename()

            # Load the selected image
            image = pygame.image.load(filename)

            # Resize image to keep sizing right but to be 100 pixels less than the screen and centered on the screen
            #make image to be it's orginal size but also fit in the window
            #image = pygame.transform.scale(image, (self.surface.get_width() - 50, self.surface.get_height() - 50))

            #image = pygame.transform.scale(image, (self.surface.get_width() - 250, self.surface.get_height() - 250))
            # Center image on the active layer
            image_rect = image.get_rect()
            image_rect.center = (self.surface.get_width() / 2, self.surface.get_height() / 2)

            # Set the caption of the Pygame window to the name of the selected image
            pygame.display.set_caption(os.path.basename(filename))

            # Update the Pygame window
            pygame.display.update()

            # Blit the loaded image onto the active layer
            self.active_layer.blit_image(image, image_rect)

             # Center image on the active layer without resizing
            image_rect.center = self.active_layer.surface.get_rect().center

            # Blit the loaded image onto the active layer
            self.active_layer.blit_image(image, image_rect)

            # Update the original Pygame surface
            pygame.display.update()
            #   # Blit the loaded image onto the active layer
            # self.active_layer.blit_image(image, image_rect)

            # # Update the original Pygame surface
            # pygame.display.update()

            # def move_image(image_rect, direction, pixels):
            #   if direction == "up":
            #    image_rect.y -= pixels
            #   elif direction == "down":
            #    image_rect.y += pixels
            #   elif direction == "left":
            #     image_rect.x -= pixels
            #   elif direction == "right":
            #     image_rect.x += pixels


# class Layer:
#     def __init__(self, surface):
#         self.surface = surface
#         self.image = None

#     def blit_image(self, image, rect):
#         self.image = image
#         self.rect = rect
#         self.surface.blit(self.image, self.rect)
# class Layer:
#     def __init__(self, surface):
#         self.surface = surface
#         self.images = []  # Store a list of images
#         self.rects = []   # Store a list of corresponding rectangles

#     def blit_image(self, image, rect):
#         self.images.append(image)
#         self.rects.append(rect)
#         self.update_layer()

#     def update_layer(self):
#         self.surface.fill((255, 255, 255))  # Clear the layer
#         for image, rect in zip(self.images, self.rects):
#             self.surface.blit(image, rect)
# class Layer:
#     def __init__(self, surface):
#         self.surface = surface
#         self.images = []  # Store a list of images
#         self.rects = []   # Store a list of corresponding rectangles

#     def blit_image(self, image, rect):
#         # Store the original size of the image
#         original_size = image.get_size()

#         # Create a new rectangle for the image based on its original size
#         new_rect = pygame.Rect(rect.topleft, original_size)

#         # Append the new image and rectangle to the lists
#         self.images.append(image)
#         self.rects.append(new_rect)

#         # Update the layer
#         self.update_layer()

#     def update_layer(self):
#         self.surface.fill((255, 255, 255))  # Clear the layer
#         for image, rect in zip(self.images, self.rects):
#             self.surface.blit(image, rect)
# class Layer:
#     def __init__(self, surface):
#         self.surface = surface
#         self.images = []  # Store a list of images
#         self.rects = []   # Store a list of corresponding rectangles

#     def blit_image(self, image, rect):
#         # Store the original size of the image
#         original_size = image.get_size()

#         # Create a new rectangle for the image based on its original size
#         new_rect = pygame.Rect(rect.topleft, original_size)

#         # Append the new image and rectangle to the lists
#         self.images.append(image)
#         self.rects.append(new_rect)

#     def update_layer(self):
#         # Clear the layer
#         self.surface.fill((255, 255, 255))
        
#         # Blit all images onto the layer
#         for image, rect in zip(self.images, self.rects):
#             self.surface.blit(image, rect)
class Layer:
    def __init__(self, surface):
        self.surface = surface
        self.images = []  # Store a list of images
        self.rects = []   # Store a list of corresponding rectangles

    def blit_image(self, image, rect):
        # Append the new image and rectangle to the lists
        self.images.append(image)
        self.rects.append(rect)

    # def update_layer(self):
    #     # Clear the layer
    #     self.surface.fill((255, 255, 255))
        
    #     # Blit all images onto the layer
    #     for image, rect in zip(self.images, self.rects):
    #         self.surface.blit(image, rect)
    def update_layer(self):
        # Clear the layer
        self.surface.fill((255, 255, 255))

        # Blit all images onto the layer with opacity
        for (image, opacity), rect in zip(self.images, self.rects):
            # Create a copy of the image with the desired opacity
            alpha_surface = pygame.Surface(image.get_size(), pygame.SRCALPHA)
            alpha_surface.fill((255, 255, 255, opacity))
            image_copy = pygame.Surface(image.get_size(), pygame.SRCALPHA)
            image_copy.blit(alpha_surface, (0, 0))
            image_copy.blit(image, (0, 0))

            # Blit the image onto the layer
            self.surface.blit(image_copy, rect)

    def blit_image(self, image, rect):
        # Append the new image, rectangle, and opacity to the lists
        opacity = layer_manager.opacity_slider_value
        self.images.append((image, opacity))
        self.rects.append(rect)












            



   
