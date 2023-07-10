import pygame
from constantes import *
from auxiliar import Auxiliar

class Platform:
    
    def __init__(self,x,y,width,height,type=0):
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles("my_images/tiles/({0}).png",1,10,flip=False,w=width,h=height)
        
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ground_collition_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)
        

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)

        screen.blit(self.image,self.rect)

        if(DEBUG):
            pygame.draw.rect(screen,GREEN,self.ground_collition_rect)

