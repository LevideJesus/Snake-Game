import pygame
from pygame.locals import *

WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600
BLOCK = 10
PLACE_X = WINDOWS_WIDTH / 2
PLACE_Y = WINDOWS_HEIGHT / 2

pygame.init() #system already to use the window
window = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))

snake_pos = [(PLACE_X, PLACE_Y)]
snake_surface = pygame.Surface((BLOCK,BLOCK))
snake_surface.fill((53,59,72))

while True: # to keep the window opens.
  window.fill((68,189,50))

  for event in pygame.event.get(): # here it´s to close the window and, importing the library for.
      if event.type == QUIT:
         pygame.quit()
         quit()

  for place in snake_pos:
    window.blit(snake_surface,place) # blit to draw something on the screen. 

  pygame.display.update() # to update the screen 