# from LayerManager import LayerManager

# layer_manager = LayerManager(screen)


# # Define button properties for "Add Layer" button
# add_layer_button_color = (255, 0, 0)  # Choose your color
# add_layer_button_text = "Add Layer"
# add_layer_button_font = pygame.font.Font(None, 36)

# # Create "Add Layer" button surface
# add_layer_button_surface = add_layer_button_font.render(add_layer_button_text, True, add_layer_button_color)

# # Get "Add Layer" button surface rectangle
# add_layer_button_rect = add_layer_button_surface.get_rect()

# # Set the position of the "Add Layer" button
# add_layer_button_rect.topleft = (10, 10)  # Adjust the position as needed

# # Draw "Add Layer" button on screen
# screen.blit(add_layer_button_surface, add_layer_button_rect)

# # Define button properties for "Upload Image" button
# upload_image_button_color = (0, 0, 255)  # Choose your color
# upload_image_button_text = "Upload Image"
# upload_image_button_font = pygame.font.Font(None, 36)

# # Create "Upload Image" button surface
# upload_image_button_surface = upload_image_button_font.render(upload_image_button_text, True, upload_image_button_color)

# # Get "Upload Image" button surface rectangle
# upload_image_button_rect = upload_image_button_surface.get_rect()

# # Set the position of the "Upload Image" button
# upload_image_button_rect.topleft = (10, 60)  # Adjust the position as needed

# # Draw "Upload Image" button on screen
# screen.blit(upload_image_button_surface, upload_image_button_rect)

# import pygame
# import Fotoforge

# # Initialize Pygame
# pygame.init()

# # Set the size of the window
# window_size = (800, 600)

# # Create the window
# screen = pygame.display.set_mode(window_size)

# # Set the title of the window
# pygame.display.set_caption("FotoForge")

# # Set background color
# screen.fill((255, 255, 255))

# # Define button properties
# button_color = (0, 255, 0)
# button_text = "New From Image"
# button_font = pygame.font.Font(None, 36)

# # Create button surface
# button_surface = button_font.render(button_text, True, button_color)

# # Get button surface rectangle
# button_rect = button_surface.get_rect()

# # Draw button on screen
# screen.blit(button_surface, button_rect)

# # Run the game loop
# while True:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             # Quit the game if the user closes the window
#             pygame.quit()
#             exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # Check if the button was clicked
#             if button_rect.collidepoint(event.pos):
#                 # Call the openFromImage() function
#                 Fotoforge.newFromImage(screen)
#         #if the keypress is ctrl+v, paste the clipboard
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
#                 Fotoforge.PasteClipboard(screen)

#  # Add the following code inside your game loop to handle button click events
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#           if button_rect.collidepoint(event.pos):
#            Fotoforge.newFromImage(screen)
#            layer_manager.add_layer()

#     # Check if the "Add Layer" button was clicked
#         elif add_layer_button_rect.collidepoint(event.pos):
#          layer_manager.add_layer()

#     # Check if the "Upload Image to Active Layer" button was clicked
#         elif upload_image_button_rect.collidepoint(event.pos):
#          layer_manager.upload_image_to_active_layer()

# # Add these lines at the end of your game loop
#     for layer in layer_manager.layers:
#            if layer.image is not None:
#             screen.blit(layer.image, layer.rect)
#           # Update the screen
#     pygame.display.update()
import pygame
import Fotoforge
from LayerManager import LayerManager

# Initialize Pygame
pygame.init()

# Set the size of the window
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("FotoForge")

# Set background color
screen.fill((255, 255, 255))
#create instance of layer manager
layer_manager = LayerManager(screen)

# Define button properties
button_color = (0, 255, 0)
button_text = "New From Image"
button_font = pygame.font.Font(None, 36)

# Create button surface
button_surface = button_font.render(button_text, True, button_color)

# Get button surface rectangle
button_rect = button_surface.get_rect()

# Draw button on screen
screen.blit(button_surface, button_rect)



# Create the LayerManager instance
layer_manager = LayerManager(screen)

# Add these lines after creating the LayerManager instance
opacity_slider_rect = pygame.Rect(10, 110, 200, 20)  # Adjust the position and size as needed
opacity_slider_width = opacity_slider_rect.width

# Define button properties for "Add Layer" button
add_layer_button_color = (255, 0, 0)  # Choose your color
add_layer_button_text = "Add Layer"
add_layer_button_font = pygame.font.Font(None, 36)

# Create "Add Layer" button surface
add_layer_button_surface = add_layer_button_font.render(add_layer_button_text, True, add_layer_button_color)

# Get "Add Layer" button surface rectangle
add_layer_button_rect = add_layer_button_surface.get_rect()

# Set the position of the "Add Layer" button to be the right side of screen
add_layer_button_rect.topleft = (screen.get_width() - add_layer_button_rect.width - 10, 10)  # Adjust the position as needed

# Draw "Add Layer" button on screen
screen.blit(add_layer_button_surface, add_layer_button_rect)

# Define button properties for "Upload Image" button
upload_image_button_color = (0, 0, 255)  # Choose your color
upload_image_button_text = "Upload Image"
upload_image_button_font = pygame.font.Font(None, 36)

# Create "Upload Image" button surface
upload_image_button_surface = upload_image_button_font.render(upload_image_button_text, True, upload_image_button_color)

# Get "Upload Image" button surface rectangle
upload_image_button_rect = upload_image_button_surface.get_rect()

# Set the position of the "Upload Image" button
upload_image_button_rect.topleft = (10, 60)  # Adjust the position as needed

