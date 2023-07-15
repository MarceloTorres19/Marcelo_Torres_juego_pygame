import pygame
import sys
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_widget import Widget
from gui_button import Button

class FormMainMenu(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.pantalla = master_surface
        self.boton0 = Button(master=self,x=500,y=330,w=350,h=80,color_background=None,color_border=None,image_background=None,on_click=self.on_click_boton1,on_click_param="level_selection",text="PLAY",font="8 BIT WONDER NOMINAL",font_size=60,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=500,y=500,w=350,h=40,color_background=None,color_border=None,image_background=None,on_click=self.on_click_boton1,on_click_param="pause_settings",text="SETTINGS",font="8 BIT WONDER NOMINAL",font_size=30,font_color=C_WHITE)
        self.boton3 = Button(master=self,x=500,y=540,w=350,h=40,color_background=None,color_border=None,image_background=None,on_click=self.on_click_boton1,on_click_param="puntuaciones",text="RANKING",font="8 BIT WONDER NOMINAL",font_size=30,font_color=C_WHITE)
        self.boton4 = Button(master=self,x=500,y=590,w=350,h=40,color_background=None,color_border=None,image_background=None,on_click=self.on_click_boton2,on_click_param=None,text="EXIT",font="8 BIT WONDER NOMINAL",font_size=30,font_color=C_WHITE)
        
        self.lista_widget = [self.boton0,self.boton2,self.boton3,self.boton4]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    
    def on_click_boton2(self, parametro):
        pygame.quit()
        sys.exit()

    def update(self,lista_eventos,keys,sonidos,delta_ms,timer_1s):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos,keys,delta_ms)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()