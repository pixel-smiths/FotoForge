import pygame
pygame.init()

class Toolbar:
    def __init__(self):
        self.tools = []
        # create rectangle for toolbar
        # toolbar is 80px tall and at the bottom of the screen
        self.left = 0
        self.top = pygame.display.get_surface().get_height() - 80
        self.width = pygame.display.get_surface().get_width()
        self.height = 80
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        # create style attributes
        self.color = (40, 40, 40)
        self.margin = 8
        self.button_width = 64
    
    def add_tool(self, tool):
        # add tool to toolbar
        self.tools.append(tool)
        # set tool's index
        tool.index = len(self.tools) - 1
        # set tool's position
        tool.left = tool.index * self.button_width + (tool.index + 1) * self.margin
        tool.top = self.top + self.margin
        tool.rect = pygame.Rect(tool.left, tool.top, self.button_width, self.button_width)
    
    def draw(self, surface):
        # draw toolbar
        pygame.draw.rect(surface, self.color, self.rect)
        # draw tools
        for tool in self.tools:
            tool.draw(surface)
        
    def get_tool(self, pos):
        # get tool at position
        for tool in self.tools:
            if tool.rect.collidepoint(pos):
                return tool
        return None