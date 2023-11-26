import pygame
import pygame_gui
from pygame.locals import *
from tkinter import filedialog
from PIL import Image

class Layer:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.photo_image = self.image.copy()
        self.dragging = False  # Add this line

class ImageWindow:
    def __init__(self):
        pygame.init()
        self.manager = pygame_gui.UIManager((800, 600))
        self.layers = []
        self.current_layer = None
        self.count = 0
        self.layer_buttons = []
        self.photo_images = []
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Image Window")

        self.create_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 5), (100, 50)), text='Create Layer', manager=self.manager)
        self.opacity_entries = {}
    # def create_layer(self):
    #     file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    #     if file_path:
    #         layer = Layer(file_path)
    #         self.layers.append(layer)
    #         self.current_layer = layer
    #         self.count += 1
    #         layer_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 5 + self.count * 55), (100, 50)), text=f'Layer {self.count}', manager=self.manager)
    #         self.layer_buttons.append(layer_button)
    #         opacity_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 60 + self.count * 55), (100, 20)), manager=self.manager)
    #         self.opacity_entries[layer_button] = opacity_entry
    #         self.photo_images.append(layer.photo_image)
    def create_layer(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            layer = Layer(file_path)
            self.layers.append(layer)
            self.current_layer = layer
            self.count += 1
            layer_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 5 + self.count * 55), (100, 50)), text=f'Layer {self.count}', manager=self.manager)
            self.layer_buttons.append(layer_button)
            opacity_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((450, 5 + self.count * 55), (100, 20)), manager=self.manager)  # Adjusted position
            self.opacity_entries[layer_button] = opacity_entry
            self.photo_images.append(layer.photo_image)
    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            time_delta = clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.create_button:
                            self.create_layer()
                        elif event.ui_element in self.layer_buttons:
                             self.current_layer = self.layers[self.layer_buttons.index(event.ui_element)]
                             for  button, entry in self.opacity_entries.items():
                                if button==event.ui_element:
                                   entry.show()
                                   entry.focus()
                                else:
                                 entry.hide()
                              
                    elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                        if event.ui_element in self.opacity_entries.values() and self.current_layer:
                            self.current_layer.image.set_alpha(int(event.text) * 2.55)
                            for button, entry in self.opacity_entries.items():
                                if self.current_layer == self.layers[self.layer_buttons.index(button)]:
                                    entry.show()
                                else:
                                    entry.hide()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for layer in reversed(self.layers):
                        if layer.rect.collidepoint(event.pos):
                            self.current_layer = layer
                            layer.dragging = True
                            layer.drag_offset = (event.pos[0] - layer.rect.x, event.pos[1] - layer.rect.y)
                            break

                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.current_layer:
                        self.current_layer.dragging = False
                
                elif event.type == pygame.MOUSEMOTION:
                    if self.current_layer and self.current_layer.dragging:
                        self.current_layer.rect.x = event.pos[0] - self.current_layer.drag_offset[0]
                        self.current_layer.rect.y = event.pos[1] - self.current_layer.drag_offset[1]
                self.manager.process_events(event)
            self.manager.update(time_delta)

            self.screen.fill((255, 255, 255))

            for layer in self.layers:
                self.screen.blit(layer.image, layer.rect)

            self.manager.draw_ui(self.screen)

            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    window = ImageWindow()
    window.run()