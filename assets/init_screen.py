# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:59:25 2019

@author: Usuario
"""

from config import QUIT, GAME, BLACK, FPS
import pygame



def init_screen(screen, assets_img, assets_snd, assets_fnt):
    
    clock = pygame.time.Clock()
    
    inicio = assets_img['tela_inicial']
    inicio_rect = inicio.get_rect()
    
    running = True
    while running:
        
        clock.tick(FPS)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            
            if event.type == pygame.KEYUP:
                state = GAME
                running = False
            
        screen.fill(BLACK)
        screen.blit(inicio, inicio_rect)
        
        pygame.display.flip()
        
    return state
    