import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.tix import IMAGETEXT
import pygame
from PIL import Image
from tkinter import Tk
from PIL import ImageGrab
import tkinter
from PIL import ImageTk

# test_FotoForge.py

def PasteClipboard(surface):
    print("Paste Clipboard")

    try:
        imageClipboard = ImageGrab.grabclipboard()
        try:
            image_str = imageClipboard.tobytes("raw", imageClipboard.mode)
        except AttributeError:
            imageClipboard = Image.open(imageClipboard[0])
            image_str = imageClipboard.tobytes("raw", imageClipboard.mode)
        image_size = imageClipboard.size
        image = ImageTk.PhotoImage(Image.frombytes(imageClipboard.mode, image_size, image_str))
        label = tkinter.Label(surface, image=image)
        label.image = image
        label.pack()

    except TypeError:
        text = surface.clipboard_get()
        label = tkinter.Label(surface, text=text)
        label.pack()

    #surface.update()

#--------------------------------------------------------------
# test_newFromImage.py

def newFromImage(surface):
    pygame.display.set_caption("Select an Image")
    Tk().withdraw()
    filename = askopenfilename()
    image = pygame.image.load(filename)

    image = pygame.transform.scale(image, (surface.get_width() - 50, surface.get_height() - 50))
    image_rect = image.get_rect()
    image_rect.center = (surface.get_width() / 2, surface.get_height() / 2)

    pygame.display.set_caption(os.path.basename(filename))
    pygame.display.update()

    surface.blit(image, image_rect)
    pygame.display.update()












    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            layer = Layer(file_path, canvas_width, canvas_height)
            self.layers.append(layer)
            self.photo_images.append(layer.photo_image)
            self.canvas.create_image(layer.x, layer.y, image=layer.photo_image, anchor=tk.NW)
            self.root.update()



#--------------------------------------------------------------
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