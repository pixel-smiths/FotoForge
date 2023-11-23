import pygame, os

def tipicon(screen, object):
        # Create a tiny tip icon from tip.png in assets and call it to be right next to any tool
        tip = pygame.image.load(os.path.join("assets", "tip.png"))
        tip = pygame.transform.scale(tip, (15, 15))
        # Calculate the position where the button ends
        button_end_x = object.x + object.width
        button_end_y = object.y + object.height
        # Position the tip icon next to the button
        screen.blit(tip, (button_end_x + 10, button_end_y - 20))
        return tip

def helpzone(screen, tool):
        #create a rectangle that appears that as the proper text to help you use that tool.
        if tool == 'upload': 
            advice = "Use this tool to help you upload an image from your computer."
        elif tool == 'Add Layer':
            advice = "Use this tool to add a layer to your project."
        
        # maek the rectangle of text appear below the tipicon location
        text = pygame.font.Font(None, 36)
        text_surface = text.render(advice, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (100, 100)
        screen.blit(text_surface, text_rect)