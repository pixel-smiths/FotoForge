#test_fotoForge.py
from pytest import raises
from Modules.FotoForge import *
from main import *
import pygame
from unittest.mock import patch

def test_PasteClipboard():
    # Test if PasteClipboard can successfully take an image from the user's clipboard
    with raises(SystemExit):
        # Set up
        pygame.font.init()
        screen = main()
        # Load an image into the clipboard
        image = pygame.image.load('C:\\Users\\niels\\OneDrive\\Documents\\github\\Fotoforge\\FotoForge\\pytestMain\\.env\\test_data\\test.png')
        image_string = pygame.image.tostring(image, 'RGBA')
        pygame.scrap.put(pygame.SCRAP_CLIPBOARD, 'image/png', image_string)
        # Call the function that handles the ctrl-v event
        with patch('builtins.input', return_value='C:\\Users\\niels\\OneDrive\\Documents\\github\\Fotoforge\\FotoForge\\pytestMain\\.env\\test_data\\test.png'):
            PasteClipboard(surface=screen)
        # Check the result
        pasted_image = pygame.scrap.get(pygame.SCRAP_CLIPBOARD)
        assert pasted_image is not None

# def test_PasteClipboard():
#     # Test if PasteClipboard can successfully take an image from the user's clipboard
#     with raises(SystemExit):
#         # Set up
#         pygame.font.init()
#         screen = main()
#         # Load an image into the clipboard
#         image = pygame.image.load('C:\\Users\\niels\\OneDrive\\Documents\\github\\Fotoforge\\FotoForge\\pytestMain\\.env\\test_data\\test.png')
#         image_string = pygame.image.tostring(image, 'RGBA')
#         pygame.scrap.put(pygame.SCRAP_CLIPBOARD, 'image/png', image_string)
#         # Call the function that handles the ctrl-v event
#         PasteClipboard(surface=screen)
#         # Check the result
#         pasted_image = pygame.scrap.get(pygame.SCRAP_CLIPBOARD)
#         assert pasted_image is not None

