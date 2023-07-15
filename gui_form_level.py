import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_widget import Widget
from gui_progressbar import ProgressBar
from player import Player
from enemy import Enemy
from plataforma import Platform
from background import Background
from bullet import Bullet
from loot import Loot
import json
from auxiliar import Auxiliar

class FormGameLevel(Form):
    def __init__(self,name,master_surface,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=None,imagen_background=None,color_border=None,active=False):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)
        self.name = name
        self.master_surface = master_surface
        self.dicc_level = Auxiliar.cargar_nivel("levels.json",name)
        self.player_1 = self.player_instantiation()
        self.game_time = 60
        self.extra_time = 0
        # --- GUI WIDGET --- 
        self.text1 = Widget(master_form=self,x=10,y=10,w=200,h=40,color_background=None,color_border=None,image_background=None,text="1P      {0}".format(self.player_1.lives),font="8 BIT WONDER NOMINAL",font_size=29,font_color=C_WHITE)
        self.text1_image = Widget(master_form=self,x=110,y=10,w=35,h=40,color_background=None,color_border=None,image_background="my_images/others/blocks/(5).png",text=None,font=None,font_size=None,font_color=None)
        self.text2 = Widget(master_form=self,x=250,y=10,w=400,h=40,color_background=None,color_border=None,image_background=None,text="SCORE  {0}".format(str(self.player_1.score).zfill(6)),font="8 BIT WONDER NOMINAL",font_size=29,font_color=C_WHITE)
        self.text3 = Widget(master_form=self,x=640,y=10,w=270,h=40,color_background=None,color_border=None,image_background=None,text="TIME  {0}".format(self.game_time),font="8 BIT WONDER NOMINAL",font_size=29,font_color=C_WHITE)
        self.background = Widget(master_form=self,x=0,y=0,w=ANCHO_VENTANA,h=60,color_background=C_BLACK,color_border=None,image_background=None,text=None,font=None,font_size=None,font_color=None)
        self.widget_list = [self.background,self.text1_image,self.text1,self.text2,self.text3]

        # --- GAME ELEMENTS --- 
        self.static_background = Background(x=0,y=55,width=w,height=h-60,path=self.dicc_level["background"])
        self.loot_list = self.player_1.loot_list
        self.enemy_list = self.enemies_instantiation()
        self.plataform_list = self.platform_instantiation()
        
        self.bullet_list =self.player_1.municiones

    def resetear(self):
        """
        Este metodo se encarga de crear nuevamente el formulario, con los mismos atributos
        """
        self.__init__(name = self.name, master_surface = self.master_surface)

    def player_instantiation(self):
            for pos in self.dicc_level["player"]["pos"]:
                x = pos[0]
                y = pos[1]
                jugador = Player(x,y)
                return jugador     
            
    def enemies_instantiation(self):
        """
        Este método se encarga de crear a los enemigos

        Retorna: una lista de objetos de enemigos
        """
        aux_enemy_list = []
        for enemy in self.dicc_level["enemies"]:
            position = enemy["pos"]
            x = position[0][0]
            y = position[0][1]
            id = enemy["id"]
            enemy_obj = Enemy(x, y,id)
            aux_enemy_list.append(enemy_obj)
        return aux_enemy_list
    
            
    def platform_instantiation(self):
        """
        Este método se encarga de instanciar a las plataformas

        Retorna: una lista de plataformas
        """
        aux_platform_list = []
        for plataforma in self.dicc_level["platforms"]:
            pos = plataforma["pos"]
            w = plataforma["w"]
            h = plataforma["h"]
            type = plataforma["type"]
            aux_platform_object = Platform(pos[0][0],pos[0][1],w,h,type)
            aux_platform_list.append(aux_platform_object)
        return aux_platform_list
    
    def win_condition(self,delta_ms):
        if len(self.enemy_list) ==0:
            self.extra_time +=delta_ms
        if self.extra_time > 4000:
            self.set_active("win")

    def update(self, event_list,keys,sound_list,delta_ms,timer_1s):

        self.win_condition(delta_ms)

        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.set_active("pause")
            if event.type == timer_1s and len(self.enemy_list) >0:
                self.game_time -= 1
        
        if self.game_time >= 0:
            self.text3._text = "TIME  {0}".format(self.game_time)
        else:
            self.set_active("lose")


        for aux_widget in self.widget_list:
            aux_widget.update(event_list,keys,delta_ms)

        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1) 
            if abs(bullet_element.x_init -bullet_element.x) > bullet_element.reach:
                self.bullet_list.remove(bullet_element)
                del bullet_element

        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms,self.plataform_list,self.bullet_list,self.player_1,self.enemy_list,sound_list)
        
        for loot in self.loot_list:
            loot.update(delta_ms)

        if self.player_1.lives <0:
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(sound_list[GAME_OVER])
            self.set_active("lose")

        self.text1._text="1P      {0}".format(self.player_1.lives)
        self.text2._text="SCORE  {0}".format(str(self.player_1.score).zfill(6))

        self.player_1.events(delta_ms,keys,self.enemy_list,self.plataform_list,sound_list)
        self.player_1.update(delta_ms,self.plataform_list,self.enemy_list,sound_list)

    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)


        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)

        for loot in self.loot_list:
            loot.draw(self.surface)

        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface) 
        self.player_1.draw(self.surface)


        for aux_widget in self.widget_list:    
            aux_widget.draw()