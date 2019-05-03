#Bibliotecas e importações
import pygame
import time
from os import path
import random
from config import WIDTH, HEIGHT, FPS

#Inicializacao do pygame
pygame.init()
pygame.mixer.init()

#Tamanho da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Nome do jogo
pygame.display.set_caption("SuperFox by TeamAura")