# Draw "Upload Image" button on screen
screen.blit(upload_image_button_surface, upload_image_button_rect)

# Run the game loop
# while True:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             # Quit the game if the user closes the window
#             pygame.quit()
#             exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # Check if the button was clicked
#             if button_rect.collidepoint(event.pos):
#                 # Call the openFromImage() function
#                 Fotoforge.newFromImage(screen)
#         # If the keypress is ctrl+v, paste the clipboard
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
#                 Fotoforge.PasteClipboard(screen)

#         # Add the following code inside your game loop to handle button click events
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if button_rect.collidepoint(event.pos):
#                 Fotoforge.newFromImage(screen)
#                 layer_manager.add_layer()

#             # Check if the "Add Layer" button was clicked
#             elif add_layer_button_rect.collidepoint(event.pos):
#                 layer_manager.add_layer()

#             # Check if the "Upload Image to Active Layer" button was clicked
#             elif upload_image_button_rect.collidepoint(event.pos):
#                 layer_manager.upload_image_to_active_layer()
# # Add these lines inside your game loop, after handling other events
#     pygame.draw.rect(screen, (0, 0, 0), opacity_slider_rect)  # Draw the slider background
#     slider_handle_pos = (opacity_slider_rect.left + (opacity_slider_width * layer_manager.opacity_slider_value / 100), opacity_slider_rect.centery)
#     pygame.draw.circle(screen, (255, 0, 0), slider_handle_pos, 10)  # Draw the slider handle

               

            

    
    

#     # # Add these lines at the end of your game loop
#     # for layer in layer_manager.layers:
#     #     if layer.image is not None:
#     #         screen.blit(layer.image, layer.rect)
#      # Add these lines at the end of your game loop
#     for layer in reversed(layer_manager.layers):
#         if layer.images:  # Check if the layer has any images
#             for image, rect in zip(layer.images, layer.rects):
#                 screen.blit(image, rect)

#     # Add these lines at the end of your game loop
#     for layer in reversed(layer_manager.layers):
#        if layer.images:  # Check if the layer has any images
#         layer.update_layer()

#     for event in pygame.event.get():
#      if event.type == pygame.MOUSEBUTTONDOWN:
#         # Check if the opacity slider was clicked
#         if opacity_slider_rect.collidepoint(event.pos):
#             # Update the opacity value based on the mouse position
#             normalized_x = min(max((event.pos[0] - opacity_slider_rect.left) / opacity_slider_width, 0), 1)
#             new_opacity_value = int(normalized_x * 100)
#             layer_manager.update_opacity_slider(new_opacity_value)

#      # Add these lines inside your game loop, after handling other events
#     pygame.draw.rect(screen, (0, 0, 0), opacity_slider_rect)  # Draw the slider background
#     slider_handle_pos = (
#         opacity_slider_rect.left + (opacity_slider_width * layer_manager.opacity_slider_value / 100),
#         opacity_slider_rect.centery
#     )
#     pygame.draw.circle(screen, (255, 0, 0), slider_handle_pos, 10) 

#      # Add these lines at the end of your game loop
#     for layer in reversed(layer_manager.layers):
#         if layer.images:
#             layer.update_layer()

#     # Update the screen
#     pygame.display.update()
# ... (previous code)

# Run the game loop
while True:
    # Handle events



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                Fotoforge.newFromImage(screen)
                layer_manager.add_layer()
            elif add_layer_button_rect.collidepoint(event.pos):
                layer_manager.add_layer()
            elif upload_image_button_rect.collidepoint(event.pos):
                layer_manager.upload_image_to_active_layer()
            elif opacity_slider_rect.collidepoint(event.pos):
                 normalized_x = min(max((event.pos[0] - opacity_slider_rect.left) / opacity_slider_width, 0), 1)
                 new_opacity_value = int(normalized_x * 100)
                 layer_manager.update_opacity_slider(new_opacity_value)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                   Fotoforge.PasteClipboard(screen)


        
    # for event in pygame.event.get():
        # if event.type == pygame.QUIT:
        #     pygame.quit()
        #     exit()
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if button_rect.collidepoint(event.pos):
        #         Fotoforge.newFromImage(screen)
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
        #         Fotoforge.PasteClipboard(screen)

        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if button_rect.collidepoint(event.pos):
        #         Fotoforge.newFromImage(screen)
        #         layer_manager.add_layer()

        #     elif add_layer_button_rect.collidepoint(event.pos):
        #         layer_manager.add_layer()

        #     elif upload_image_button_rect.collidepoint(event.pos):
        #         layer_manager.upload_image_to_active_layer()

        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if opacity_slider_rect.collidepoint(event.pos):
        #         normalized_x = min(max((event.pos[0] - opacity_slider_rect.left) / opacity_slider_width, 0), 1)
        #         new_opacity_value = int(normalized_x * 100)
        #         layer_manager.update_opacity_slider(new_opacity_value)

    # Draw the slider background
    pygame.draw.rect(screen, (0, 0, 0), opacity_slider_rect)
    
    # Draw the slider handle
    slider_handle_pos = (
        opacity_slider_rect.left + (opacity_slider_width * layer_manager.opacity_slider_value / 100),
        opacity_slider_rect.centery
    )
    pygame.draw.circle(screen, (255, 0, 0), slider_handle_pos, 10)

    # Update the layers
    for layer in reversed(layer_manager.layers):
        if layer.images:
            layer.update_layer()

    pygame.display.update()



   





        

        
 


   