from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget

class FormLose(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.text1 = Widget(master_form=self,x=48,y=73,w=600,h=70,color_background=None,color_border=None,image_background= None,text="GAME OVER",font="8 BIT WONDER NOMINAL",font_size=60,font_color=C_WHITE)
        self.text2 = Widget(master_form=self,x=100,y=200,w=500,h=70,color_background=None,color_border=None,image_background= None,text="PLAY AGAIN ",font="8 BIT WONDER NOMINAL",font_size=45,font_color=C_WHITE)
        self.text3 = Widget(master_form=self,x=530,y=210,w=50,h=70,color_background=None,color_border=None,image_background= None,text="?",font="STENCIL",font_size=57,font_color=C_WHITE)
        self.boton1 = Button(master=self,x=220,y=315,w=90,h=30,color_background=None,color_border=None,image_background= None,on_click=self.on_click_reset,on_click_param="level_1",text="YES",font="8 BIT WONDER NOMINAL",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=370,y=315,w=60,h=30,color_background=None,color_border=None,image_background= None,on_click=self.on_click_boton1,on_click_param="main_menu",text="NO",font="8 BIT WONDER NOMINAL",font_size=30,font_color=C_WHITE)        
        self.lista_widget = [self.text1,self.text2,self.text3,self.boton1,self.boton2]

    def on_click_boton1(self, parametro):
       
        self.set_active(parametro)
    
    def on_click_reset(self,parametro):
        self.forms_dict[self.boton1.on_click_param].resetear()
        self.set_active(parametro)

    def cambiar_nivel(self,parametro):
        self.boton1.on_click_param = parametro

    def update(self, lista_eventos,sonidos,delta_ms,keys,timer_1s):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos,delta_ms,keys)
    
    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()