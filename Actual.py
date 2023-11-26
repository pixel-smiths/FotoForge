import tkinter as tk
import tkinter.simpledialog
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import ImageEnhance

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
       self.photo_images = []
       self.current_layer = None
       self.buttons = []
       self.count=0

       self.root = tk.Tk()
       self.root.title("Image Window")

       self.button_frame = tk.Frame(self.root)
       self.button_frame.grid(row=0, column=0, sticky="nw")

       self.create_button = tk.Button(self.button_frame, text="Create Layer", command=self.create_layer)
       self.create_button.pack()

       self.canvas = tk.Canvas(self.root, width=800, height=600)
       self.canvas.grid(row=1, column=0, sticky="nw")

       self.canvas.bind("<ButtonPress-1>", self.start_drag)
       self.canvas.bind("<B1-Motion>", self.drag_image)

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            layer = Layer(file_path)
            self.layers.append(layer)
            self.photo_images.append(layer.photo_image)
            self.canvas.create_image(layer.x, layer.y, image=layer.photo_image, anchor=tk.NW)
            self.root.update()

    def start_drag(self, event):
        canvas_x = self.canvas.canvasx(event.x)
        canvas_y = self.canvas.canvasy(event.y)

        for index, layer in reversed(list(enumerate(self.layers))):
            if (layer.x <= canvas_x < (layer.x + layer.image.size[0]) and
            layer.y <= canvas_y < (layer.y + layer.image.size[1])):
                self.current_layer = layer
                self.start_x = canvas_x - layer.x
                self.start_y = canvas_y - layer.y
                print("Image index:", index)
                break

    def drag_image(self, event):
        if self.current_layer is not None:
            canvas_x = self.canvas.canvasx(event.x)
            canvas_y = self.canvas.canvasy(event.y)

            self.current_layer.x = canvas_x - self.start_x
            self.current_layer.y = canvas_y - self.start_y

            self.canvas.delete("all")
            for layer in self.layers:
                self.canvas.create_image(layer.x, layer.y, image=layer.photo_image, anchor="nw")
        

   
    def create_layer(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            layer = Layer(file_path)
            self.layers.append(layer)
            self.photo_images.append(layer.photo_image)
            self.canvas.create_image(layer.x, layer.y, image=layer.photo_image, anchor=tk.NW)
            self.root.update()

            layer_index = self.count
            layer_button = tk.Button(self.button_frame, text="Layer " + str(layer_index+1), command=lambda: self.select_layer(layer_index))
            layer_button.pack()
            self.count += 1

   
    def select_layer(self, index):
        if index < len(self.layers):
            print("Button pressed! Index:", index)
            opacity = tk.simpledialog.askfloat("Opacity", "Enter opacity (1 - 100):", minvalue=1.0, maxvalue=100.0)
            if opacity is not None:
               self.adjust_opacity(index, opacity)
        else:
             print("Invalid layer index:", index)



 
   
    def adjust_opacity(self, index, opacity):
        layer = self.layers[index]
        if layer.image.mode != 'RGBA':
            layer.image = layer.image.convert('RGBA')
        alpha = Image.new('L', layer.image.size, int(opacity * 255 / 100))
        layer.image.putalpha(alpha)
        layer.photo_image = ImageTk.PhotoImage(layer.image)  # Create a new PhotoImage object
        self.canvas.delete("all")
        for layer in self.layers:
            self.canvas.create_image(layer.x, layer.y, image=layer.photo_image, anchor="nw")

    def run(self):
        self.root.mainloop()
window = ImageWindow()
window.run()