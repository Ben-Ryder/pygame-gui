# cursor object
import pygame
class cursor:
    def __init__(self, imageRef):
        pygame.mouse.set_visible(False)
        self.image = pygame.image.load(imageRef).convert_alpha()
        
    def draw(self,surface):
        surface.blit(self.image,pygame.mouse.get_pos())
