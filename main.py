import pygame
import Modules.FotoForge
from Layer import Layer
import pygame_gui



def main():
    # Initialize top layer position

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



     # ... existing code ...

    # Define button properties for "Create Layer"
    button_color_layer = (0, 0, 255)
    button_text_layer = "Create Layer"
    button_font_layer = pygame.font.Font(None, 36)

    # Create button surface for "Create Layer"
    button_surface_layer = button_font_layer.render(button_text_layer, True, button_color_layer)

    # # Get button surface rectangle for "Create Layer"
    # button_rect_layer = button_surface_layer.get_rect()
    # button_rect_layer.topleft = (0, 50)  # Position it below the "New From Image" button
    # Get button surface rectangle for "Create Layer"
    button_rect_layer = button_surface_layer.get_rect()
    button_rect_layer.topright = (screen.get_width() - 10, 10)  # Position it at the upper right corner with a 10px margin

    # Draw button on screen
    screen.blit(button_surface_layer, button_rect_layer)

    # Create a Layer instance
    layer = Layer(screen)

    # Store the button surfaces and rectangles in the Layer instance
    layer.button_surface = button_surface
    layer.button_rect = button_rect
    layer.button_surface_layer = button_surface_layer
    layer.button_rect_layer = button_rect_layer

    # Create a UIManager instance
    manager = pygame_gui.UIManager(window_size)

# Create a UITextEntryLine instance
    # opacity_textbox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 50), (100, 50)), manager=manager)
  # Define the size of the textbox
    textbox_width = 50
    textbox_height = 30

    # Calculate the position of the textbox
    textbox_left = (window_size[0] - textbox_width) / 2
    textbox_top = 5  # 10px margin from the top

    # Create a UITextEntryLine instance
    opacity_textbox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((textbox_left, textbox_top), (textbox_width, textbox_height)), manager=manager)





    # Run the game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game if the user closes the window
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the "New From Image" button was clicked
                if button_rect.collidepoint(event.pos):
                # Call the newFromImage() function
                   Modules.FotoForge.newFromImage(layer)
            # Check if the "Create Layer" button was clicked
                elif button_rect_layer.collidepoint(event.pos):
                # Call the createLayer() function
                  layer.createLayer()

            # elif event.type == pygame.KEYDOWN:
            #   # Check if the top layer exists
            #   if layer.image:
            #      if event.key == pygame.K_o:
            #     # Prompt the user to enter an opacity percentage
            #         alpha_percentage = int(input("Enter an opacity percentage: "))
           
            #       # Adjust the opacity of the top layer
            #         layer.adjustOpacity(alpha_percentage)
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    if event.ui_element == opacity_textbox:
                        alpha_percentage = int(opacity_textbox.get_text())
                        layer.adjustOpacity(alpha_percentage)

            manager.process_events(event)
    
           
           
                 
        # Update the screen
        manager.update(pygame.time.get_ticks())
        manager.draw_ui(screen)
        pygame.display.update()




if __name__ == "__main__":
    main()
    exit()