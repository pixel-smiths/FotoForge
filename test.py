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

    def perform(self, event):
        # Implement fill logic using canvas
        pass

    def draw(self):
        self.canvas.bind("<Button-1>", self.perform)
        # Additional setup for the fill tool, if needed

# Example usage:
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

pen_tool = PenTool("Pen", None)
pen_tool.canvas = canvas
pen_tool.active = True
pen_tool.draw()

fill_tool = FillTool("Fill", None)
fill_tool.canvas = canvas
fill_tool.draw()

root.mainloop()
