from player import *
from constantes import *
from auxiliar import Auxiliar
from botin import Loot
GROUND_COLLIDE_H = 8 


class Enemy:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,id,p_scale=1,interval_time_jump=100) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/enemies/red/walk/{0}.png",1,3,flip=True, scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("my_images/enemies/red/walk/{0}.png",1,3,scale=p_scale)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/enemies/red/idle/{0}.png",1,1,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("my_images/enemies/red/idle/{0}.png",1,1,flip=True,scale=p_scale)
        self.death_hit = Auxiliar.getSurfaceFromSeparateFiles("my_images/enemies/red/death/{0}.png",1,2,flip=True,scale=p_scale)
        self.death_in_air = Auxiliar.getSurfaceFromSeparateFiles("my_images/enemies/red/death/{0}.png",3,4,flip=True,scale=p_scale)
        self.death_on_platflorm = Auxiliar.getSurfaceFromSeparateFiles("my_images/enemies/red/death/{0}.png",7,3,flip=True,scale=p_scale)
        self.animation_snow_enemy = Auxiliar.getSurfaceFromSeparateFiles("my_images/enemies/red/snowball/{0}.png",1,2,flip=True,scale=p_scale)
        self.animation_snow = Auxiliar.getSurfaceFromSeparateFiles("my_images/others/snowball/({0}).png",1,5,flip=True,scale=p_scale+0.3)
        self.snowball_roll = Auxiliar.getSurfaceFromSeparateFiles("my_images/others/snowball_2/({0}).png",1,4,flip=False,scale=p_scale+0.3)
        self.explosion = Auxiliar.getSurfaceFromSeparateFiles("my_images/enemies/explosion/big-explosion{0}.png",1,9,flip=False,scale=p_scale-0.8)
        self.id = id
        self.contador = 0
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.is_dead = False
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/6,y,self.rect.width*2/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H
        self.death_time = 0
        #Creacion de hitbox de bola de nieve
        self.times_hitted = 0
        self.image_snow = self.animation_snow[self.times_hitted] 
        self.snowball_rect = self.image.get_rect()
        self.snowball_rect.x = x
        self.snowball_rect.y = y
        self.snowball_collition_rect = pygame.Rect(self.rect.x,self.rect.y,self.snowball_rect.width,self.snowball_rect.height)

        self.snowball_ground_collition_rect = pygame.Rect(self.snowball_collition_rect)
        self.snowball_ground_collition_rect.height = GROUND_COLLIDE_H
        self.snowball_ground_collition_rect.y = y + self.snowball_rect.height - GROUND_COLLIDE_H


        self.snowball_top_collition_rect = pygame.Rect(self.snowball_collition_rect)
        self.snowball_top_collition_rect.height = GROUND_COLLIDE_H
        self.snowball_top_collition_rect.width = self.snowball_collition_rect.width / 2
        self.snowball_top_collition_rect.y = y - GROUND_COLLIDE_H
        self.snowball_top_collition_rect.x = x + self.snowball_collition_rect.width / 4

        # self.snowball_left_collition_rect = pygame.Rect(self.snowball_collition_rect)
        # self.snowball_left_collition_rect.width = GROUND_COLLIDE_H
        # self.snowball_left_collition_rect.height = self.snowball_rect.height/2                        POR AHORA ESTO NO SIRVE
        # self.snowball_left_collition_rect.y = y + GROUND_COLLIDE_H
        # self.snowball_left_collition_rect.x = self.snowball_rect.x
        
        # self.snowball_right_collition_rect = pygame.Rect(self.snowball_collition_rect)
        # self.snowball_right_collition_rect.width = GROUND_COLLIDE_H
        # self.snowball_right_collition_rect.height = self.snowball_rect.height/2
        # self.snowball_right_collition_rect.y = y + GROUND_COLLIDE_H
        # self.snowball_right_collition_rect.x = self.snowball_rect.right

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_stunned = False
        self.is_rolling = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 
        self.interval_time_jump = interval_time_jump
        
        self.tiempo_last_hit = 0 
        self.interval_time_freeze = 1200
        
        self.tiempo_last_true =0

        self.tiempo_transcurrido_pateado  =0

        self.got_kicked = False
        self.direction_kicked = None
        self.is_exploting = False

    def change_x(self,delta_x):
        if self.is_stunned and not self.is_rolling:
            pass
        else:
            self.rect.x += delta_x
            self.collition_rect.x += delta_x
            self.ground_collition_rect.x += delta_x
            self.snowball_collition_rect.x += delta_x
            self.snowball_ground_collition_rect.x += delta_x
            self.snowball_top_collition_rect.x += delta_x
            # self.snowball_left_collition_rect.x += delta_x
            # self.snowball_right_collition_rect.x += delta_x
            if self.rect.left <0:
                self.rect.x *=0
                self.collition_rect.x = self.rect.width/6
                self.ground_collition_rect.x = self.rect.x + self.rect.w / 3
                self.snowball_collition_rect.x = 0
                self.snowball_ground_collition_rect.x = 0
                self.snowball_top_collition_rect.x = self.snowball_collition_rect.width / 4
                # self.snowball_left_collition_rect.x =0
                # self.snowball_right_collition_rect.x = self.rect.width
            elif self.rect.right >ANCHO_VENTANA:
                self.rect.right = ANCHO_VENTANA
                self.collition_rect.right = ANCHO_VENTANA - self.rect.width/6
                self.ground_collition_rect.right = ANCHO_VENTANA - 2*self.rect.w / 3
                self.snowball_collition_rect.right = ANCHO_VENTANA
                self.snowball_ground_collition_rect.right = ANCHO_VENTANA
                self.snowball_top_collition_rect.right= ANCHO_VENTANA - self.snowball_collition_rect.width / 4
                # self.snowball_left_collition_rect.x =ANCHO_VENTANA-self.rect.width
                # self.snowball_right_collition_rect.x =ANCHO_VENTANA

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y
        self.snowball_collition_rect.y += delta_y
        self.snowball_ground_collition_rect.y += delta_y
        self.snowball_top_collition_rect.y += delta_y
        # self.snowball_left_collition_rect.y += delta_y
        # self.snowball_right_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        if self.is_stunned:
            if(not self.is_on_plataform(plataform_list)):
                    if(self.move_y == 0):
                        self.is_fall = True
                        self.change_y(self.gravity)
            pass
        else:
            self.tiempo_transcurrido_move += delta_ms
            if(self.tiempo_transcurrido_move >= self.move_rate_ms):
                self.tiempo_transcurrido_move = 0

                if(not self.is_on_plataform(plataform_list)):
                    if(self.move_y == 0):
                        self.is_fall = True
                        self.change_y(self.gravity)
                else:
                    self.is_fall = False
                    self.change_x(self.move_x)
                    if self.contador <= 50:
                        self.move_x = -self.speed_walk
                        self.animation = self.walk_l
                        self.contador += 1 
                    elif self.contador <= 100:
                        self.move_x = self.speed_walk
                        self.animation = self.walk_r
                        self.contador += 1
                    else:
                        self.contador = 0
    
    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno    
    
    

    def snow_trap(self, lista_proyectiles, delta_ms):
        self.tiempo_transcurrido += delta_ms
        if not self.got_kicked:
            if (self.tiempo_transcurrido - self.tiempo_last_hit > self.interval_time_freeze) and not self.is_rolling:
                if self.times_hitted >0:
                    self.times_hitted -=1
                    self.tiempo_last_hit = self.tiempo_transcurrido
                    self.animation = self.animation_snow_enemy
                    self.frame = 0
                else:
                    self.is_stunned = False
        for proyectil in lista_proyectiles:
                if self.rect.colliderect(proyectil.rect):
                    self.tiempo_last_hit = self.tiempo_transcurrido
                    self.is_stunned  = True
                    if self.times_hitted < 4:
                        self.times_hitted +=1
                    elif self.times_hitted ==4:
                        self.tiempo_last_hit += 4000
                    lista_proyectiles.remove(proyectil)
                    del proyectil
        

    def rolling_ball(self,player,delta_ms):
        self.tiempo_transcurrido +=delta_ms
        if player.is_pushing and self.times_hitted ==4:
            self.change_x(player.move_x)
            self.animation = self.snowball_roll
            self.is_rolling = True
            self.tiempo_last_true = self.tiempo_transcurrido
        else:
            if self.tiempo_transcurrido - self.tiempo_last_true > 100 and not self.got_kicked:
                self.is_rolling = False

    def kicked_ball(self,delta_ms,platform_list):
        
        self.tiempo_transcurrido_pateado += delta_ms
        if self.tiempo_transcurrido_pateado < 5000:
            if self.animation != self.snowball_roll:
                self.animation = self.snowball_roll
            self.is_rolling = True
            if self.direction_kicked == DIRECTION_L:
                self.change_x(-20)    
            else:
                self.change_x(20)

            
            if (self.rect.left ==0 or self.rect.right == ANCHO_VENTANA) and self.ground_collition_rect.bottom >= GROUND_LEVEL:
                self.got_kicked = False
                self.is_rolling = False
                # HACER QUE SE MUERA, EXPLOSION
                self.is_dead = True
                self.is_exploting = True
                self.death_time = self.tiempo_transcurrido

            if self.rect.left ==0:
                self.direction_kicked = DIRECTION_R
            elif self.rect.right == ANCHO_VENTANA:
                self.direction_kicked = DIRECTION_L

            if(not self.is_on_plataform(platform_list)):
                    if(self.move_y == 0):
                        self.is_fall = True
                        self.change_y(self.gravity)
        else:
            self.got_kicked = False
            self.is_rolling = False
            self.tiempo_transcurrido_pateado = 0
            
        # print(self.tiempo_transcurrido_pateado)
        
        
    def check_collition(self, enemy_list):
        for enemy in enemy_list:
            if enemy.id != self.id:
                if self.collition_rect.colliderect(enemy.collition_rect) and self.got_kicked and not enemy.is_dead:

                    # enemy_list.remove(enemy)
                    # del enemy
                    enemy.is_dead = True
                    enemy.direction_kicked = self.direction_kicked
                    enemy.death_time = self.tiempo_transcurrido

    def death_state(self,enemy_list,plataform_list):
        if self.is_dead :
            if not self.is_exploting:
                if self.tiempo_transcurrido - self.death_time <3000:
                    if self.direction_kicked == DIRECTION_L:
                            self.change_x(-8)
                    else:
                        self.change_x(8)
                    if self.rect.left ==0:
                        self.direction_kicked = DIRECTION_R
                    elif self.rect.right == ANCHO_VENTANA:
                        self.direction_kicked = DIRECTION_L
                elif self.tiempo_transcurrido - self.death_time >4500:
                    self.remove_from_list(enemy_list)

                if self.tiempo_transcurrido - self.death_time <300:
                    if self.animation != self.death_hit:
                        self.frame = 0
                        
                        self.animation = self.death_hit
                elif self.tiempo_transcurrido - self.death_time <1700:
                    self.change_y(-self.gravity)
                    
                    if self.animation != self.death_in_air:
                        self.frame = 0   
                        self.animation = self.death_in_air
                elif self.tiempo_transcurrido - self.death_time <3000:
                    self.change_y(self.gravity)
                    if self.animation != self.death_on_platflorm:
                        self.frame = 0   
                        self.animation = self.death_on_platflorm
                else:
                    if(not self.is_on_plataform(plataform_list)):
                        self.change_y(self.gravity)
            else:
                if self.animation != self.explosion:
                    self.animation = self.explosion
                    self.frame = 0
                    self.frame_rate_ms = 70
                if self.tiempo_transcurrido - self.death_time >630:
                    self.remove_from_list(enemy_list)


    def remove_from_list(self,enemy_list):
        for enemy in enemy_list:
            if self.id == enemy.id:
                enemy_list.remove(enemy)
                del enemy

    def do_animation(self,delta_ms):
        if self.is_dead and self.animation == self.death_on_platflorm:
            self.frame_rate_ms = 700

        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def update(self,delta_ms,plataform_list, bullet_list, player, enemy_list):
        if self.is_dead:
            self.death_state(enemy_list,plataform_list)
        else:    
            if self.got_kicked:
                self.kicked_ball(delta_ms,plataform_list )
            else:
                self.do_movement(delta_ms,plataform_list)
        self.rolling_ball(player,delta_ms)  
        self.check_collition(enemy_list)
        self.snow_trap(bullet_list, delta_ms)
        self.do_animation(delta_ms) 

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=(0,255,0),rect=self.collition_rect)
            if self.is_stunned:
                pygame.draw.rect(screen,color=(0,255,0),rect=self.snowball_collition_rect)
                pygame.draw.rect(screen,color=(255,0,0),rect=self.snowball_ground_collition_rect)
                # pygame.draw.rect(screen,color=(255,255,0),rect=self.snowball_left_collition_rect)
                # pygame.draw.rect(screen,color=(0,255,0),rect=self.snowball_right_collition_rect)
                pygame.draw.rect(screen,color=(0,0,255),rect=self.snowball_top_collition_rect )
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

        if self.is_stunned and not self.is_rolling and not self.is_dead:
            
            self.image_snow = self.animation_snow[self.times_hitted-1]
            screen.blit(self.image_snow,self.rect)

