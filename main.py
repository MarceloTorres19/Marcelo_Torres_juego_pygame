# from curses import KEY_DOWN, KEY_LEFT, KEY_RIGHT
import pygame

from constantes import *
from player import Player
from plataforma import Platform
from enemigo import Enemy
from proyectil import Bullet
from botin import Loot


screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

# imagen_fondo = pygame.image.load("my_images/locations/stage1.png")
imagen_fondo = pygame.image.load("my_images/locations/stage1.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))


player_1 = Player(x=0,y=400,speed_walk=6,speed_run=10,gravity=15,jump_power=40,frame_rate_ms=35,move_rate_ms=33,jump_height=120, p_scale = 3.2)

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
        # if event.type == pygame.MOUSEBUTTONDOWN:0
        #      print(event)
            
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

    player_1.events(delta_ms,keys,enemy_list,lista_plataformas)
    player_1.update(delta_ms,lista_plataformas,enemy_list)
    player_1.draw(screen)

    pygame.display.flip()
    
pygame.quit()



    





