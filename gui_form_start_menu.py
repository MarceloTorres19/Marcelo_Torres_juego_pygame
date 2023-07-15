import pygame
from pygame.locals import *
from gui_form import Form
from gui_widget import Widget
from gui_button import Button
from gui_progressbar import ProgressBar
from constantes import *

class FormStartMenu(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)
        self.image = Widget(master_form=self,x=0,y=0,w=ANCHO_VENTANA,h=721,color_background=None,color_border=None,image_background="my_images/gui/menu/menuprincipal.jpg",text=None,font=None,font_size=None,font_color=None)
        self.text1= Widget(master_form=self,x=220,y=730,w=500,h=40,color_background=None,color_border=None,image_background=None,text="PRESS SPACE TO START",font="8 BIT WONDER NOMINAL",font_size=25,font_color=C_WHITE)
       
        self.lista_widget = [self.image ,self.text1]
        

    def update(self, lista_eventos,sonidos,delta_ms,keys,timer_1s):
    
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos,keys,delta_ms)
        for evento in lista_eventos:
             if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    self.set_active("main_menu")

    def draw(self): 
        """
        Este metodo se encarga de dibujar los distintos widget en pantalla
        """
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()