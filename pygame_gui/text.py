# Ben-Ryder 2018

import pygame

class text:
    def __init__(self,text,size,colour,font = None):
        self.text = text
        self.size = size
        self.colour = colour
        self.font = font
        self._config_font()
        self._config_text()

    def _config_font(self):
        self.graphic_font = pygame.font.SysFont(self.font,self.size)

    def _config_text(self):
        self.graphic_text = self.graphic_font.render(self.text,True,self.colour)

    def change_text(self,text):
        self.text = text
        self._config_text()

    def draw(self,display,x,y):
        display.blit(self.graphic_text,[x,y])
