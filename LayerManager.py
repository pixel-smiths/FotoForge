# import os
# from tkinter import Tk
# from tkinter.filedialog import askopenfilename
# import pygame

# class Layer:
#     def __init__(self, surface):
#         self.surface = surface
#         self.images = []  # Store a list of images
#         self.rects = []   # Store a list of corresponding rectangles
        

#         self.surface.set_alpha(10)
#         # Other initialization code...

#     # def blit_image(self, image, rect):
#     #     # Append the new image and rectangle to the lists
#     #     self.images.append(image)
#     #     self.rects.append(rect)

#     def blit_image(self, image, rect):
#         image = image.convert_alpha()  # Ensure the image supports per-pixel alpha
#         image.fill((255, 255, 255, 128), special_flags=pygame.BLEND_RGBA_MULT)  # Set the alpha value of the image
#         self.images.append(image)
#         self.rects.append(rect)

#     # def update_layer(self):
#     # # If there are images to blit onto the layer, fill the layer with a fully transparent color
#     #     if self.images:
#     #         self.surface.fill((0, 0, 0, 0))
#     # # If there are no images, fill the layer with a fully opaque white color
#     #     else:
#     #        self.surface.fill((255, 255, 255))

#     # # Blit all images onto the layer
#     #     for image, rect in zip(self.images, self.rects):
#     #         self.surface.blit(image, rect)

#     def update_layer(self):
#         # Clear the layer
#         self.surface.fill((250,250,250,0))
#          # Blit all images onto the layer with transparency
#         for image, rect in zip(self.images, self.rects):
#             self.surface.blit(image, rect.topleft)

#         # # Blit all images onto the layer
#         # for image, rect in zip(self.images, self.rects):
#         #     self.surface.blit(image, rect)
# # class Layer:
# #     def __init__(self, surface):
# #         self.surface = pygame.Surface(surface.get_size(), pygame.SRCALPHA)  # Create a surface that supports per-pixel alpha
# #         self.images = []
# #         self.rects = []

# #     def blit_image(self, image, rect):
# #         image = image.convert_alpha()  # Ensure the image supports per-pixel alpha
# #         self.images.append(image)
# #         self.rects.append(rect)

# #     def update_layer(self):
# #         self.surface.fill((0, 0, 0, 0))  # Fill the layer with fully transparent color

# #         for image, rect in zip(self.images, self.rects):
# #             self.surface.blit(image, rect)


# class LayerManager:
#     def __init__(self, surface):
#         self.surface = surface
#         self.layers = []
#         self.active_layer = None

#     def add_layer(self):
#         layer = Layer(self.surface)
#         self.layers.append(layer)
#         self.active_layer = layer
#     # def add_layer(self):
#     #     width, height = self.surface.get_size()
#     #     new_layer = Layer(width, height)
#     #     self.layers.append(new_layer)
#     #     self.active_layer = new_layer

#     def add_layer_with_image(self, file_path):
#         self.add_layer()  # create a new layer and set it as the active layer
#         self.upload_image_to_active_layer(file_path)  # upload the image to the active layer

#     # def upload_image_to_active_layer(self, file_path):
#     #     if self.active_layer is not None:
#     #         image = pygame.image.load(file_path)

#     #         image_rect = image.get_rect()
#     #         image_rect.center = (self.surface.get_width() / 2, self.surface.get_height() / 2)

#     #         self.active_layer.blit_image(image, image_rect)

#     # def upload_image_to_active_layer(self):
#     #     if self.active_layer is not None:
#     #         pygame.display.set_caption("Select an Image for Layer")
#     #         Tk().withdraw()
#     #         filename = askopenfilename()
#     #         image = pygame.image.load(filename)

#     #         image_rect = image.get_rect()
#     #         image_rect.center = (self.surface.get_width() / 2, self.surface.get_height() / 2)

#     #         pygame.display.set_caption(os.path.basename(filename))
#     #         pygame.display.update()

#     #         self.active_layer.blit_image(image, image_rect)
#     #         pygame.display.update()
#     def upload_image_to_active_layer(self):
#       if self.active_layer is not None:
#            pygame.display.set_caption("Select an Image for Layer")
#            Tk().withdraw()
#            filename = askopenfilename()
#            image = pygame.image.load(filename)

#         # Get the size of the image and the window
#            image_width, image_height = image.get_size()
#            window_width, window_height = self.surface.get_size()

#         # Calculate the scaling factors
#            width_scale = window_width / image_width
#            height_scale = window_height / image_height

#         # Choose the smaller scaling factor
#            scale = min(width_scale, height_scale)

#         # Scale the image
#            if scale < 1.0:  # only scale down, not up
#               image = pygame.transform.scale(image, (int(image_width * scale), int(image_height * scale)))

#            image_rect = image.get_rect()
#            image_rect.center = (window_width / 2, window_height / 2)

#            pygame.display.set_caption(os.path.basename(filename))
#            pygame.display.update()

#            self.active_layer.blit_image(image, image_rect)
#            pygame.display.update()











            



   
