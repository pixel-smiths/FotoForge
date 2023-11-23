import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pygame
import io
from PIL import Image
from tkinter import Tk
from PIL import ImageGrab
import pygame_gui



# test_FotoForge.py
# Define a dictionary to store the visibility status of each image
# image_visibility = {}
   


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

        image = pygame.image.fromstring(image_str, image_size, imageClipboard.mode)
        image_rect = image.get_rect()
        surface.blit(image, image_rect)

    except TypeError:
        text = Tk().clipboard_get()
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (surface.get_width() / 2, surface.get_height() / 2)
        surface.blit(text_surface, text_rect)
    # except TCLError:
    #     print("Clipboard is empty")

    pygame.display.update()

#--------------------------------------------------------------
# test_newFromImage.py

def newFromImage(layer, image_names, image_name_labels, manager):
    pygame.display.set_caption("Select an Image")
    Tk().withdraw()
    filename = askopenfilename()

    # Add a placeholder name to the image_names list
    image_names.append('placeholder')
    
    # Calculate the position of the new UILabel
    label_top = 100 + len(image_name_labels) * 20  # 20px height for each label
    # Create a new UILabel for the image name
    image_name_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, label_top), (780, 20)), text=os.path.basename(filename), manager=manager)
    # Add the UILabel to the list
    image_name_labels.append(image_name_label)

    # Add the actual image name to the image_names list
    image_names.append(os.path.basename(filename))

    # Set the initial visibility of the new image to True
    # image_visibility[os.path.basename(filename)] = True

    



    layer.image = pygame.image.load(filename)
    layer.image = pygame.transform.scale(layer.image, (layer.surface.get_width() - 50, layer.surface.get_height() - 50))
    layer.rect = layer.image.get_rect()
    layer.rect.center = (layer.surface.get_width() / 2, layer.surface.get_height() / 2)

    pygame.display.set_caption(os.path.basename(filename))
    pygame.display.update()

    layer.surface.blit(layer.image, layer.rect)
    pygame.display.update()