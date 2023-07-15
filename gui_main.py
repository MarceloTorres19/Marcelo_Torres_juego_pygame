import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form import Form
from gui_form_level import FormGameLevel
from gui_form_pause import FormPause
from gui_form_pause_settings import FormPauseSettings
from gui_form_lose import FormLose
from gui_form_win import FormWin
from gui_form_start_menu import FormStartMenu
from gui_form_main_menu import FormMainMenu
from gui_form_level_selection import FormLevelSelection
from music import Music

flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

timer_1s = pygame.USEREVENT + 0
pygame.time.set_timer(timer_1s,1000)

music = Music()
music.play_music()

level_1 = FormGameLevel(name="level_1",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,0,0),imagen_background= None,color_border=(255,0,255),active=False)
level_2 = FormGameLevel(name="level_2",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,0,0),imagen_background= None,color_border=(255,0,255),active=False)
level_3 = FormGameLevel(name="level_3",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,0,0),imagen_background= None,color_border=(255,0,255),active=False)
form_pause = FormPause(name="pause",master_surface = screen,x=300,y=230,w=300,h=300,imagen_background="my_images/gui/menu/button/Window.png",color_background=None ,color_border=C_BLACK,active=False)
form_pause_settings = FormPauseSettings(name="pause_settings",master_surface =screen,x=300,y=230,w=300,h=300,imagen_background="my_images/gui/menu/button/Window.png",color_background=None ,color_border=C_BLACK,active=False)
form_pause_settings_menu = FormPauseSettings(name="pause_settings_menu",master_surface =screen,x=300,y=230,w=300,h=300,imagen_background="my_images/gui/menu/button/Window.png",color_background=None ,color_border=C_BLACK,active=False,main_menu=True)
form_lose= FormLose(name="lose",master_surface = screen,x=100,y=155,w=680,h=500,imagen_background="my_images/gui/menu/button/Window.png",color_background=None ,color_border=C_BLACK,active=False)
form_win= FormWin(name="win",master_surface = screen,x=100,y=155,w=680,h=400,imagen_background="my_images/gui/menu/button/Window.png",color_background=None ,color_border=C_BLACK,active=False)
start_menu = FormStartMenu(name="start_menu",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,0,0),imagen_background= None,color_border=(255,0,255),active=True)
main_menu = FormMainMenu(name="main_menu",master_surface=screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,0,0),imagen_background="my_images/gui/menu/main_menu.png",color_border=None,active=False)
level_selection = FormLevelSelection(name="level_selection",master_surface=screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=None,imagen_background="my_images/gui/menu/button/background_snow.png",color_border=None,active=False)

running =True
while running:     
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    aux_form_active = Form.get_active()
    if(aux_form_active != None):
        aux_form_active.update(event_list,keys,music.sound_list,delta_ms,timer_1s)
        aux_form_active.draw()

    pygame.display.flip()




    


  



