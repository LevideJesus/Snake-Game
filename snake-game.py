import pygame
from pygame.locals import *

WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600

pygame.init() #system already to use the window
window = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))

while True: # to keep the window opens.
  window.fill((68,189,50))

  for event in pygame.event.get(): # here it´s to close the window and, importing the library for.
      if event.type == QUIT:
         pygame.quit()
         quit()