import tkinter as tk

class Tool:
    def __init__(self, name, icon):
        self.name = name
        self.icon = icon
        self.canvas = None
        self.active = False

    def draw(self):
        # Implement drawing logic using canvas
        pass

class PenTool(Tool):
    def __init__(self, name, icon):
        super().__init__(name, icon)
        self.color = "#000000"  # black color
        self.width = 4
        self.last_mouse = None

    def set_color(self, color):
        self.color = color

    def perform(self, event):
        if self.last_mouse:
            x1, y1 = self.last_mouse
            x2, y2 = event.x, event.y
            self.canvas.create_line(x1, y1, x2, y2, fill=self.color, width=self.width, capstyle=tk.ROUND, smooth=tk.TRUE)
        self.last_mouse = (event.x, event.y)

    def draw(self):
        self.canvas.bind("<B1-Motion>", self.perform)
        self.canvas.bind("<ButtonRelease-1>", lambda e: setattr(self, 'last_mouse', None))
        # Additional setup for the pen tool, if needed

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