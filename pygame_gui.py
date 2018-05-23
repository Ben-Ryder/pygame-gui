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


class image:
    def __init__(self,image_ref):
        self.image = pygame.image.load(image_ref).convert_alpha()
        self.rect = self.image.get_rect()

    def draw(self,display,x,y):
        display.blit(self.image,[x,y])


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


class checkbox:
    def __init__(self,rest_image,hover_image,active_image,active_hover_image):
        self.rest_image = image(rest_image)
        self.hover_image = image(hover_image)
        self.active_image = image(active_image)
        self.active_hover_image = image(active_hover_image)
        self.rect = self.rest_image.image.get_rect()
        self.active = False

    def mouse_over(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def check_clicked(self):
        if self.mouse_over():
            self.active = not self.active
            return True
        return False
    
    def draw(self,display,x,y):
        self.rect[0],self.rect[1] = x,y
        if self.mouse_over():
            if self.active:
                self.active_hover_image.draw(display,x,y)
            else:
                self.hover_image.draw(display,x,y)
        else:
            if self.active:
                self.active_image.draw(display,x,y)
            else:
                self.rest_image.draw(display,x,y)


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
