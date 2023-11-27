import tkinter as tk
import tkinter.simpledialog
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import ImageEnhance
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import Image, ImageTk
from PIL import ImageGrab
import os
import tempfile
import Modules.FotoForge as FotoForge


class Layer:
    def __init__(self, image_or_path, width, height):
        if isinstance(image_or_path, Image.Image):
            self.image = image_or_path
        else:
            self.image = Image.open(image_or_path)
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

class ImageWindow:
    def __init__(self):
        self.layers = []
        self.photo_images = []
        self.current_layer = None
        self.buttons = []
        self.count = 0

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

    def export_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            new_image = Image.new('RGBA', (canvas_width, canvas_height), "white")
            for layer in self.layers:
                layer_image = layer.image.convert("RGBA")
                new_image = Image.alpha_composite(new_image, layer_image)
            new_image.save(file_path)

    def layer_from_filename(self, filename):
        if filename is not None:
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            layer = Layer(filename, canvas_width, canvas_height)
            self.layers.append(layer)
            self.photo_images.append(layer.photo_image)
            self.canvas.create_image(layer.x, layer.y, image=layer.photo_image, anchor=tk.NW)
            self.root.update()
        else:
            raise ValueError("Filename cannot be None")

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
    def create_layer(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            layer = Layer(file_path, canvas_width, canvas_height)
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
            
            # Save the bytes to a temporary file
            temp_dir = tempfile.gettempdir()
            temp_file = os.path.join(temp_dir, 'clipboard_image.png')
            imageClipboard.save(temp_file)

            print(f"Saved clipboard image to {temp_file}")

            # Create a layer from the clipboard image path
            self.layer_from_filename(temp_file)

            # image = ImageTk.PhotoImage(Image.frombytes(imageClipboard.mode, image_size, image_str))
            # label = tkinter.Label(surface, image=image)
            # label.image = image
            # label.pack()
        except TypeError:
            # This must be a text clipboard
            # Get the text from the clipboard
            text = self.canvas.clipboard_get()
            print(f"Clipboard text: {text}")
            # Create a layer from the clipboard image path
            self.layer_from_filename(temp_file)

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