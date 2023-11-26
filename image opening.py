

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class Layer:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.x = 0
        self.y = 0

class ImageWindow:
    def __init__(self):
        self.layers = []

        self.root = tk.Tk()
        self.root.title("Image Window")

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.button = tk.Button(self.root, text="Open Image", command=self.open_image)
        self.button.pack()

        self.canvas.bind("<ButtonPress-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.drag_image)

        self.drag_data = None

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            layer = Layer(file_path)
            self.layers.append(layer)
            self.canvas.create_image(layer.x, layer.y, image=layer.photo_image, anchor=tk.NW)

    def start_drag(self, event):
        for index, layer in reversed(list(enumerate(self.layers))):
            if (layer.x <= event.x < layer.x + layer.image.width and
            layer.y <= event.y < layer.y + layer.image.height):
                self.current_layer = layer
            self.start_x = event.x - layer.x
            self.start_y = event.y - layer.y
            print("Image index:", index)  # Print the index of the image
            break

    def drag_image(self, event):
       if self.current_layer is not None:
            # Update the layer's position
            self.current_layer.x = event.x - self.start_x
            self.current_layer.y = event.y - self.start_y

            # Redraw the canvas
            self.canvas.delete("all")
            for layer in self.layers:
                self.canvas.create_image(layer.x, layer.y, image=layer.photo_image, anchor="nw")

    def run(self):
        self.root.mainloop()
    

if __name__ == "__main__":
    window = ImageWindow()
    window.run()
