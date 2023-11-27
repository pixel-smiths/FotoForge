import tkinter as tk
from tkinter import simpledialog
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

class PenTool:
    def __init__(self, canvas, toolbar, layers):
        self.canvas = canvas
        self.toolbar = toolbar
        self.layers = layers
        self.old_x = None
        self.old_y = None

    def on_button_press(self, event):
        if self.toolbar.current_tool == self:
            self.old_x = event.x
            self.old_y = event.y

    def on_motion(self, event):
        if self.toolbar.current_tool == self:
            if self.old_x and self.old_y and self.layers:
                layer = self.layers[-1]
                draw = ImageDraw.Draw(layer.image)
                draw.line((self.old_x, self.old_y, event.x, event.y), fill=self.toolbar.line_color, width=self.toolbar.line_width)
                self.old_x = event.x
                self.old_y = event.y
                # Convert the layer's image to a PhotoImage and update the canvas
                photo_image = ImageTk.PhotoImage(layer.image)
                self.canvas.create_image(0, 0, image=photo_image, anchor='nw')
                # Store a reference to the PhotoImage to prevent it from being garbage collected
                self.canvas.photo_image = photo_image

    def on_button_release(self, event):
        if self.toolbar.current_tool == self:
            self.old_x = None
            self.old_y = None
class TextBoxTool:
    def __init__(self, canvas, toolbar, layers ):
        self.canvas = canvas
        self.toolbar = toolbar
        self.layers = layers

    def on_click(self, event):
        text = simpledialog.askstring("Input", "Enter text:", parent=self.canvas)
        if text:
            self.canvas.create_text(event.x, event.y, text=text, fill="black", font=('Helvetica', '12'))
class EraserTool:
    def __init__(self, canvas, toolbar, layers):
        self.canvas = canvas
        self.toolbar = toolbar
        self.layers = layers
        self.old_x = None
        self.old_y = None

    def on_button_press(self, event):
        if self.toolbar.current_tool == self:
            self.old_x = event.x
            self.old_y = event.y

    def on_motion(self, event):
        if self.toolbar.current_tool == self:
            print("Erasing")
            if self.old_x and self.old_y and self.layers:
                layer = self.layers[-1]
                draw = ImageDraw.Draw(layer.image)
                draw.line((self.old_x, self.old_y, event.x, event.y)
                        , fill="white", width=self.toolbar.line_width)
                self.old_x = event.x
                self.old_y = event.y
                # Convert the layer's image to a PhotoImage and update the canvas
                photo_image = ImageTk.PhotoImage(layer.image)
                self.canvas.create_image(0, 0, image=photo_image, anchor='nw')
                # Store a reference to the PhotoImage to prevent it from being garbage collected
                self.canvas.photo_image = photo_image

    def on_button_release(self, event):
        if self.toolbar.current_tool == self:
            self.old_x = None
            self.old_y = None
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