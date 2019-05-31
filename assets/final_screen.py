# -*- coding: utf-8 -*-
"""
Created on Fri May 31 07:43:06 2019

@author: Usuario
"""

from config import QUIT, GAME, BLACK, FPS, WIDTH, HEIGHT
import pygame

def final_screen(screen, assets):
    
    clock = pygame.time.Clock()
    
    final = assets['tela_final']
    final_rect = final.get_rect()
    final = pygame.transform.scale(final, (WIDTH, HEIGHT))
    
    pygame.event.get()
    
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
        screen.blit(final, final_rect)
        
        pygame.display.flip()
        
    return state