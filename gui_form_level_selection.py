import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget

pass
class FormLevelSelection(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.image_table = Widget(master_form=self,x=200,y=120,w=500,h=500,color_background=None,color_border=None,image_background="my_images/gui/menu/button/table.png",text=None,font=None,font_size=None,font_color=None)
        self.text1 = Widget(master_form=self,x=210,y=165,w=500,h=50,color_background=None,color_border=None,image_background=None,text="SELECT LEVEL",font="8 BIT WONDER NOMINAL",font_size=42,font_color=C_WHITE)
        self.boton1 = Button(master=self,x=260,y=410,w=130,h=130,color_background=None,color_border=None,image_background="my_images/gui/menu/button/1.png",on_click=self.on_click_boton_nivel,on_click_param="level_1",text=None,font=None,font_size=None,font_color=None)
        self.boton2 = Button(master=self,x=390,y=410,w=130,h=130,color_background=None,color_border=None,image_background="my_images/gui/menu/button/2.png",on_click=self.on_click_boton_nivel,on_click_param="level_2",text=None,font=None,font_size=None,font_color=None)
        self.boton3 = Button(master=self,x=520,y=408,w=130,h=130,color_background=None,color_border=None,image_background="my_images/gui/menu/button/3.png",on_click=self.on_click_boton_nivel,on_click_param="level_3",text=None,font=None,font_size=None,font_color=None)
        #name="level_selection",master_surface=screen,x=200,y=120,w=500,h=500,color_background=None,imagen_background="my_images/gui/menu/button/table.png",color_border=None,active=False)

        self.lista_widget = [self.image_table,self.text1,self.boton1,self.boton2,self.boton3]

    def update(self, lista_eventos,keys,sonidos,delta_ms,timer_1s):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos,keys,delta_ms)
        for evento in lista_eventos:
             if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active("main_menu")

    def on_click_boton_nivel(self,parametro):
        self.forms_dict[parametro].resetear()
        self.set_active(parametro)
        self.forms_dict["pause"].cambiar_nivel(parametro)
        self.forms_dict["win"].cambiar_nivel(parametro)
        self.forms_dict["lose"].cambiar_nivel(parametro)


    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()