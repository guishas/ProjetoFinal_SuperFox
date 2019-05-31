# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:11:12 2019

@author: Usuario
"""

from os import path

#Diretorio das imagens
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
fnt_dir = path.join(path.dirname(__file__), 'font')

#Dados gerais do jogo
WIDTH = 800
HEIGHT = 500
FPS = 60

#Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

#Gravidade
gravidade = -0.5

#Estados
PARADO = 0
PULANDO = 1
ANDANDO = 2
NO_PULO = 3
CAINDO = 4
SHOOTING = 5

QUIT = 6
GAME = 7
INIT = 8

DONE = 15