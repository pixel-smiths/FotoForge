import pygame

pygame.font.init()

# ****Can change
# setting background color
background_color = (234, 212, 252)
# setting the toolbar color
toolbarRec_color = (70, 106, 242)
# setting color for the right rectangle which will hold the color palette and Layers
colorRec_color = (164, 205, 69)

# setting dimensions of the display
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption('FotoForge')
screen.fill(background_color)

# importing the Logo
# ****Can change
image = pygame.image.load('Log.png')
# using x and y to scale the logo size
x = 310
y = 135

# Adding buttons
button_height = 30
button_width = 120 - 20
button_margin = 10

# Position of the buttons, will be vertical
button_positions = [
    (25, 80),
    (25, 130),
    (25, 210),
]

# Creating labels for the buttons
# *****for text tool and draw toll we will have icons, this is just to show what they are
button_labels = [
    "Open Image+",
    "Text Tool",
    "Draw Tool",
]

# Button colors
button_color = (255, 255, 255)

# Buttons
buttons = [pygame.Rect(pos, (button_width, button_height)) for pos in button_positions]

# Slider variables
slider_width = 100
slider_height = 5  # Adjusted the thickness of the slider
slider_color = (100, 100, 100)
slider_value = 50  # Initial value for the slider (adjust as needed)
slider_visible_text = False  # Initial visibility state for Text Tool slider
slider_visible_draw = False  # Initial visibility state for Draw Tool slider
slider_dragging = False  # Initial dragging state

