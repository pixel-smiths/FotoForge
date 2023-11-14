import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pygame
import io
from PIL import Image
from tkinter import Tk
from PIL import ImageGrab

def PasteClipboard(surface):
    print("Paste Clipboard")
    try:
        # Try to get an image from the clipboard using imagegrab
        imageClipboard = ImageGrab.grabclipboard()
        #convert image to pygame image
        try:
            image_str = imageClipboard.tobytes("raw", imageClipboard.mode)
        except AttributeError:
            # Clipboard contains filepath, load image from filepath
            imageClipboard = Image.open(imageClipboard[0])
            image_str = imageClipboard.tobytes("raw", imageClipboard.mode)
        image_size = imageClipboard.size
        image = pygame.image.fromstring(image_str, image_size, imageClipboard.mode)
        #if using 
        # #resize image to keep sizing right but to be 100 pixels less than the screen and centered on the screen
        # image = pygame.transform.scale(image, (surface.get_width()-50, surface.get_height()-50))
        #center image on screen
        image_rect = image.get_rect()
        # image_rect.center = (surface.get_width()/2, surface.get_height()/2)
        # Blit the loaded image onto the original Pygame surface
        surface.blit(image, image_rect)

    except TypeError:
        #upload text in clipboard to pygame
        text = Tk().clipboard_get()
        #create a font
        font = pygame.font.Font(None, 36)
        #create a surface with the text
        text_surface = font.render(text, True, (0,0,0))
        #get the rectangle of the text surface
        text_rect = text_surface.get_rect()
        #center the text on the screen
        text_rect.center = (surface.get_width()/2, surface.get_height()/2)
        # Blit the loaded image onto the original Pygame surface
        surface.blit(text_surface, text_rect)
    pygame.display.update()


def newFromImage(surface):
    # Set the caption of the Pygame window to "Select an Image"
    pygame.display.set_caption("Select an Image")

    # Open a file system dialog to select an image
    Tk().withdraw()
    filename = askopenfilename()

    # Load the selected image
    image = pygame.image.load(filename)

    #resize image to keep sizing right but to be 100 pixels less than the screen and centered on the screen
    image = pygame.transform.scale(image, (surface.get_width()-50, surface.get_height()-50))
    #center image on screen
    image_rect = image.get_rect()
    image_rect.center = (surface.get_width()/2, surface.get_height()/2)


    # Set the caption of the Pygame window to the name of the selected image
    pygame.display.set_caption(os.path.basename(filename))

    # Update the Pygame window
    pygame.display.update()

    # Blit the loaded image onto the original Pygame surface
    surface.blit(image, image_rect)

    # Update the original Pygame surface
    pygame.display.update()

 



   