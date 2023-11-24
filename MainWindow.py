import pygame
pygame.font.init()


#****Can change
#setting background color
background_color = (234, 212, 252)
#setting the toolbar color
toolbarRec_color = (70,106,242)
#setting color for the right rectangle which will hold the color palette and Layers
colorRec_color = (164, 205, 69)


#setting dimensions of the display
screen = pygame.display.set_mode((900,700))
pygame.display.set_caption('FotoForge')
screen.fill(background_color)

#importing the Logo
#****Can change
image = pygame.image.load('Log.png')
#using x and y to scale the logo size 
x = 300
y = 110



#updating display
pygame.display.flip()
running = True
while running:
    #create a new image which is the scaled version 
    #"scale" takes as parameters (original image, (x,y))
    newLogo = pygame.transform.scale(image, (x,y))
    #setting coordinates of logo
    screen.blit(newLogo, (315,40))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #setting toolbar dimensions, color and drawing the toolbar
    toolbarRec_width = 150
    toolbar_rect = pygame.Rect(0, 0, toolbarRec_width, 700)
    pygame.draw.rect(screen, toolbarRec_color, toolbar_rect)


    #Text in the toolbar
    #Initializing font
    font = pygame.font.SysFont("Comic Sans", 25, bold=True)
    text = font.render('ToolBar', True, (255,255,255))
    text_rect = text.get_rect(topleft=(30,20))
    screen.blit(text, text_rect)



    #setting dimensions of the right rectangle thta will hold the color palette and layers
    colorRec_width = 150
    color_rect =  pygame.Rect(750, 0, toolbarRec_width, 700)
    pygame.draw.rect(screen, colorRec_color, color_rect)
    pygame.display.update()