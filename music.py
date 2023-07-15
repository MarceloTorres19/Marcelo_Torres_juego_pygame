import pygame

# AGREGAR MUSICA

class Music:
    def __init__(self) -> None:
        self.muerte = pygame.mixer.Sound("sounds/sfx/self_hitted_2.wav")
        self.shoot = pygame.mixer.Sound("sounds/sfx/shoot.wav")
        self.pick_up = pygame.mixer.Sound("sounds/sfx/pick_up.wav")
        self.select = pygame.mixer.Sound("sounds/sfx/select.wav")
        self.bounce = pygame.mixer.Sound("sounds/sfx/bounce.wav")
        self.jump = pygame.mixer.Sound("sounds/sfx/jump.wav")
        self.power_up = pygame.mixer.Sound("sounds/sfx/power_up.wav")
        self.game_over = pygame.mixer.Sound("sounds/sfx/18 - Game Over.mp3")
        self.enemy_hitted = pygame.mixer.Sound("sounds/sfx/enemy_hitted.wav")
        self.enemy_hitted_ball = pygame.mixer.Sound("sounds/sfx/crash.wav")
        self.sound_list= [self.shoot,self.select,self.pick_up,self.jump,self.enemy_hitted,self.game_over,self.power_up,self.bounce,self.muerte,self.enemy_hitted_ball]
        for sound in self.sound_list:
            sound.set_volume(0.3)
            

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/tracks/01 - Title Theme.mp3")
        pygame.mixer.music.queue('sounds/tracks/07 - Stage Theme 3.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)