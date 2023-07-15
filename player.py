import pygame
from constantes import *
from auxiliar import Auxiliar
from bullet import Bullet
from loot import Loot
from math import sin 


variable_global = 0
class Player():
    stats_init = [False,False,False,2,0]
    def __init__(self,x,y,speed_walk=6,speed_run=10,gravity=15,jump_power=40,frame_rate_ms=35,move_rate_ms=33,jump_height=105, p_scale = 3.2,interval_time_jump=600) -> None:
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
        self.walk_shoot_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/walk_and_shoot/({0}).png",1,8,flip=False,scale=p_scale)
        self.walk_shoot_l= Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/walk_and_shoot/({0}).png",1,8,flip=True,scale=p_scale)
        self.push_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/push_2/({0}).png",1,4,flip=False,scale=p_scale)
        self.push_l= Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/push_2/({0}).png",1,4,flip=True,scale=p_scale)
        self.push_r_buffed = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/buffed_push_2/({0}).png",1,4,flip=False,scale=p_scale)
        self.push_l_buffed= Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/buffed_push_2/({0}).png",1,4,flip=True,scale=p_scale)
        self.player_spawn = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/start/({0}).png",1,7,flip=True,scale=p_scale)
        self.kick_r = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/kick/({0}).png",1,4,flip=False,scale=p_scale)
        self.kick_l = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/kick/({0}).png",1,4,flip=True,scale=p_scale)
        self.death = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/death/({0}).png",1,16,flip=False,scale=p_scale)
        self.in_snowball = Auxiliar.getSurfaceFromSeparateFiles("my_images/caracter/in_snowball/({0}).png",1,4,flip=True,scale=p_scale)
        self.frame = 0
        self.lives = Player.stats_init[3]
        self.score = Player.stats_init[4]
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
        self.rect_x_init = x
        self.rect_y_init = y
        self.collition_rect = pygame.Rect(x+self.rect.width/5,y+8,self.rect.width*3/5,self.rect.height-8)
        self.collition_rect_x_init = x+self.rect.width/5
        self.collition_rect_y_init = y+8
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H
        self.ground_collition_rect_y_init = y + self.rect.height - GROUND_COLLIDE_H
        self.ground_collition_rect.width = self.ground_collition_rect.width - 4
        self.ground_collition_rect.x = x + self.ground_collition_rect.width/2 
        self.ground_collition_rect_x_init = x + self.ground_collition_rect.width/2 
        self.municiones = []
        self.tiempo_spawn = 0
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
        self.tiempo_last_push = 0
        self.tiempo_last_kick =0
        self.death_time = 0
        Loot.loot_list.clear()
        self.loot_list = Loot.loot_list
        # self.ignore_platform = False
        self.is_moving = False
        self.is_jumping = False
        self.is_falling = False
        self.is_pushing  = False 
        self.is_kicking = False
        self.kicked = False
        self.is_dead = False
        self.is_trapped = False
        self.enemy_pushed_id = None
        self.is_buffed_speed = Player.stats_init[0]
        self.is_buffed_bullet = Player.stats_init[1]
        self.is_buffed_reach = Player.stats_init[2]
        self.is_inmune = True   

    def spawn_pos(self):
        self.rect.x = self.rect_x_init
        self.collition_rect.x = self.collition_rect_x_init
        self.ground_collition_rect.x = self.ground_collition_rect_x_init
        self.rect.y = self.rect_y_init
        self.collition_rect.y = self.collition_rect_y_init
        self.ground_collition_rect.y = self.ground_collition_rect_y_init

    def walk(self,direction,on_off =True):
        if not self.is_jumping:
            if(not self.is_buffed_speed and (self.direction != direction or((self.animation != self.walk_r and self.animation != self.walk_l)
                                    or (self.animation != self.push_r  and self.animation != self.push_l)))):
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    if self.is_pushing:
                        self.animation = self.push_r
                    elif self.tiempo_transcurrido- self.tiempo_last_push>100:
                        if not self.is_falling and not self.is_shooting:
                            self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    if self.is_pushing:
                        self.animation = self.push_l 
                    elif self.tiempo_transcurrido- self.tiempo_last_push>100: 
                        if not self.is_falling and not self.is_shooting:
                            self.animation = self.walk_l
                    
  
    def walk_buffed(self,direction):
        if not self.is_jumping:
            if(self.direction != direction or ((self.animation != self.walk_r_buffed and self.animation != self.walk_l_buffed)
                                               or (self.animation != self.push_r_buffed  and self.animation != self.push_l_buffed))):
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_run
                    if self.is_pushing:
                        self.animation = self.push_r_buffed
                    elif self.tiempo_transcurrido- self.tiempo_last_push>100:
                        if not self.is_falling and not self.is_shooting:
                            self.animation = self.walk_r_buffed
                else:
                    self.move_x = -self.speed_run
                    if self.is_pushing:
                        self.animation = self.push_l_buffed 
                    elif self.tiempo_transcurrido- self.tiempo_last_push>100: 
                        if not self.is_falling and not self.is_shooting:
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
            self.frame = 0
            self.move_x = 0
            self.move_y = 0
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            

    def stay_buffed(self):
        if(self.is_jumping or self.is_falling) or self.is_trapped:
            return
        
        if(self.animation != self.stay_r_buffed and self.animation != self.stay_l_buffed):
            self.frame = 0
            self.move_x = 0
            self.move_y = 0
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r_buffed
            else:
                self.animation = self.stay_l_buffed
            

    def shoot_snow(self,sound_list,on_off =True):
        self.is_shooting = on_off
        global variable_global
        if variable_global > 1:
            variable_global = 0
    
        if(not self.is_jumping and self.is_shooting): 
            
            if(self.direction == DIRECTION_R and self.animation != self.shoot_r):
                self.animation = self.shoot_r
            elif(self.direction == DIRECTION_L and self.animation != self.shoot_l):
                self.animation = self.shoot_l     
            if self.is_buffed_reach:
                reach = BUFFED_REACH
            else:
                reach = NORMAL_REACH
            pygame.mixer.Sound.play(sound_list[SHOOT])
            bala = Bullet(self.rect.x,self.rect.y+10,abs(self.move_x)/3+10,35,45,self.direction, reach,variable_global,self.is_buffed_bullet)
            self.municiones.append(bala)
            
        variable_global +=1

    def push_snowball(self,enemy_list):
        for enemy in enemy_list:
            
            if (enemy.snowball_collition_rect.collidepoint(self.rect.midright) and enemy.times_hitted ==4 and self.direction ==DIRECTION_R) or (
                enemy.snowball_collition_rect.collidepoint(self.rect.midleft) and enemy.times_hitted ==4 and self.direction ==DIRECTION_L):
                
                if abs(self.rect.right - enemy.snowball_collition_rect.left) <8 or abs(self.rect.left - enemy.snowball_collition_rect.right) <8 :
                    self.is_pushing  = True 
                    self.tiempo_last_push = self.tiempo_transcurrido
                    self.enemy_pushed_id = enemy.id
                    break
                else:
                    
                    self.is_pushing  = False 
            else:
                
                self.is_pushing  = False 

    def kick_snowball(self,enemy_list):
        if(not self.is_jumping):
            if(self.animation != self.kick_r and self.animation != self.kick_l):
                if(self.direction == DIRECTION_R):
                    self.animation = self.kick_r
                else:
                    self.animation = self.kick_l 
            for enemy in enemy_list:
                    if (abs(self.rect.right - enemy.snowball_collition_rect.left) <10 or abs(self.rect.left - enemy.snowball_collition_rect.right) <10) and (
                        enemy.times_hitted ==4):
                        enemy.got_kicked = True
                        enemy.direction_kicked = self.direction
            
    def check_collition(self, enemy_list,sound_list):
        for enemy in enemy_list:
        
            if self.collition_rect.colliderect(enemy.collition_rect):
                if (self.tiempo_transcurrido - self.tiempo_spawn > INMUNITY_TIME) and not enemy.is_stunned and not enemy.is_dead and not self.is_trapped:
                    self.death_time = self.tiempo_transcurrido
                    self.lives -=1
                    Player.stats_init[3] = self.lives
                    self.is_dead = True
                    self.animation = self.death
                if enemy.is_rolling:
                    self.is_trapped = True
                    self.trapped_in_snowball(enemy,sound_list)
                else:
                    self.is_trapped = False

    def check_collition_with_items(self,sound_list):
        for item in self.loot_list:
            if self.collition_rect.colliderect(item.rect):
                if item.value == YELLOW_POT and not self.is_buffed_reach:
                    self.is_buffed_reach = True
                    Player.stats_init[2] = self.is_buffed_reach
                    pygame.mixer.Sound.play(sound_list[POWER_UP])
                elif item.value == BLUE_POT and not self.is_buffed_bullet:
                    self.is_buffed_bullet = True
                    Player.stats_init[1] = self.is_buffed_bullet
                    pygame.mixer.Sound.play(sound_list[POWER_UP])
                elif item.value == RED_POT and not self.is_buffed_speed:
                    self.is_buffed_speed = True
                    Player.stats_init[0] = self.is_buffed_speed
                    pygame.mixer.Sound.play(sound_list[POWER_UP])
                else:
                    pygame.mixer.Sound.play(sound_list[PICK_UP])
                self.score += item.value
                Player.stats_init[4] = self.score
                self.loot_list.remove(item)

    def death_state(self,sound_list):
        if self.tiempo_transcurrido - self.death_time <800:
            self.add_y(-5)
            pygame.mixer.Sound.play(sound_list[SELF_HIT])
        if self.tiempo_transcurrido - self.death_time <3200:
            if self.animation != self.death:
                
                self.frame =0
                self.animation = self.death
        else:
            self.frame = 0
            self.lose_buffs()
            self.spawn_pos()
            self.tiempo_spawn = self.tiempo_transcurrido
            self.is_dead = False
            self.is_inmune = True     
                    
    def lose_buffs(self):
        self.is_buffed_speed = False
        self.is_buffed_bullet = False
        self.is_buffed_reach = False
        Player.stats_init[0] = self.is_buffed_speed
        Player.stats_init[1] = self.is_buffed_bullet
        Player.stats_init[2] = self.is_buffed_reach 

    def inmunity_timer(self):
        if self.tiempo_transcurrido-self.tiempo_spawn> INMUNITY_TIME:
            self.is_inmune = False

    def wave_value(self):
        value = sin(self.tiempo_transcurrido)
        if value < 0:
            return 0
        else:
            return 255
                    
    def trapped_in_snowball(self, enemy,sound_list):
        if self.is_trapped:
            if self.animation != self.in_snowball:
                self.frame =0
                self.animation = self.in_snowball
                pygame.mixer.Sound.play(sound_list[HITTED_BALL])
            
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
            if self.is_moving:
                self.add_x(self.move_x,lista_plataformas)
            self.add_y(self.move_y)
            self.apply_gravity(lista_plataformas,enemy_list)


    def apply_gravity(self,lista_plataformas,enemy_list):
        if not self.is_on_platform(lista_plataformas,enemy_list): #or (self.ignore_platform and self.ground_collition_rect.bottom  < GROUND_LEVEL): mecanica no implementada
                 self.add_y(self.gravity)
                 if not self.is_jumping:
                    self.is_falling = True
                    if(self.direction == DIRECTION_R):
                        self.animation = self.fall_r
                    else:
                        self.animation = self.fall_l
                    self.frame = 0 
        elif(self.is_jumping):
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

    def is_next_to_platform(self,lista_plataformas):
        if not self.is_jumping:
            for plataforma in lista_plataformas:
                if ((plataforma.rect.collidepoint(self.collition_rect.midleft) or plataforma.rect.collidepoint(self.collition_rect.midright)) and 
                    not abs(self.ground_collition_rect.y -plataforma.ground_collition_rect.y)<8):
                    if abs(self.collition_rect.left - plataforma.rect.right) <6:
                        self.rect.x =plataforma.rect.right
                        self.collition_rect.x = plataforma.rect.right + self.rect.width/5
                        self.ground_collition_rect.x = self.rect.x + self.rect.w / 3
                    elif abs(self.collition_rect.right - plataforma.rect.left) <6:
                        self.rect.right =plataforma.rect.left
                        self.collition_rect.right = plataforma.rect.left - self.rect.width/5
                        self.ground_collition_rect.x = plataforma.rect.left - 2*self.rect.w / 3
                        
                                
    def add_x(self,delta_x,lista_plataformas):
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
        self.is_next_to_platform(lista_plataformas)
        
            
    def add_y(self,delta_y):
        self.rect.y += delta_y  
        self.ground_collition_rect.y += delta_y
        self.collition_rect.y += delta_y
        
    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.is_dead:
            if(self.tiempo_transcurrido_animation >=160):
                self.tiempo_transcurrido_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                else: 
                    self.frame = 15
        else:
            if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
                self.tiempo_transcurrido_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                else: 
                    self.frame = 0


    def update(self,delta_ms,lista_plataformas,enemy_list,sound_list):
        if self.is_dead:
            self.death_state(sound_list)
        else:
            self.check_collition_with_items(sound_list)
            self.push_snowball(enemy_list)
            self.check_collition(enemy_list,sound_list)
            if not self.is_trapped:
                self.do_movement(delta_ms,lista_plataformas,enemy_list)
        self.do_animation(delta_ms)
        self.inmunity_timer()
        

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.collition_rect)
            pygame.draw.rect(screen,GREEN,self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        if self.is_inmune:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)


    def events(self,delta_ms,keys, enemy_list,lista_plataformas,sound_list):
        self.tiempo_transcurrido += delta_ms
        if not self.is_dead:
            if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
                if self.is_buffed_speed:
                    self.walk_buffed(DIRECTION_L)            
                else:
                    self.walk(DIRECTION_L)
                self.is_moving = True
        
            if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
                if self.is_buffed_speed:
                    self.walk_buffed(DIRECTION_R)
                else:    
                    self.walk(DIRECTION_R)
                self.is_moving = True
            
            if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
                self.is_moving = False
        
            if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not keys[pygame.K_s] and not keys[pygame.K_f]):
                if self.is_buffed_speed:
                    self.stay_buffed()
                else:
                    self.stay()
                
            if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
                if self.is_buffed_speed:
                    self.stay_buffed()
                else:
                    self.stay()  

            if(keys[pygame.K_SPACE]):
                if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                    self.jump(lista_plataformas,enemy_list,True)
                    pygame.mixer.Sound.play(sound_list[JUMP])
                    self.tiempo_last_jump = self.tiempo_transcurrido
                

            if(keys[pygame.K_s]):
                if((self.tiempo_transcurrido - self.tiempo_last_shot) > COOLDOWN_DISPARO):
                    self.shoot_snow(sound_list) 
                    self.tiempo_last_shot = self.tiempo_transcurrido

            if(not keys[pygame.K_s]):
                
                self.shoot_snow(sound_list,False) 
            

            if(keys[pygame.K_f]):
                
                self.kick_snowball(enemy_list)


        # if(keys[pygame.K_DOWN]):
        #     self.ignore_platform = True
        # else:
        #     self.ignore_platform = False
            
                
                
                
                
            
            



            