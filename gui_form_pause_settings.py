import pygame
from pygame.locals import *
from gui_form import Form
from gui_widget import Widget
from gui_button import Button
from gui_progressbar import ProgressBar
from constantes import *

class FormPauseSettings(Form):
    
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.text1 = Widget(master_form=self,x=80,y=30,w=150,h=40,color_background=None,color_border=None,image_background=None,text="MUSIC",font="8 BIT WONDER NOMINAL",font_size=25,font_color=C_WHITE)
        self.text2 = Widget(master_form=self,x=80,y=110,w=150,h=40,color_background=None,color_border=None,image_background=None,text="SFX",font="8 BIT WONDER NOMINAL",font_size=25,font_color=C_WHITE)
        self.pb1 = ProgressBar(master=self,x=59,y=75,w=180,h=30,color_background=None,color_border=None,image_background="my_images/gui/menu/button/bar.png",image_progress="my_images/gui/menu/button/bar_botton.png",value=3,value_max=10)
        self.pb2 = ProgressBar(master=self,x=59,y=155,w=180,h=30,color_background=None,color_border=None,image_background="my_images/gui/menu/button/bar.png",image_progress="my_images/gui/menu/button/bar_botton.png",value=3,value_max=10)
        self.boton1 = Button(master=self,x=32,y=80,w=20,h=20,color_background=None,color_border=None,image_background="my_images/gui/menu/button/minus.png",on_click=self.on_click_boton1,on_click_param=None,text=None,font=None,font_size=None,font_color=None)
        self.boton2 = Button(master=self,x=32,y=160,w=20,h=20,color_background=None,color_border=None,image_background="my_images/gui/menu/button/minus.png",on_click=self.on_click_boton2,on_click_param=None,text=None,font=None,font_size=None,font_color=None)
        self.boton3 = Button(master=self,x=246,y=80,w=20,h=20,color_background=None,color_border=None,image_background="my_images/gui/menu/button/plus.png",on_click=self.on_click_boton3,on_click_param=None,text=None,font=None,font_size=None,font_color=None)
        self.boton4 = Button(master=self,x=246,y=160,w=20,h=20,color_background=None,color_border=None,image_background="my_images/gui/menu/button/plus.png",on_click=self.on_click_boton4,on_click_param=None,text=None,font=None,font_size=None,font_color=None)
        self.boton5 = Button(master=self,x=65,y=220,w=180,h=23,color_background=None,color_border=None,image_background= None,on_click=self.on_click_boton5,on_click_param="pause",text="GO BACK",font="8 BIT WONDER NOMINAL",font_size=18,font_color=C_WHITE)
        self.lista_widget = [self.text1,self.text2,self.pb1,self.pb2,self.boton1,self.boton2,self.boton3,self.boton4,self.boton5]

    def on_click_boton1(self, parametro):
        if self.pb1.value > 0:
            self.pb1.value -= 1
    
    def on_click_boton2(self, parametro):
        if self.pb2.value > 0:
            self.pb2.value -= 1
    
    def on_click_boton3(self, parametro):
        if self.pb1.value < self.pb1.value_max:
            self.pb1.value += 1
    
    def on_click_boton4(self, parametro):
        if self.pb2.value < self.pb2.value_max:
            self.pb2.value += 1
        
    def on_click_boton5(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,sonidos,delta_ms,keys,timer_1s):
        pygame.mixer.music.set_volume(self.pb1.value/10)
        
        # for sonido in sonidos:
        #     sonido.set_volume(self.pb2.value/10)
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos,keys,delta_ms)
        for evento in lista_eventos:
             if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active("pause")

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()