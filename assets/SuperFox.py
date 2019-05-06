#Bibliotecas e importações
import pygame
from os import path
from config import WIDTH, HEIGHT, FPS, BLACK

#Diretorio das imagens
img_dir = path.join(path.dirname(__file__), 'img')

#Inicializacao do pygame
pygame.init()
pygame.mixer.init()

#Tamanho da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Nome do jogo
pygame.display.set_caption("SuperFox by TeamAura")

#Ajuste de velocidade
clock = pygame.time.Clock()
    
#Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'bg_fase1.png')).convert()
background_rect = background.get_rect()
    
#Carrega os sons do jogo

#comando para evitar travamentos
try:
    
    #Loop principal
    running = False
    
    while running:
        
        #Ajusta o tick do jogo
        clock.tick(FPS)
        
        #Eventos pygame
        for event in pygame.event.get():
            #verifica se foi fechado
            if event.type == pygame.QUIT:
                running = True
        
        #A cada loop redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        
        #Depois de desenhar tudo inverte o display
        pygame.display.flip()
finally:
    pygame.quit()
        
        
        
        
        