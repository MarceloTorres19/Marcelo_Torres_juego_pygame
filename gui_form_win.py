from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget

class FormWin(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.text1 = Widget(master_form=self,x=48,y=73,w=600,h=70,color_background=None,color_border=None,image_background= None,text="STAGE CLEAR",font="8 BIT WONDER NOMINAL",font_size=50,font_color=C_WHITE)
        self.boton1 = Button(master=self,x=175,y=200,w=300,h=30,color_background=None,color_border=None,image_background= None,on_click=self.on_click_reset,on_click_param="level_1",text="CONTINUE",font="8 BIT WONDER NOMINAL",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=190,y=270,w=300,h=30,color_background=None,color_border=None,image_background= None,on_click=self.on_click_reset,on_click_param="main_menu",text="MAIN MENU ",font="8 BIT WONDER NOMINAL",font_size=30,font_color=C_WHITE)
        
        self.lista_widget = [self.text1,self.boton1,self.boton2]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    
    def on_click_reset(self,parametro):
        self.forms_dict[self.boton1.on_click_param].resetear()
        self.set_active("level_selection")

    def cambiar_nivel(self,parametro):
    
        self.boton1.on_click_param = parametro
    
    def update(self,event_list,keys,sound_list,delta_ms,timer_1s):
        
        for aux_widget in self.lista_widget:
            aux_widget.update(event_list,keys,delta_ms)
        
    def draw(self): 
        """
        Este metodo se encarga de dibujar los distintos widget en pantalla
        """
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()