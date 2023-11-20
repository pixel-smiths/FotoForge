#test_fotoForge.py
from pytest import raises
from unittest.mock import patch
from FotoForge import *
from main import *
import pygame

def test_newFromImage():
    with raises(SystemExit):
        pygame.font.init()
        screen = main()
        filename = "C:\\Users\\niels\\OneDrive\\Documents\\github\\Fotoforge\\FotoForge\\pytestMain\\.env\\test_data\\test.png"
        # Call the function
        Control_image = pygame.image.load(filename)
        image = newFromImage(surface=screen)
        # Check the result
        for x in range(Control_image.get_width()):
            for y in range(Control_image.get_height()):
                assert Control_image.get_at((x, y)) == image.get_at((x, y))
