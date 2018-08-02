# Ben-Ryder 2018

import pygame
import pygame_gui.image


class Cursor:
    def __init__(self, imageref):
        pygame.mouse.set_visible(False)
        self.image = pygame_gui.Image(imageref)
        
    def draw(self, surface):
        self.image.draw(surface, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
