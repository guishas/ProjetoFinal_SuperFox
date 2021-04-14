
#Bibliotecas e importações
import pygame
from os import path
from config import img_dir, snd_dir, fnt_dir, WIDTH, HEIGHT, BLACK, QUIT, GAME, INIT, DONE
from init_screen import init_screen
from game_screen import game_screen        
from final_screen import final_screen
 
#função assets (imagens e sons)

def load_assets_img(img_dir):
    assets_img = {}
    assets_img['player_img'] = pygame.image.load(path.join(img_dir, 'fox_static.png')).convert()
    assets_img['bloco_tijolo'] = pygame.image.load(path.join(img_dir, 'bloco_tijolo.png')).convert()
    assets_img['bloco_item'] = pygame.image.load(path.join(img_dir, 'bloco_item.png')).convert()
    assets_img['background'] = pygame.image.load(path.join(img_dir, 'bg_fase1.png')).convert()
    fox_walk = []
    for i in range(1, 3, 1):
        filename = 'fox_walk{}.png'.format(i)
        walk = pygame.image.load(path.join(img_dir, filename)).convert()
        walk = pygame.transform.scale(walk, (48, 60))
        walk.set_colorkey(BLACK)
        fox_walk.append(walk)
    assets_img['fox_walk'] = fox_walk
    assets_img['pipe_img'] = pygame.image.load(path.join(img_dir, 'pipes_fase1.png')).convert()
    assets_img['bloco_usado'] = pygame.image.load(path.join(img_dir, 'bloco_usado.png')).convert()
    assets_img['fox_jump'] = pygame.image.load(path.join(img_dir, 'fox_jump.png')).convert()
    mob_walk = []
    for i in range(1, 3, 1):
        filename = 'mob_walk{}.png'.format(i)
        mobwalk = pygame.image.load(path.join(img_dir, filename)).convert()
        mobwalk = pygame.transform.scale(mobwalk, (80, 68))
        mobwalk.set_colorkey(BLACK)
        mob_walk.append(mobwalk)
    assets_img['mob_walk'] = mob_walk
    assets_img['fireball'] = pygame.image.load(path.join(img_dir, 'fireball.png')).convert()
    explosion_anim = []
    for i in range(9):
        filename = 'regularExplosion0{}.png'.format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert()
        img = pygame.transform.scale(img, (32, 32))
        img.set_colorkey(BLACK)
        explosion_anim.append(img)
    assets_img['explosion_anim'] = explosion_anim
    assets_img['fox_life'] = pygame.image.load(path.join(img_dir, 'fox_healthpoint.png')).convert()
    mob_fly = []
    for i in range(1, 3, 1):
        filename = 'mob2_fly{}.png'.format(i)
        mobfly = pygame.image.load(path.join(img_dir, filename)).convert()
        mobfly = pygame.transform.scale(mobfly, (80, 68))
        mobfly.set_colorkey(BLACK)
        mob_fly.append(mobfly)
    assets_img['mob_fly'] = mob_fly
    assets_img['tela_inicial'] = pygame.image.load(path.join(img_dir, 'tela_inicial.png')).convert()
    assets_img['tela_final'] = pygame.image.load(path.join(img_dir, 'tela_final.png')).convert()
    return assets_img

def load_assets_snd(snd_dir):
    assets_snd = {}
    assets_snd['jump_sound'] = pygame.mixer.Sound(path.join(snd_dir, 'jump_sound.wav'))
    assets_snd['music_sound'] = pygame.mixer.Sound(path.join(snd_dir, 'music_sound.ogg'))
    assets_snd['fireball_sound'] = pygame.mixer.Sound(path.join(snd_dir, 'fireball_sound.wav'))
    assets_snd['death_sound'] = pygame.mixer.Sound(path.join(snd_dir, 'death_sound.wav'))
    assets_snd['destruction_sound'] = pygame.mixer.Sound(path.join(snd_dir, 'expl6.wav'))
    return assets_snd

def load_assets_fnt(fnt_dir):
    assets_fnt = {}
    assets_fnt['score_font'] = pygame.font.Font(path.join(fnt_dir, 'PressStart2P.ttf'), 28)
    return assets_fnt


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("SuperFox by TeamAura")

assets_img = load_assets_img(img_dir)
assets_snd = load_assets_snd(snd_dir)
assets_fnt = load_assets_fnt(fnt_dir)

try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = init_screen(screen, assets_img, assets_snd, assets_fnt)
        elif state == GAME:
            state = game_screen(screen, assets_img, assets_snd, assets_fnt)
        elif state == DONE:
            state = final_screen(screen, assets_img, assets_snd, assets_fnt)
        else:
            state = QUIT

finally:
    pygame.quit()
    