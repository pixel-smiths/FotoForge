
import pygame

# Initialize Pygame
pygame.init()

# Set the size of the window
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("FotoForge")

#set backgorund to white
screen.fill((255, 255, 255))

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the game if the user closes the window
            pygame.quit()
            exit()

    # Update the screen
    pygame.display.update()
