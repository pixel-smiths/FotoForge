import pygame
import FotoForge
from Toolbar import Toolbar
from Tool import Tool
import os

def main():
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

    # create toolbar
    toolbar = Toolbar()
    blue_tool = Tool("Blue", pygame.image.load(os.path.join("assets", "blue_tool.png")))
    toolbar.add_tool(blue_tool)

    # Run the game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game if the user closes the window
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the button was clicked
                if button_rect.collidepoint(event.pos):
                    # Call the openFromImage() function
                    FotoForge.newFromImage(screen)
            #if the keypress is ctrl+v, paste the clipboard
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    FotoForge.PasteClipboard(screen)
        # draw toolbar and tools
        toolbar.draw(screen)
        # Update the screen
        pygame.display.update()
if __name__ == "__main__":
    main()
    exit()