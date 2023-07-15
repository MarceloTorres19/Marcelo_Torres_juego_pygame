import pygame,random
from constantes import *
from auxiliar import Auxiliar


class Loot:
    loot_list = []
    def __init__(self,x,y):
        self.potion_red= Auxiliar.getSurfaceFromSeparateFiles("my_images/others/potions/({0}).png",1,2,flip=False,scale=2.8)
        self.potion_blue= Auxiliar.getSurfaceFromSeparateFiles("my_images/others/potions/({0}).png",3,2,flip=False,scale=2.8)
        self.potion_yellow= Auxiliar.getSurfaceFromSeparateFiles("my_images/others/potions/({0}).png",5,2,flip=False,scale=2.8)
        self.potions_list =[self.potion_red,self.potion_blue,self.potion_yellow]
        self.items = Auxiliar.getSurfaceFromSeparateFiles("my_images/others/items/({0}).png",1,6,flip=False,scale=2.5)
        for elemento in self.items:
            elemento = [elemento]
            self.potions_list.append(elemento)
        self.numero_aleatorio = random.randint(0, len(self.potions_list)-1)
        self.animation = self.potions_list[self.numero_aleatorio]
        self.value_list =[RED_POT,BLUE_POT,YELLOW_POT,100,200,300,500,800,1000]
        self.value = self.value_list[self.numero_aleatorio]
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ground_collition_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)
        self.frame_rate_ms = 260
        self.tiempo_transcurrido_animation = 0
        self.numero_aleatorio2 = random.randint(0,2)
        if self.numero_aleatorio2 <2:
            self.loot_list.append(self) 
        
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
        
        if type(self.animation) == list:
            self.image = self.animation[self.frame]
        else:
            self.image = self.animation

        screen.blit(self.image,self.rect)

        if(DEBUG):
            pygame.draw.rect(screen,GREEN,self.ground_collition_rect)

