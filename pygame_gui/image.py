# Ben-Ryder 2018

import pygame


class Image:
    def __init__(self, image_ref):
        self.image = pygame.image.load(image_ref).convert_alpha()
        self.rect = self.image.get_rect()

    def draw(self, display, x, y):
        display.blit(self.image, [x, y])
