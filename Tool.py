import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

class Tool:
    def __init__(self, name, icon_path):
        self.name = name
        self.icon_image = Image.open(icon_path)
        self.icon = ImageTk.PhotoImage(self.icon_image)
        self.rect = None
        self.index = None

    def draw(self, canvas):
        canvas.create_image(self.rect[0], self.rect[1], image=self.icon, anchor=tk.NW)

class PenTool(Tool):
    def __init__(self, name, icon_path):
        super().__init__(name, icon_path)
        self.draw_size = 1
        self.color = "black"
        self.last_mouse = (0, 0)
        self.active = True

    def set_draw_size(self, size):
        self.draw_size = size

    def perform(self, draw, mouse):
        lmx, lmy = self.last_mouse
        mx, my = mouse
        draw.line([lmx, lmy, mx, my], fill=self.color, width=self.draw_size)
        self.last_mouse = mouse

class FillTool(Tool):
    def __init__(self, name, icon_path):
        super().__init__(name, icon_path)
        self.active = False

    def perform(self, draw, mouse, image):
        x, y = mouse
        target_color = image.getpixel((x, y))
        fill_color = self.color
        if target_color == fill_color:
            return

        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            if image.getpixel((x, y)) == target_color:
                draw.point((x, y), fill=fill_color)

                if x > 0:
                    stack.append((x - 1, y))
                if x < image.width - 1:
                    stack.append((x + 1, y))
                if y > 0:
                    stack.append((x, y - 1))
                if y < image.height - 1:
                    stack.append((x, y + 1))

'''pseudocode for active vs passive tools

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