import pygame
from constantes import *
from auxiliar import Auxiliar

class Loot:
    
    def __init__(self,x,y,type=0):
        self.red_potion= Auxiliar.getSurfaceFromSeparateFiles("my_images/others/potions_2/red({0}).png",1,3,flip=False,scale=1.9)
        self.blue_potion= Auxiliar.getSurfaceFromSeparateFiles("my_images/others/potions_2/blue({0}).png",1,3,flip=False,scale=1.9)
        self.animation = self.blue_potion
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ground_collition_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)
        self.frame_rate_ms = 90
        
    def update(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0


    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)

        screen.blit(self.image,self.rect)

        if(DEBUG):
            pygame.draw.rect(screen,GREEN,self.ground_collition_rect)

