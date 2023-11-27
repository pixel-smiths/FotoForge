import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageTk
from PIL import ImageGrab

import os
import tempfile

class Layer:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

class ImageLayer(Layer):
    def __init__(self, image_or_path):
        if isinstance(image_or_path, str):
            self.image = Image.open(image_or_path)
        else:
            self.image = image_or_path
        
        self.photo_image = ImageTk.PhotoImage(self.image)
        super().__init__(self.image.width, self.image.height)

class TextLayer(Layer):
    def __init__(self, text, font, color):
        self.text = text
        self.font = font
        self.color = color
        super().__init__(0, 0)
    
    def set_text(self, text):
        self.text = text

    def perform(self, event):
        if self.active:
            x, y = event.x, event.y
            self.canvas.create_text(x, y, text=self.text, fill=self.text_color, anchor=tk.NW)

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.layers = []
    
    def layer_from_filename(self, filename):
        if filename is not None:
            layer = ImageLayer(filename)
            self.layers.append(layer)
            self.photo_images.append(layer.photo_image)
            self.canvas.create_image(layer.x, layer.y, image=layer.photo_image, anchor=tk.NW)
            self.root.update()
        else:
            raise ValueError("Filename cannot be None")

    def add_layer(self, layer):
        self.layers.append(layer)

    def remove_layer(self, layer):
        self.layers.remove(layer)

    def perform(self, event):
        for layer in self.layers:
            layer.perform(event)

class Interface:
    def __init__(self):
        self.layers = [] # C
        self.photo_images = [] # C
        self.current_layer = None # I
        self.buttons = [] # I
        self.count = 0

        #I
        self.root = tk.Tk()
        self.root.title("FotoForge")
        self.root.geometry("900x600")

        self.root.iconbitmap("assets/Log.ico")

        self.button_frame = tk.Frame(self.root, bg="lightblue")
        self.button_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.create_button = tk.Button(self.button_frame, text="Create Layer", command=self.create_layer)
        self.create_button.pack()

        self.export_button = tk.Button(self.button_frame, text="Export", command=self.export_image)
        self.export_button.pack(side=tk.BOTTOM)

        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.drag_image)

        self.root.bind_all("<Control-v>", lambda event: self.PasteClipboard())

    def export_image(self): #I
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            new_image = Image.new('RGBA', (canvas_width, canvas_height), "white")
            for layer in self.layers:
                layer_image = layer.image.convert("RGBA")
                new_image = Image.alpha_composite(new_image, layer_image)
            new_image.save(file_path)

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.layer_from_filename(file_path)
            
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
    
    def create_layer(self): #I
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            layer = ImageLayer(file_path)
            self.layers.append(layer)
            self.photo_images.append(layer.photo_image)
            self.canvas.create_image(layer.x, layer.y, image=layer.photo_image, anchor=tk.NW)
            self.root.update()

            layer_index = self.count
            layer_button = tk.Button(self.button_frame, text="Layer " + str(layer_index+1), command=lambda: self.select_layer(layer_index))
            layer_button.pack()
            self.count += 1

    def PasteClipboard(self):
        print("Paste Clipboard")
        try:
            imageClipboard = ImageGrab.grabclipboard()
            try:
                image_str = imageClipboard.tobytes("raw", imageClipboard.mode)
            except AttributeError:
                imageClipboard = Image.open(imageClipboard[0])
                image_str = imageClipboard.tobytes("raw", imageClipboard.mode)
            image_size = imageClipboard.size
            temp_dir = tempfile.gettempdir()
            temp_file = os.path.join(temp_dir, 'clipboard_image.png')
            imageClipboard.save(temp_file)
            print(f"Saved clipboard image to {temp_file}")
            self.layer_from_filename(temp_file)
        except TypeError:
            text = self.canvas.clipboard_get()
            print(f"Clipboard text: {text}")
            self.layer_from_filename(temp_file)

    def select_layer(self, index): #I
        if index < len(self.layers):
            print("Button pressed! Index:", index)
            opacity = tk.simpledialog.askfloat("Opacity", "Enter opacity (1 - 100):", minvalue=1.0, maxvalue=100.0)
            if opacity is not None:
                self.adjust_opacity(index, opacity)
        else:
            print("Invalid layer index:", index)

    def adjust_opacity(self, index, opacity): #C
        layer = self.layers[index]
        if layer.image.mode != 'RGBA':
            layer.image = layer.image.convert('RGBA')
        alpha = Image.new('L', layer.image.size, int(opacity * 255 / 100))
        layer.image.putalpha(alpha)
        layer.photo_image = ImageTk.PhotoImage(layer.image)  # Create a new PhotoImage object
        self.canvas.delete("all")
        for layer in self.layers:
            self.canvas.create_image(layer.x, layer.y, image=layer.photo_image, anchor="nw")

    def run(self): #I
        self.root.mainloop()

window = Interface()
window.run() 