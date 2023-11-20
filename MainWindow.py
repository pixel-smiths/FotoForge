import pygame

#****Can change
#setting background color
background_color = (234, 212, 252)
#setting the toolbar color
toolbar_color = (70,106,242)

#setting dimensions of the display
screen = pygame.display.set_mode((900,700))
pygame.display.set_caption('FotoForge')
screen.fill(background_color)

#importing the Logo
#****Can change
image = pygame.image.load('assets/Log.png')
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
    toolbar_width = 200
    toolbar_rect = pygame.Rect(0, 0, toolbar_width, 700)
    pygame.draw.rect(screen, toolbar_color, toolbar_rect)
    pygame.display.update()