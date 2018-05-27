# Ben-Ryder 2018

import pygame
from pygame_gui.text import *
from pygame_gui.image import *

class entry:
    def __init__(self,background_image,
                 initial_text,text_size,text_colour,text_font = None,text_padX = 0,text_padY = 0,sticky = False):
        self.background_image = image(background_image)
        self.rect = self.background_image.image.get_rect()
        self.text = text(initial_text,text_size,text_colour,text_font)
        self.text_padX = text_padX
        self.text_padY = text_padY
        self.active = False
        self.sticky = sticky

    def get_text(self):
        return self.text.text

    def mouse_over(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def check_clicked(self):
        if self.mouse_over():
            self.active = True
            if self.sticky:
                self.text.change_text("")
        else:
            self.active = False

    def handle_event(self,event):
        if self.active:
            key_uni = event.unicode
            key_str = pygame.key.name(event.key)

            if key_str == "backspace":
                self.text.change_text(self.text.text[:-1])
            elif key_str == "space" and self.text.graphic_text.get_width() < self.rect[2]- self.text_padX*3:
                self.text.change_text(self.text.text + " ")
            else:
                if self.text.graphic_text.get_width() < self.rect[2]-self.text_padX*3 and key_uni.isprintable():
                    if pygame.key.get_mods()& pygame.KMOD_CAPS or pygame.key.get_mods()&pygame.KMOD_SHIFT:
                        self.text.change_text(self.text.text+key_uni.upper())
                    else:
                        self.text.change_text(self.text.text+key_uni.lower())

    def draw(self,display,x,y):
        self.rect[0],self.rect[1] = x,y
        self.background_image.draw(display,x,y)
        self.text.draw(display,x+self.text_padX,y+self.text_padY)
