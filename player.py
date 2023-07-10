import pygame
from constantes import *
from auxiliar import Auxiliar
from proyectil import Bullet
GROUND_COLLIDE_H = 8 
'''
ACA FALTAN SPRITES DE PATEAR
por ahora queda el 2
'''

variable_global = 0
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=600) -> None:
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/idle_2/({0}).png",1,1,flip=False,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/idle_2/({0}).png",1,1,flip=True,scale=p_scale)
        self.stay_r_buffed = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/buffed_walk_2/({0}).png",1,4,flip=False,scale=p_scale)
        self.stay_l_buffed = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/buffed_walk_2/({0}).png",1,4,flip=True,scale=p_scale)

        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/jump/({0}).png",1,7,flip=True,scale=p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/jump/({0}).png",1,7,flip=False,scale=p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/jump_2/({0}).png",1,8,flip=False,scale=p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/jump_2/({0}).png",1,8,flip=True,scale=p_scale)
        
        self.fall_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/fall/{0}.png",1,1,flip=False,scale=p_scale)
        self.fall_l = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/fall/{0}.png",1,1,flip=True,scale=p_scale)

        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/walk_2/({0}).png",1,4,flip=False,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/walk_2/({0}).png",1,4,flip=True,scale=p_scale)
        self.walk_r_buffed = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/buffed_walk_2/({0}).png",1,4,flip=False,scale=p_scale)
        self.walk_l_buffed = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/buffed_walk_2/({0}).png",1,4,flip=True,scale=p_scale)

        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/shoot/({0}).png",1,4,flip=False,scale=p_scale)
        self.shoot_l= Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/shoot/({0}).png",1,4,flip=True,scale=p_scale)
        
        self.push_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/push_2/({0}).png",1,4,flip=False,scale=p_scale)
        self.push_l= Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/push_2/({0}).png",1,4,flip=True,scale=p_scale)
        self.push_r_buffed = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/buffed_push_2/({0}).png",1,4,flip=False,scale=p_scale)
        self.push_l_buffed= Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/buffed_push_2/({0}).png",1,4,flip=True,scale=p_scale)
        # self.player_spawn = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/start/({0}).png",1,7,flip=True,scale=p_scale)
        self.kick_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/kick/({0}).png",1,4,flip=False,scale=p_scale)
        self.kick_l = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/kick/({0}).png",1,4,flip=True,scale=p_scale)

        self.in_snowball = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/in_snowball/({0}).png",1,4,flip=True,scale=p_scale)
        self.frame = 0
        self.lives = 3
        # self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/5,y+8,self.rect.width*3/5,self.rect.height-8)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H
        self.ground_collition_rect.width = self.ground_collition_rect.width - 4
        self.ground_collition_rect.x = x + self.ground_collition_rect.width/2 
        self.municiones = []

        self.is_jumping = False
        self.is_falling = False
        
        self.is_pushing  = False 
        self.is_kicking = False
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

        self.tiempo_last_shot =0
        
        self.is_buffed = False

        self.tiempo_last_push = 0

        self.tiempo_last_kick =0

        self.is_moving = False

        self.kicked = False

        self.ignore_platform = False

        self.tiempo_last_collide = 0

        self.is_trapped = False

    def walk(self,direction,on_off =True):
        # if not on_off:
        #     self.is_moving =False
        # else:
            if not self.is_jumping:
                if(not self.is_buffed and (self.direction != direction or((self.animation != self.walk_r and self.animation != self.walk_l)
                                        or (self.animation != self.push_r  and self.animation != self.push_l)))):

                    self.direction = direction
                    if(direction == DIRECTION_R):
                            self.move_x = self.speed_walk
                            if self.is_pushing:
                                self.animation = self.push_r
                            elif self.tiempo_transcurrido- self.tiempo_last_push>100:
                                if not self.is_falling:
                                    self.animation = self.walk_r
                            # print(self.move_x)
                    else:
                            self.move_x = -self.speed_walk
                            if self.is_pushing:
                                self.animation = self.push_l 
                            elif self.tiempo_transcurrido- self.tiempo_last_push>100:
                                if not self.is_falling:
                                    self.animation = self.walk_l
                    # self.is_moving =True

        
                

    def walk_buffed(self,direction):
        if not self.is_jumping:
            if(self.direction != direction or (self.animation != self.walk_r_buffed and self.animation != self.walk_l_buffed)):
                self.direction = direction
                if(direction == DIRECTION_R):
                    
                    self.move_x = self.speed_run
                    if not self.is_falling:
                        self.animation = self.walk_r_buffed
                else:
                    
                    self.move_x = -self.speed_run
                    if not self.is_falling:
                        self.animation = self.walk_l_buffed
                
                
    
    def jump(self,lista_plataformas, enemy_list , on_off = True):
        if self.is_on_platform(lista_plataformas,enemy_list):
            if(on_off and not self.is_jumping):
                self.y_start_jump = self.rect.y
                if(self.direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.move_y = -self.jump_power
                    self.animation = self.jump_r
                else:
                    self.move_x = -self.speed_walk
                    self.move_y = -self.jump_power
                    self.animation = self.jump_l
                self.frame = 0
                self.is_jumping = True
            if(on_off == False ):
                self.is_jumping = False
                self.stay()

    def stay(self):
        if(self.is_jumping or self.is_falling) or self.is_trapped:
            return
        
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def stay_buffed(self):
        if(self.is_jumping):
            return
        
        if(self.animation != self.stay_r_buffed and self.animation != self.stay_l_buffed):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r_buffed
            else:
                self.animation = self.stay_l_buffed
            self.move_x = 0
            self.move_y = 0
            

    def shoot_snow(self,on_off =True):
        self.is_shooting = on_off
        global variable_global
        if variable_global > 1:
            variable_global = 0
    
        if(not self.is_jumping and self.is_shooting): #and not self.is_fall):
            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l     
            bala = Bullet(self.rect.x,self.rect.y+10,10,35,45,self.direction, 400,variable_global)
            self.municiones.append(bala)
            
        variable_global +=1

    def push_snowball(self,enemy_list):
        for enemy in enemy_list:
            
            if (enemy.snowball_collition_rect.collidepoint(self.rect.midright) and enemy.times_hitted ==4 and self.direction ==DIRECTION_R) or (
                enemy.snowball_collition_rect.collidepoint(self.rect.midleft) and enemy.times_hitted ==4 and self.direction ==DIRECTION_L):
                
                if abs(self.rect.right - enemy.snowball_collition_rect.left) <8 or abs(self.rect.left - enemy.snowball_collition_rect.right) <8 :
                    self.is_pushing  = True 
                    self.tiempo_last_push = self.tiempo_transcurrido
                    break
                else:
                    
                    self.is_pushing  = False 
            else:
                
                self.is_pushing  = False 
        # print(self.is_pushing)


    def kick_snowball(self,enemy_list, delta_ms):
        if(not self.is_jumping):
            if(self.animation != self.kick_r and self.animation != self.kick_l):
                # self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.kick_r
                else:
                    self.animation = self.kick_l 
            for enemy in enemy_list:
                    if (abs(self.rect.right - enemy.snowball_collition_rect.left) <10 or abs(self.rect.left - enemy.snowball_collition_rect.right) <10) and (
                        enemy.times_hitted ==4):
                        enemy.got_kicked = True
                        enemy.direction_kicked = self.direction
            
    def check_collition(self, enemy_list):
        for enemy in enemy_list:
        
            if self.collition_rect.colliderect(enemy.collition_rect):
                if self.tiempo_transcurrido - self.tiempo_last_collide > INMUNITY_TIME:
                    self.tiempo_last_collide = self.tiempo_transcurrido
                    if not enemy.is_stunned :
                        self.lives -=1
                        
                if enemy.is_rolling:
                    # self.lives -=1
                    self.is_trapped = True
                    self.trapped_in_snowball( enemy)
                    # if self.animation != self.in_snowball:
                    #     self.frame =0
                    #     self.animation = self.in_snowball
                    # self.add_x(enemy.rect.x) 
                    # self.add_y(enemy.rect.y) 
                    
                else:
                    self.is_trapped = False

    def trapped_in_snowball(self, enemy):
        if self.is_trapped:
            if self.animation != self.in_snowball:
                self.frame =0
                self.animation = self.in_snowball
            
            self.rect.x = enemy.rect.x
            self.collition_rect.x = enemy.collition_rect.x
        
            self.ground_collition_rect.x = self.rect.x + self.ground_collition_rect.width/2 
            self.rect.y = enemy.rect.y
            self.ground_collition_rect.y =  self.rect.y + self.rect.height - GROUND_COLLIDE_H
            self.collition_rect.y = self.rect.y +8
        

        

    
    def do_movement(self,delta_ms,lista_plataformas,enemy_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            if((abs(self.y_start_jump)- abs(self.rect.y) > self.jump_height and self.is_jumping)) or  self.rect.y <0:
            
                self.move_y = 0

            self.tiempo_transcurrido_move = 0
            self.add_x(self.move_x)
            self.add_y(self.move_y)

            if not self.is_on_platform(lista_plataformas,enemy_list) or (self.ignore_platform and self.ground_collition_rect.bottom  < GROUND_LEVEL):
                 self.add_y(self.gravity)
                 if not self.is_jumping:
                     self.is_falling = True
                     if(self.direction == DIRECTION_R):
                         self.animation = self.fall_r
                         self.frame = 0
                         
                     else:
                         self.animation = self.fall_l
                         self.frame = 0
            elif(self.is_jumping): # SACAR
                self.jump(lista_plataformas,enemy_list, False)


    def is_on_platform(self,lista_plataformas,enemy_list):
        retorno = False
        if(self.ground_collition_rect.bottom  >= GROUND_LEVEL):     
            retorno = True
            self.is_falling = False
        else:
            for plataforma in lista_plataformas:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    self.is_falling = False
                    break  
            for enemy in enemy_list:
                if(self.ground_collition_rect.colliderect(enemy.snowball_top_collition_rect)
                   and (enemy.is_rolling or enemy.times_hitted ==4) ):
                    retorno = True
                    self.is_falling = False
                    break   
        return retorno

                           
    def add_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x
        if self.rect.left <0:
            self.rect.x =0
            self.collition_rect.x = self.rect.width/5
            self.ground_collition_rect.x = self.rect.x + self.rect.w / 3
        elif self.rect.right >ANCHO_VENTANA:
            self.rect.right = ANCHO_VENTANA
            self.collition_rect.right = ANCHO_VENTANA - self.rect.width/5
            self.ground_collition_rect.x = ANCHO_VENTANA - 2*self.rect.w / 3
            
    def add_y(self,delta_y):
        self.rect.y += delta_y  
        self.ground_collition_rect.y += delta_y
        self.collition_rect.y += delta_y
        
        

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0


    def update(self,delta_ms,lista_plataformas,enemy_list):
        
        self.push_snowball(enemy_list)
        self.check_collition(enemy_list)
        if not self.is_trapped:

            self.do_movement(delta_ms,lista_plataformas,enemy_list)
        self.do_animation(delta_ms)
        

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.collition_rect)
            pygame.draw.rect(screen,GREEN,self.ground_collition_rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        # print(self.is_trapped)
        
        

    def events(self,delta_ms,keys, enemy_list,lista_plataformas):
        self.tiempo_transcurrido += delta_ms

        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            if self.is_buffed:
                self.walk_buffed(DIRECTION_L)            
            else:
                self.walk(DIRECTION_L)
        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            if self.is_buffed:
                self.walk_buffed(DIRECTION_R)
            else:    
                self.walk(DIRECTION_R)
        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not keys[pygame.K_s] and not keys[pygame.K_f]):
            if self.is_buffed:
                self.stay_buffed()
            else:
                self.stay()
            
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()   

        if(keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(lista_plataformas,enemy_list,True)
                self.tiempo_last_jump = self.tiempo_transcurrido
            

        if(keys[pygame.K_s]):
            if((self.tiempo_transcurrido - self.tiempo_last_shot) > COOLDOWN_DISPARO):
                self.shoot_snow() 
                self.tiempo_last_shot = self.tiempo_transcurrido

        if(not keys[pygame.K_s]):
            
           self.shoot_snow(False) 
           

        if(keys[pygame.K_f]):
            
            self.kick_snowball(enemy_list,delta_ms)

        if(keys[pygame.K_DOWN]):
            self.ignore_platform = True
        else:
            self.ignore_platform = False
            
                
                
                
                
            
            



            