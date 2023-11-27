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