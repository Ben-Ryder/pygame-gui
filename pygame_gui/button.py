import pygame
from pygame_gui.image import *

class button:
    def __init__(self,rest_image,hover_image):
        self.rest_image = image(rest_image)
        self.hover_image = image(hover_image)
        self.rect = self.rest_image.image.get_rect()
        self.function = None

    def set_function(self,function):
        self.function = function

    def mouse_over(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def check_clicked(self):
        if self.mouse_over():
            if self.function != None:
                self.function()
            return True
        return False
    
    def draw(self,display,x,y):
        self.rect[0],self.rect[1] = x,y
        if self.mouse_over():
            self.hover_image.draw(display,x,y)
        else:
            self.rest_image.draw(display,x,y)
