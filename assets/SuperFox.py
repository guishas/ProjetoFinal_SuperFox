#Bibliotecas e importações
import pygame
from os import path
from config import img_dir, snd_dir, fnt_dir, WIDTH, HEIGHT, FPS, BLACK, WHITE, YELLOW, gravidade, PARADO, PULANDO, ANDANDO, NO_PULO, CAINDO, SHOOTING, QUIT, GAME, INIT
from init_screen import init_screen
from game_screen import game_screen        
            
#função assets (imagens e sons)
def load_assets(img_dir, snd_dir, fnt_dir):
    assets = {}
    assets['player_img'] = pygame.image.load(path.join(img_dir, 'fox_static.png')).convert()
    assets['bloco_tijolo'] = pygame.image.load(path.join(img_dir, 'bloco_tijolo.png')).convert()
    assets['bloco_item'] = pygame.image.load(path.join(img_dir, 'bloco_item.png')).convert()
    assets['background'] = pygame.image.load(path.join(img_dir, 'bg_fase1.png')).convert()
    fox_walk = []
    for i in range(1, 3, 1):
        filename = 'fox_walk{}.png'.format(i)
        walk = pygame.image.load(path.join(img_dir, filename)).convert()
        walk = pygame.transform.scale(walk, (70, 58))
        walk.set_colorkey(BLACK)
        fox_walk.append(walk)
    assets['fox_walk'] = fox_walk
    assets['pipe_img'] = pygame.image.load(path.join(img_dir, 'pipes_fase1.png')).convert()
    assets['bloco_usado'] = pygame.image.load(path.join(img_dir, 'bloco_usado.png')).convert()
    assets['jump_sound'] = pygame.mixer.Sound(path.join(snd_dir, 'jump_sound.wav'))
    assets['music_sound'] = pygame.mixer.Sound(path.join(snd_dir, 'music_sound.ogg'))
    assets['fox_jump'] = pygame.image.load(path.join(img_dir, 'fox_jump.png')).convert()
    mob_walk = []
    for i in range(1, 3, 1):
        filename = 'mob_walk{}.png'.format(i)
        mobwalk = pygame.image.load(path.join(img_dir, filename)).convert()
        mobwalk = pygame.transform.scale(mobwalk, (80, 68))
        mobwalk.set_colorkey(BLACK)
        mob_walk.append(mobwalk)
    assets['mob_walk'] = mob_walk
    assets['fireball'] = pygame.image.load(path.join(img_dir, 'fireball.png')).convert()
    assets['fireball_sound'] = pygame.mixer.Sound(path.join(snd_dir, 'fireball_sound.wav'))
    assets['death_sound'] = pygame.mixer.Sound(path.join(snd_dir, 'death_sound.wav'))
    explosion_anim = []
    for i in range(9):
        filename = 'regularExplosion0{}.png'.format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert()
        img = pygame.transform.scale(img, (32, 32))
        img.set_colorkey(BLACK)
        explosion_anim.append(img)
    assets['explosion_anim'] = explosion_anim
    assets['destruction_sound'] = pygame.mixer.Sound(path.join(snd_dir, 'expl6.wav'))
    assets['score_font'] = pygame.font.Font(path.join(fnt_dir, 'PressStart2P.ttf'), 28)
    assets['fox_life'] = pygame.image.load(path.join(img_dir, 'fox_healthpoint.png')).convert()
    mob_fly = []
    for i in range(1, 3, 1):
        filename = 'mob2_fly{}.png'.format(i)
        mobfly = pygame.image.load(path.join(img_dir, filename)).convert()
        mobfly = pygame.transform.scale(mobfly, (80, 68))
        mobfly.set_colorkey(BLACK)
        mob_fly.append(mobfly)
    assets['mob_fly'] = mob_fly
    assets['tela_inicial'] = pygame.image.load(path.join(img_dir, 'tela_inicial.png')).convert()
    return assets

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("SuperFox by TeamAura")

assets = load_assets(img_dir, snd_dir, fnt_dir)

try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = init_screen(screen, assets)
        elif state == GAME:
            state = game_screen(screen, assets)
        else:
            state = QUIT

finally:
    pygame.quit()
    