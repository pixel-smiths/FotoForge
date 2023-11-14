import pygame
import Fotoforge
from LayerManager import LayerManager

pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("FotoForge")
screen.fill((255, 255, 255))

layer_manager = LayerManager(screen)

button_color = (0, 255, 0)
button_text = "New From Image"
button_font = pygame.font.Font(None, 36)

button_surface = button_font.render(button_text, True, button_color)
button_rect = button_surface.get_rect()
screen.blit(button_surface, button_rect)

add_layer_button_color = (255, 0, 0)
add_layer_button_text = "Add Layer"
add_layer_button_font = pygame.font.Font(None, 36)

add_layer_button_surface = add_layer_button_font.render(add_layer_button_text, True, add_layer_button_color)
add_layer_button_rect = add_layer_button_surface.get_rect()
add_layer_button_rect.topleft = (screen.get_width() - add_layer_button_rect.width - 10, 10)
screen.blit(add_layer_button_surface, add_layer_button_rect)

upload_image_button_color = (0, 0, 255)
upload_image_button_text = "Upload Image"
upload_image_button_font = pygame.font.Font(None, 36)

upload_image_button_surface = upload_image_button_font.render(upload_image_button_text, True, upload_image_button_color)
upload_image_button_rect = upload_image_button_surface.get_rect()
upload_image_button_rect.topleft = (10, 60)
screen.blit(upload_image_button_surface, upload_image_button_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("New from image is clicked")
                Fotoforge.newFromImage(screen)
                layer_manager.add_layer()

            # elif add_layer_button_rect.collidepoint(event.pos):
            #     print("Add layer is clicked")
            #     layer_manager.add_layer()

            elif upload_image_button_rect.collidepoint(event.pos):
                print("Upload image is clicked")
                layer_manager.upload_image_to_active_layer()
            elif add_layer_button_rect.collidepoint(event.pos):
                 print("Add layer is clicked")
                 layer_manager.add_layer()
                 layer_manager.upload_image_to_active_layer()

    for layer in (layer_manager.layers):
        if layer.images:
            layer.update_layer()
    # Clear the screen
    # screen.fill((255, 255, 255))

    # # Draw all layers onto the screen in order
    # for layer in layer_manager.layers:
    #     screen.blit(layer.surface, (0, 0))

    # # Draw the buttons onto the screen
    # screen.blit(button_surface, button_rect)
    # screen.blit(add_layer_button_surface, add_layer_button_rect)
    # screen.blit(upload_image_button_surface, upload_image_button_rect)

    pygame.display.update()

   


   

  



   





        

        
 


   