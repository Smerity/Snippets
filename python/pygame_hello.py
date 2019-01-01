# Inspired by https://gist.github.com/nicolasfig/3903404
# (and by inspired it really isn't modified much)
# After looking at the API I realize again that PyGame is cool but not really for me :S

import sys

import pygame
from pygame.locals import QUIT

pygame.init()

# No clue what this does ^_^
window = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption('Hello World')

#Set up the colors
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

#Set up fonts
basicFont = pygame.font.SysFont(None, 48)

#Set up the text
text = basicFont.render('HELLO WORLD', True, BLACK)
textRect = text.get_rect()
textRect.centerx = window.get_rect().centerx
textRect.centery = window.get_rect().centery

#Draw the white background onto the surface
window.fill(BLACK)

pygame.draw.polygon(window, WHITE, ((250, 0), (500, 200),(250, 400), (0, 200)))
pygame.draw.polygon(window, GREEN, ((125,100),(375,100),(375,300),(125,300)))

pygame.draw.circle(window, RED, (250,200), 125)

#Draw the text onto the surface
window.blit(text,textRect)

#Get a pixel array of the surface
pixArray = pygame.PixelArray(window)
for i in range(100):
    pixArray[int(i * 0.480)][int(i * 0.380)] = BLUE
del pixArray

#Draw the window onto the screen
pygame.display.update()

#Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