# Font for slider labels
font = pygame.font.SysFont("Arial", 12)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, button in enumerate(buttons):
                if button.collidepoint(event.pos):
                    if button_labels[i] == "Text Tool":
                        # Toggle the visibility of the Text Tool slider when "Text Tool" button is clicked
                        slider_visible_text = not slider_visible_text
                        slider_visible_draw = False  # Hide Draw Tool slider when Text Tool is clicked
                        # Check if the mouse is over the Text Tool slider and start dragging
                        slider_rect_text = pygame.Rect(button.x, button.bottom + 12, slider_width, slider_height)
                        slider_dragging = slider_rect_text.collidepoint(event.pos)
                    elif button_labels[i] == "Draw Tool":
                        # Toggle the visibility of the Draw Tool slider when "Draw Tool" button is clicked
                        slider_visible_draw = not slider_visible_draw
                        slider_visible_text = False  # Hide Text Tool slider when Draw Tool is clicked
                        # Check if the mouse is over the Draw Tool slider and start dragging
                        slider_rect_draw = pygame.Rect(button.x, button.bottom + 12, slider_width, slider_height)
                        slider_dragging = slider_rect_draw.collidepoint(event.pos)
                    elif button_labels[i] == "Open Image+":
                        # Perform "Open Image" functionality
                        print(f"Perform 'Open Image' functionality")

        elif event.type == pygame.MOUSEMOTION:
            if slider_dragging:
                # Update slider_value based on mouse movement
                slider_value = max(0, min((event.pos[0] - button.x) / slider_width * 100, 100))

        elif event.type == pygame.MOUSEBUTTONUP:
            slider_dragging = False

    # Create a new image which is the scaled version
    # "scale" takes as parameters (original image, (x,y))
    newLogo = pygame.transform.scale(image, (x, y))
    # Setting coordinates of logo
    screen.blit(newLogo, (280, 30))

    # Setting toolbar dimensions, color, and drawing the toolbar
    toolbarRec_width = 150
    toolbar_rect = pygame.Rect(0, 0, toolbarRec_width, 700)
    pygame.draw.rect(screen, toolbarRec_color, toolbar_rect)

    # Text in the toolbar
    # Initializing font
    font_toolbar = pygame.font.SysFont("Comic Sans", 25, bold=True)
    text_toolbar = font_toolbar.render('ToolBar', True, (255, 255, 255))
    text_rect_toolbar = text_toolbar.get_rect(topleft=(30, 2))
    screen.blit(text_toolbar, text_rect_toolbar)

    # Drawing all three buttons
    for i, button in enumerate(buttons):
        pygame.draw.rect(screen, button_color, button)
        font_button = pygame.font.SysFont("Comic Sans", 15, bold=False)
        text_button = font_button.render(button_labels[i], True, (0, 0, 0))
        text_rect_button = text_button.get_rect(center=button.center)
        screen.blit(text_button, text_rect_button)

        # Draw the slider for Text Tool if it's visible and Text Tool button is clicked
        if slider_visible_text and button_labels[i] == "Text Tool":
            slider_x = button.x  # Adjust the slider position based on the "Text Tool" button
            slider_y = button.bottom + 12  # Adjust the vertical position
            pygame.draw.rect(screen, slider_color, (slider_x, slider_y, slider_width, slider_height))

            # Draw labels for min, medium, and max values on the slider below the slider
            label_min = font.render("10", True, (0, 0, 0))
            label_med = font.render("50", True, (0, 0, 0))
            label_max = font.render("100", True, (0, 0, 0))

            label_rect_min = label_min.get_rect(center=(slider_x + 15, slider_y + slider_height + 15))
            label_rect_med = label_med.get_rect(center=(slider_x + slider_width // 2, slider_y + slider_height + 15))
            label_rect_max = label_max.get_rect(center=(slider_x + slider_width - 15, slider_y + slider_height + 15))

            screen.blit(label_min, label_rect_min)
            screen.blit(label_med, label_rect_med)
            screen.blit(label_max, label_rect_max)

            # Draw the slider thumb
            thumb_x = int(slider_value * slider_width / 100)
            pygame.draw.circle(screen, (255, 255, 255), (slider_x + thumb_x, slider_y + slider_height // 2), 10)

        # Draw the slider for Draw Tool if it's visible and Draw Tool button is clicked
        elif slider_visible_draw and button_labels[i] == "Draw Tool":
            slider_x = button.x  # Adjust the slider position based on the "Draw Tool" button
            slider_y = button.bottom + 12  # Adjust the vertical position
            pygame.draw.rect(screen, slider_color, (slider_x, slider_y, slider_width, slider_height))

            # Draw labels for min, medium, and max values on the slider below the slider
            label_min = font.render("10", True, (0, 0, 0))
            label_med = font.render("50", True, (0, 0, 0))
            label_max = font.render("100", True, (0, 0, 0))

            label_rect_min = label_min.get_rect(center=(slider_x + 15, slider_y + slider_height + 15))
            label_rect_med = label_med.get_rect(center=(slider_x + slider_width // 2, slider_y + slider_height + 15))
            label_rect_max = label_max.get_rect(center=(slider_x + slider_width - 15, slider_y + slider_height + 15))

            screen.blit(label_min, label_rect_min)
            screen.blit(label_med, label_rect_med)
            screen.blit(label_max, label_rect_max)

            # Draw the slider thumb
            thumb_x = int(slider_value * slider_width / 100)
            pygame.draw.circle(screen, (255, 255, 255), (slider_x + thumb_x, slider_y + slider_height // 2), 10)

    # Draw a white rectangle in the middle of the window
    middle_rect_width = 500
    middle_rect_height = 450
    middle_rect_color = (255, 255, 255)
    middle_rect = pygame.Rect((screen.get_width() - middle_rect_width) // 2 - 25, (screen.get_height() - middle_rect_height) // 2 + 50, middle_rect_width, middle_rect_height)
    pygame.draw.rect(screen, middle_rect_color, middle_rect)

    # Setting dimensions of the right rectangle that will hold the color palette and layers
    colorRec_width = 200  # Adjusted the width
    color_rect = pygame.Rect(screen.get_width() - colorRec_width, 0, colorRec_width, 700)  # Adjusted the position and width
    pygame.draw.rect(screen, colorRec_color, color_rect)

    pygame.display.update()

pygame.quit()
