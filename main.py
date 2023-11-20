import pygame
import Modules.FotoForge as FotoForge
from Modules.LayerManager import LayerManager
from Modules.Tool import Tool
from Modules.Toolbar import Toolbar
import os

def main():from Layer import Layer
def main():
    # Initialize top layer position

        # Initialize Pygame
        pygame.init()

    pygame.init()

        # Set the size of the window
    window_size = (800, 600)

        # Create the window
    screen = pygame.display.set_mode(window_size)

        # Set the title of the window
    pygame.display.set_caption("FotoForge")

        # Set background color
    screen.fill((255, 255, 255))

    layer_manager = LayerManager(screen)

    #upload from image button also known as New From Image
    button_color = (0, 255, 0)
    button_text = "New From Image"
    button_font = pygame.font.Font(None, 36)
    button_surface = button_font.render(button_text, True, button_color)
    button_rect = button_surface.get_rect()
    screen.blit(button_surface, button_rect)

    # create toolbar
    toolbar = Toolbar()
    blue_tool = Tool("Blue", pygame.image.load(os.path.join("assets", "blue_tool.png")))
    toolbar.add_tool(blue_tool)

    add_layer_button_color = (255, 0, 0)
    add_layer_button_text = "Add Layer"
    add_layer_button_font = pygame.font.Font(None, 36)

    add_layer_button_surface = add_layer_button_font.render(add_layer_button_text, True, add_layer_button_color)
    add_layer_button_rect = add_layer_button_surface.get_rect()
    add_layer_button_rect.topleft = (screen.get_width() - add_layer_button_rect.width - 10, 10)
    screen.blit(add_layer_button_surface, add_layer_button_rect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("New from image is clicked")
                    FotoForge.newFromImage(screen)
                    layer_manager.add_layer()

                # elif add_layer_button_rect.collidepoint(event.pos):
                #     print("Add layer is clicked")
                #     layer_manager.add_layer()

                # elif upload_image_button_rect.collidepoint(event.pos):
                #     print("Upload image is clicked")
                #     layer_manager.upload_image_to_active_layer()
                elif add_layer_button_rect.collidepoint(event.pos):
                    print("Add layer is clicked")
                    layer_manager.add_layer()
                    layer_manager.upload_image_to_active_layer()
            #clipboard
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    FotoForge.PasteClipboard(screen)
        # Update the screen
        pygame.display.update()
if __name__ == "__main__":
    main()
    exit()