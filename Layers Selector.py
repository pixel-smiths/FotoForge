
import pygame_menu
import pygame
import pygame_gui

pygame.init()
count = 1
window_width = 150
window_height = 300
scrollable_height = 250
scroll_speed = 5

window_surface = pygame.display.set_mode((window_width, window_height))
manager = pygame_gui.UIManager((window_width, window_height))

buttons = []
button_y = 0

button_text = "Create Layer"
button_text_color = "grey"

def create_button(button_y):
    button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, button_y), (100, 50)),
                                          text="Layer " + str(count),
                                          manager=manager)
    buttons.append(button)

font = pygame.font.Font(None, 15)
start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, button_y), (window_width, 50)),
                                            text="Create Layer",
                                            manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    button_y += 50
                    create_button(button_y)
                    count += 1
                elif event.ui_element in buttons:
                    button_index = buttons.index(event.ui_element)
                    print("Button pressed! Index:", button_index)

        manager.process_events(event)

    manager.update(time_delta)

    if count > 4:
        scrollable_surface = pygame.Surface((window_width, scrollable_height))
        scrollable_surface.fill(pygame.Color("white"))
        scrollable_surface.blit(window_surface, (0, -scroll_speed))
        window_surface.blit(scrollable_surface, (0, 0))
        scrollable_height += 50

    else:
        window_surface.fill(pygame.Color("white"))

    manager.draw_ui(window_surface)

    pygame.display.update()

pygame.quit()


