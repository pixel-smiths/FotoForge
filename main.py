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
    layers=[]


   

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


        # Define a list to store the image names
    image_name_labels = []

    

# # Create a UILabel to display the image names
    first_image_name_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 100), (780, 490)), text='', manager=manager)

    # Add the UILabel to the list
    image_name_labels.append(first_image_name_label)

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

# Define image_names and image_names_label before the game loop
    image_names = []
    image_names_label = []

    # # Define a dictionary to store the visibility status of each image
    # image_visibility = {}



# Create a clock object
    clock = pygame.time.Clock()


    # Run the game loop
    while True:
        # Handle events
        # Calculate time_delta
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game if the user closes the window
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the "New From Image" button was clicked
                if button_rect.collidepoint(event.pos):
                # Call the newFromImage() function
                   Modules.FotoForge.newFromImage(layer,image_names, image_name_labels, manager)
            # Check if the "Create Layer" button was clicked
                elif button_rect_layer.collidepoint(event.pos):
                # Call the createLayer() function
                  new_layer = Layer(screen)
                  new_layer.createLayer(image_names, manager)
                  layers.append(new_layer)
                

            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                # Move the top layer
                 if layers:
                    top_layer = layers[-1]
                    if event.key == pygame.K_UP:
                       top_layer.rect.y -= 5  # move layer up
                    elif event.key == pygame.K_DOWN:
                        top_layer.rect.y += 5  # move layer down
                    elif event.key == pygame.K_LEFT:
                        top_layer.rect.x -= 5  # move layer left
                    elif event.key == pygame.K_RIGHT:
                         top_layer.rect.x += 5  # move layer right
            # Redraw the layer at its new position
                    screen.fill((0, 0, 0))  # clear the surface
                    for layer in layers:
                        screen.blit(layer.image, layer.rect)  # draw the image
                    pygame.display.update()  # update the display
                
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    if event.ui_element == opacity_textbox:
                       alpha_percentage = int(opacity_textbox.get_text())
                       layer.adjustOpacity(alpha_percentage)

          
            # elif event.type == pygame.USEREVENT:
            #     if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            #         if event.ui_element == opacity_textbox:
            #             alpha_percentage = int(opacity_textbox.get_text())
            #             layer.adjustOpacity(alpha_percentage)

            # elif event.type == pygame.USEREVENT:
            #      if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            # # Toggle the visibility of the corresponding image
            #        image_name = event.ui_element.text
            #        image_visibility[image_name] = not image_visibility[image_name]

            # Draw images
        # for image_name in image_names:
        #    if image_visibility[image_name]:

            manager.process_events(event)
    
           
           
                 
        # Update the screen
        manager.update(pygame.time.get_ticks())
        manager.draw_ui(screen)

        


    #     # Update the chart manager
    #     chart_manager.update(time_delta)

    # # Draw the chart manager
    #     chart_manager.draw_ui(chart_screen)
        pygame.display.update()

       




if __name__ == "__main__":
    main()
    exit()