import pygame
from pygame.locals import *
from constantes import *
from nivel import Nivel
from gui_form import Form
from gui_progressbar import ProgressBar
from gui_widget import Widget

pass
class FormNivel(Form):
    """
    Formulario que maneja el nivel, dependiendo de cual se cargue
    """
    def __init__(self, name, master_surface, x=0, y=0, w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=None, color_border=None, active=False):
        self.nombre_jugador = "PLAYER"
        self.name = name
        self.nivel_actual = Nivel(self.name,master_surface)
        self.tiempo_juego = self.nivel_actual.tiempo_juego
        imagen_background = self.nivel_actual.fondo
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        self.text1 = Widget(master=self,x=-100,y=-10,w=1400,h=60,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\bar.png",text=None,font=None,font_size=None,font_color=None)
        self.text2 = Widget(master=self,x=550,y=10,w=100,h=30,color_background=None,color_border=None,image_background=None,text="{0}".format(self.tiempo_juego),font="8 BIT WONDER NOMINAL",font_size=19,font_color=WHITE)
        self.text3 = Widget(master=self,x=1000,y=10,w=200,h=30,color_background=None,color_border=None,image_background=None,text="{0}".format(self.nivel_actual.puntuacion),font="8 BIT WONDER NOMINAL",font_size=19,font_color=WHITE)
        self.ima1 = Widget(master=self,x=510,y=10,w=30,h=30,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Clock_Icon.png",text=None,font=None,font_size=None,font_color=None)
        self.ima2 = Widget(master=self,x=50,y=10,w=30,h=30,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\HP_Icon.png",text=None,font=None,font_size=None,font_color=None)
        self.ima3 = Widget(master=self,x=960,y=10,w=30,h=30,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Shop_Cristal_Icon_01.png",text=None,font=None,font_size=None,font_color=None)
        self.pb1 = ProgressBar(master=self,x=100,y=15,w=100,h=20,color_background=None,color_border=None,image_background=None,image_progress=CORAZON,value=self.nivel_actual.jugador.vidas,value_max=5)

        self.puntuacion_nivel = 0
        self.entrar = False
        self.perder = False

        self.lista_widget = [self.text1,self.text2,self.text3,self.pb1,self.ima1,self.ima2,self.ima3]

        
    def resetear(self):
        """
        Este metodo se encarga de crear nuevamente el formulario, con los mismos atributos
        """
        self.__init__(name = self.name, master_surface = self.master_surface)

    def update(self, lista_eventos, teclas, delta_ms, tiempo, sonidos):
        """
        Este metodo se encarga de actualizar el nivel actual, las colisiones y el jugador
        Tambien ingresar la puntacion del jugador al terminar el nivel a la base de datos
        Y por ultimo actualizar los distintos widget

        Parametros: una lista de eventos, teclas, sonidos y un valor delta_ms y un evento de usario de tiempo
        """
        self.nivel_actual.update(delta_ms,sonidos)
        self.nivel_actual.colisiones(delta_ms,sonidos)
        self.nivel_actual.jugador.update(delta_ms,self.nivel_actual.pantalla,teclas,lista_eventos,self.nivel_actual.tiles,self.nivel_actual.obstaculos,self.nivel_actual.plataformas,sonidos)

        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active("pausa")
                if evento.key == pygame.K_UP:
                    self.entrar = True
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_UP:
                    self.entrar = False
           
            if evento.type == tiempo:
                self.tiempo_juego -= 1
        
        if self.nivel_actual.jugador.ganar and self.entrar:
            self.set_active("you_win")
            pygame.mixer.Sound.play(sonidos[5])
            self.puntuacion_nivel = self.nivel_actual.puntuacion
            if self.name == "nivel_1":
                insertar_linea(self.nombre_jugador,"nivel_1", self.puntuacion_nivel)
            if self.name == "nivel_2":
                insertar_linea(self.nombre_jugador,"nivel_2", self.puntuacion_nivel)
            if self.name == "nivel_3":
                insertar_linea(self.nombre_jugador,"nivel_3", self.puntuacion_nivel)
            if self.name == "nivel_4":
                insertar_linea(self.nombre_jugador,"nivel_4", self.puntuacion_nivel)

        if not self.nivel_actual.jugador.vivo or self.perder:
            self.set_active("you_lose")

        self.text3._text = "{0}".format(self.nivel_actual.puntuacion).zfill(8)
        self.pb1.value = self.nivel_actual.jugador.vidas
        if self.tiempo_juego >= 0:
            self.text2._text = "{0}".format(self.tiempo_juego)
        else:
            self.perder = True
        
   
        
    def draw(self): 
        """
        Este metodo se encarga de dibujar todo lo relacionado al nivel, y al jugadoor
        Tambien los distintos tipos de widget y obstaculos
        """
        super().draw()
        self.nivel_actual.draw()
        self.nivel_actual.jugador.draw(self.nivel_actual.pantalla)
        for obstaculo in self.nivel_actual.obstaculos:
            obstaculo.draw(self.nivel_actual.pantalla)
        for aux_widget in self.lista_widget:    
            aux_widget.draw()
        


        