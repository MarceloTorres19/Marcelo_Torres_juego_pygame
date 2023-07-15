# from curses import KEY_DOWN, KEY_LEFT, KEY_RIGHT
import pygame

from constantes import *
from player import Player
from plataforma import Platform
from enemy import Enemy
from bullet import Bullet
from loot import Loot


screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

# imagen_fondo = pygame.image.load("my_images/locations/stage1.png")
imagen_fondo = pygame.image.load("my_images/locations/stage1.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))


player_1 = Player(x=0,y=400,speed_walk=6,speed_run=10,gravity=15,jump_power=40,frame_rate_ms=35,move_rate_ms=33,jump_height=120, p_scale = 3.2)
lut = Loot(50,400)
lut2 = Loot(100,400)
lut3 = Loot(300,400)
lut11 = Loot(200,400)
lut22 = Loot(360,400)
lut33 = Loot(420,400)
lista_lut=[lut,lut2,lut3,lut11,lut22,lut33]
lista_plataformas = []

lista_plataformas.append(Platform(0,570,220,50,3))
lista_plataformas.append(Platform(340,570,220,50,3))
lista_plataformas.append(Platform(ANCHO_VENTANA-220,570,220,50,3))
lista_plataformas.append(Platform(150,460,600,50,5))
lista_plataformas.append(Platform(0,350,350,50,6))
lista_plataformas.append(Platform(ANCHO_VENTANA-350,350,350,50,6))
lista_plataformas.append(Platform(200,180,500,100,7))
lista_plataformas.append(Platform(100,230,100,50,8))
lista_plataformas.append(Platform(ANCHO_VENTANA-200,230,100,50,9))
lista_plataformas.append(Platform(0,680,ANCHO_VENTANA,50,4))

enemy_list = []
# enemy_list.append (Enemy(x=450,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=35,move_rate_ms=33,jump_height=140,p_scale=2.9,interval_time_jump=300))
enemy_list.append (Enemy(x=450,y=400,speed_walk=6,speed_run=5,gravity=12,jump_power=30,frame_rate_ms=35,move_rate_ms=33,jump_height=140,id=1,p_scale=2.9,interval_time_jump=300))
enemy_list.append (Enemy(x=300,y=50,speed_walk=6,speed_run=5,gravity=12,jump_power=30,frame_rate_ms=35,move_rate_ms=33,jump_height=140,id=2,p_scale=2.9,interval_time_jump=300))
enemy_list.append (Enemy(x=400,y=68,speed_walk=6,speed_run=5,gravity=12,jump_power=30,frame_rate_ms=35,move_rate_ms=33,jump_height=140,id=3,p_scale=2.9,interval_time_jump=300))

enemy_list.append (Enemy(x=400,y=580,speed_walk=6,speed_run=5,gravity=12,jump_power=30,frame_rate_ms=35,move_rate_ms=33,jump_height=140,id=4,p_scale=2.9,interval_time_jump=300))
enemy_list.append (Enemy(x=400,y=600,speed_walk=6,speed_run=5,gravity=12,jump_power=30,frame_rate_ms=35,move_rate_ms=33,jump_height=140,id=5,p_scale=2.9,interval_time_jump=300))
balas = player_1.municiones

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
            
    keys = pygame.key.get_pressed()

    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())

    for plataforma in lista_plataformas:
        plataforma.draw(screen)

    for enemy in enemy_list:
        enemy.update(delta_ms,lista_plataformas,balas,player_1,enemy_list)
        enemy.draw(screen)
    
    for bala in balas:
        bala.update(delta_ms,lista_plataformas, enemy_list, player_1) 
        bala.draw(screen) 
        if abs(bala.x_init -bala.x) > bala.reach:
            balas.remove(bala)
            del bala
    
    for lot in lista_lut:
        lot.update(delta_ms)
        lot.draw(screen)

    player_1.events(delta_ms,keys,enemy_list,lista_plataformas)
    player_1.update(delta_ms,lista_plataformas,enemy_list)
    player_1.draw(screen)

    pygame.display.flip()
    
pygame.quit()

#level_1
        # self.plataform_list.append(Platform(0,630,220,50,3))
        # self.plataform_list.append(Platform(340,630,220,50,3))
        # self.plataform_list.append(Platform(ANCHO_VENTANA-220,630,220,50,3))
        # self.plataform_list.append(Platform(150,520,600,50,5))
        # self.plataform_list.append(Platform(0,410,350,50,6))
        # self.plataform_list.append(Platform(ANCHO_VENTANA-350,410,350,50,6))
        # self.plataform_list.append(Platform(200,240,500,100,7))
        # self.plataform_list.append(Platform(100,290,100,50,8))
        # self.plataform_list.append(Platform(ANCHO_VENTANA-200,290,100,50,9))
        # self.plataform_list.append(Platform(0,740,ANCHO_VENTANA,50,4))
        #level_2
        # self.plataform_list.append(Platform(220,630,508,50,12))
        # self.plataform_list.append(Platform(108,520,112,160,10))
        # self.plataform_list.append(Platform(350,520,315,50,13))
        # self.plataform_list.append(Platform(665,410,112,160,11))
        # self.plataform_list.append(Platform(350,300,315,50,13))
        # self.plataform_list.append(Platform(665,190,112,160,11))
        # self.plataform_list.append(Platform(108,300,112,160,10))
        # self.plataform_list.append(Platform(220,410,315,50,14))
        # self.plataform_list.append(Platform(170,190,350,50,16))
        # self.plataform_list.append(Platform(0,740,ANCHO_VENTANA,50,4))
        #level_3

        # self.plataform_list.append(Platform(290,190,440,50,24))
        # self.plataform_list.append(Platform(730,190,50,270,23))
        # self.plataform_list.append(Platform(165,300,440,50,27))
        # self.plataform_list.append(Platform(165,410,50,50,25))
        # self.plataform_list.append(Platform(115,300,50,160,26))
        # self.plataform_list.append(Platform(400,410,330,50,22))
        # self.plataform_list.append(Platform(0,520,395,50,28))
        # self.plataform_list.append(Platform(505,520,395,50,29))
        # self.plataform_list.append(Platform(505,630,280,50,21))
        # self.plataform_list.append(Platform(ANCHO_VENTANA-115,570,115,110,20))
        # self.plataform_list.append(Platform(115,630,280,50,19))
        # self.plataform_list.append(Platform(0,570,115,110,18))
        # self.plataform_list.append(Platform(0,740,ANCHO_VENTANA,50,17))


    





