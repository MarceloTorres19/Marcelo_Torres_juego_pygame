import pygame,sys
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget

class FormPause(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)
        self.text1 = Widget(master_form=self,x=35,y=25,w=240,h=70,color_background=None,color_border=None,image_background= None,text="PAUSED",font="8 BIT WONDER NOMINAL",font_size=38,font_color=C_WHITE)
        self.boton1 = Button(master=self,x=50,y=115,w=210,h=23,color_background=None,color_border=None,image_background= None,on_click=self.on_click_boton1,on_click_param="level_1",text="RESUME",font="8 BIT WONDER NOMINAL",font_size=23,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=50,y=150,w=210,h=23,color_background=None,color_border=None,image_background= None,on_click=self.on_click_boton1,on_click_param="pause_settings",text="SETTINGS",font="8 BIT WONDER NOMINAL",font_size=23,font_color=C_WHITE)
        self.boton3 = Button(master=self,x=50,y=185,w=210,h=23,color_background=None,color_border=None,image_background= None,on_click=self.on_click_boton1,on_click_param="main_menu",text="MAIN MENU",font="8 BIT WONDER NOMINAL",font_size=23,font_color=C_WHITE)
        self.boton4 = Button(master=self,x=50,y=220,w=210,h=23,color_background=None,color_border=None,image_background= None,on_click=self.exit_game,on_click_param="None",text="EXIT GAME",font="8 BIT WONDER NOMINAL",font_size=23,font_color=C_WHITE)
        
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4,self.text1]

    def on_click_boton1(self, parametro):
       
        self.set_active(parametro)
    
    def on_click_reset(self,parametro):
        self.forms_dict[self.boton1.on_click_param].resetear()
        self.set_active(parametro)
    

    def cambiar_nivel(self,parametro):
        self.boton1.on_click_param = parametro

    def exit_game(self,none):
        sys.exit()

    def update(self, lista_eventos,keys,sonidos,delta_ms,timer_1s):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos,keys,delta_ms)
        for evento in lista_eventos:
             if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active(self.boton1.on_click_param)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()