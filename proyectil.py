from player import *
from constantes import *
from auxiliar import Auxiliar

class Bullet():
    
    def __init__(self,x_init,y_init,velocidad,frame_rate_ms,move_rate_ms, direction, reach, frame) -> None:
        self.bullet_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/others/proyectiles/{0}.png",1,2,flip=True,scale=2.2)
        self.bullet_l = Auxiliar.getSurfaceFromSeparateFiles("my_images/others/proyectiles/{0}.png",1,2,flip=False,scale=2.2)
        self.bullet_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/others/proyectiles_2/({0}).png",1,2,flip=False,scale=3.5)
        self.bullet_l = Auxiliar.getSurfaceFromSeparateFiles("my_images/others/proyectiles_2/({0}).png",1,2,flip=True,scale=3.5)
        self.bullet_buffed_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/others/proyectiles/{0}.png",3,2,flip=True,scale=5)
        self.bullet_buffed_l = Auxiliar.getSurfaceFromSeparateFiles("my_images/others/proyectiles/{0}.png",3,2,flip=False,scale=5)
        self.frame = frame
        self.animation = self.bullet_r
        if direction == DIRECTION_L:
            self.animation = self.bullet_l
        else:
            x_init +=20
        self.direction = direction
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.collition_rect = self.rect
        self.x_init = x_init
        self.x = x_init
        self.y = y_init
        self.reach = reach

        self.rect.x = x_init
        self.rect.y = y_init
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        
        self.move_x = velocidad
        self.move_y = 0
        
        self.is_active = True 
   
    def change_x (self,delta_x):
        if  self.direction == DIRECTION_L:
            self.x = self.x - delta_x
            self.rect.x = int(self.x)
            # self.animation = self.bullet_l
        else:
            self.x = self.x + delta_x
            self.rect.x = int(self.x)
            

    def change_y(self,delta_y):
        self.y = self.y + delta_y
        self.rect.y = int(self.y)

    def do_movement(self,delta_ms,plataform_list,enemy_list,player):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            
            self.change_x(self.move_x)
            self.change_y(self.move_y)
            # self.check_impact(plataform_list,enemy_list,player)
        

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
    
    # def check_impact(self,plataform_list,enemy_list):
    #     for aux_enemy in enemy_list:
    #         if(self.is_active and self.rect.colliderect(aux_enemy.rect)):
    #             print("IMPACTO ENEMY")
    #             self.is_active = False

    def update(self,delta_ms,plataform_list,enemy_list,player):
        self.do_movement(delta_ms,plataform_list,enemy_list,player)
        
        self.do_animation(delta_ms) 
    def draw(self,screen):
        if(self.is_active):
            if(DEBUG):
                pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            screen.blit(self.image,self.rect)
