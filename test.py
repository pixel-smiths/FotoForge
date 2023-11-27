import tkinter as tk

class FillTool:
    def __init__(self, canvas):
        self.canvas = canvas
        self.active = False
        self.fill_color = "#FF0000"  # Red color (customize as needed)
        self.stack = []

    def perform(self, event):
        start_pixel = (event.x, event.y)

        # Get the color of the clicked pixel
        target_color = self.canvas.gettags(self.canvas.find_closest(event.x, event.y))

        if target_color != self.fill_color:
            self.flood_fill(start_pixel, target_color)

    def flood_fill(self, start_pixel, target_color):
        self.stack = [(start_pixel[0], start_pixel[1])]

        while self.stack:
            x, y = self.stack.pop()

            current_color = self.canvas.gettags(self.canvas.find_closest(x, y))
            print(current_color)

            if current_color == target_color:
                self.canvas.create_rectangle(x, y, x+1, y+1, fill=self.fill_color, outline=self.fill_color, tags=(self.fill_color,))
                self.stack.append((x - 1, y))
                self.stack.append((x + 1, y))
                self.stack.append((x, y - 1))
                self.stack.append((x, y + 1))

# Example usage:
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

fill_tool = FillTool(canvas)

# Bind the left mouse button to perform the fill
root.bind("<Button-1>", fill_tool.perform)

root.mainloop()