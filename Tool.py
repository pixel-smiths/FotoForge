import pygame
pygame.init()

class Tool:
    def __init__(self, name, icon):
        self.name = name
        self.icon = icon
        self.left = 0
        self.top = 0
        # add attributes for rectangle and index (see Toolbar.py)
        self.rect = None
        self.index = None
    
    def draw(self, surface):
        # draw tool
        surface.blit(self.icon, self.rect)

class PenTool(Tool):
    def __init__(self, name, icon):
        super().__init__(name, icon)
        self.start = None
        self.end = None
        self.color = (0, 0, 0)
        self.width = 4
        self.draw_size = 1
        self.last_mouse = (0, 0)
        self.active = True
    
    def set_draw_size(self, size):
        self.draw_size = size

    def perform(self, layer, mouse, color):
        lmx, lmy = self.last_mouse
        mx, my = mouse
        num_circles = int(((mx-lmx)**2 + (my-lmy)**2)**0.5)

        circles = []
        for i in range(num_circles):
            x = mx + i*(lmx-mx)/num_circles
            y = my + i*(lmy-my)/num_circles
            pygame.draw.circle(layer, color, (int(x), int(y)), self.draw_size/2)
            circles.append((int(x), int(y)))
        self.last_mouse = mouse
        return circles

class FillTool(Tool):
    def __init__(self, name, icon):
        super().__init__(name, icon)
        self.active = False
    
    def perform(self, layer, mouse, color=(255,255,255)):
        x, y = mouse

        initial_color = layer.get_at((x, y))
        if initial_color == color:
            return

        stack = [(x, y)]

        while stack:
            x, y = stack.pop()

            if layer.get_at((x, y)) == initial_color:
                layer.set_at((x, y), color)

                if x > 0:
                    stack.append((x - 1, y))
                if x < layer.get_width() - 1:
                    stack.append((x + 1, y))
                if y > 0:
                    stack.append((x, y - 1))
                if y < layer.get_height() - 1:
                    stack.append((x, y + 1))

        pygame.display.update()

_='''pseudocode for active vs passive tools

mouse_clicked = False
main loop:
    if (left mouse button clicked) and not mouse_clicked:
        if tool.active = False:
            mouse_clicked = True
            # do action once even if mouse button is held down
        tool.perform(layer, mouse, color)

    if (left mouse button let go):
        mouse_clicked = False

if the tool is passive and the mouse is clicked, the tool's function 
is performed exacly once. if the tool is active and the mouse is 
clicked and held, the tool's function is performed for as long as 
the mouse button is held down.
'''