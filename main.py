import pygame
import FotoForge
from Toolbar import Toolbar
from Tool import *
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
    pen_tool = PenTool("Pen Tool", pygame.image.load(os.path.join("assets", "blue_tool.png")))
    fill_tool = FillTool("Fill Tool", pygame.image.load(os.path.join("assets", "blue_tool.png")))
    toolbar.add_tool(pen_tool)
    toolbar.add_tool(fill_tool)

    active_tool = toolbar.tools[0]
    active_color = (0, 0, 0)
    passive_flag = False
    tool_flag = False
    mouse_x, mouse_y = 0, 0

    # Run the game loop
    while True:
        # Handle events
        last_mouse_x, last_mouse_y = mouse_x, mouse_y
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game if the user closes the window
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the button was clicked
                for tool in toolbar.tools:
                    if tool.rect.collidepoint(event.pos):
                        print("Clicked", tool.name)
                        active_tool = tool
                
                if screen.get_rect().collidepoint(event.pos):
                    tool_flag = True

                if button_rect.collidepoint(event.pos):
                    # Call the openFromImage() function
                    FotoForge.newFromImage(screen)
            elif event.type == pygame.MOUSEBUTTONUP:
                passive_flag = False
                tool_flag = False
            #if the keypress is ctrl+v, paste the clipboard
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    FotoForge.PasteClipboard(screen)
        
        # Perform the tool's action
        if tool_flag:
            print("Tool engaged")
            if active_tool.active:
                ret = active_tool.perform(screen, (mouse_x, mouse_y), active_color, (last_mouse_x, last_mouse_y))
                if active_tool.name == "Pen Tool":
                    for circle in ret:
                        pygame.draw.circle(screen, active_color, circle, active_tool.width)
            elif not passive_flag:
                passive_flag = True
                active_tool.perform(screen, (mouse_x, mouse_y), active_color)

        # draw toolbar and tools
        toolbar.draw(screen)
        # Update the screen
        pygame.display.update()
if __name__ == "__main__":
    main()
    exit()