#Bibliotecas e importações
import pygame
from os import path

#Diretorio das imagens
img_dir = path.join(path.dirname(__file__), 'img')

#Dados gerais do jogo
WIDTH = 800
HEIGHT = 500
FPS = 60

#Cores
BLACK = (0, 0, 0)


#Classe jogador que representa a raposa
class Player(pygame.sprite.Sprite):
    
    #Construtor da classe
    def __init__(self):
        
        #Construtor da classe pai
        pygame.sprite.Sprite.__init__(self)
        
        #Imagem do player
        player_img = pygame.image.load(path.join(img_dir, 'fox_static.png')).convert()
        self.image = player_img
        
        #Diminuindo o tamanho da imagem
        self.image = pygame.transform.scale(player_img, (70, 58))
        
        #Deixando transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhes sobre posicionamento
        self.rect = self.image.get_rect()
        
        #Posicao
        self.rect.x = 20
        self.rect.bottom = HEIGHT - 80
        
        #Velocidade
        self.speedx = 0
    
    def update(self):
        self.rect.x += self.speedx
        
        #Mantém dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    
<<<<<<< HEAD
        
=======

>>>>>>> c1c383203baeb0b312f354e59f6873ba56e996ec
class BlocoTijolo(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
        #Imagem
        brick_img = pygame.image.load(path.join(img_dir, 'bloco_tijolo.png')).convert()
        self.image = brick_img
        
        #Diminuindo a imagem
        self.image = pygame.transform.scale(brick_img, (40, 40))
        
        #Imagem transparente
        self.image.set_colorkey(BLACK)
        
        #Posicionamento
        self.rect = self.image.get_rect()
        
        #posicao
        self.rect.x = 100
        self.rect.y = 250
        
        self.radius = 25
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
background = pygame.transform.scale(background, (800, 500))
background_rect = background.get_rect()

#Carrega os sons do jogo

#Cria um player
player = Player()

#Cria um bloco de tijolo
bloco = BlocoTijolo()

#Grupo sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(bloco)

#Grupo mobs
mobs = pygame.sprite.Group()

#comando para evitar travamentos
try:
    
    #Loop principal
    running = True
    
    while running:
        
        #Ajusta o tick do jogo
        clock.tick(FPS)
        
        #Eventos pygame
        for event in pygame.event.get():
            
            #verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
                
            #verifica se apertou alguma tecla
            elif event.type == pygame.KEYDOWN:
                #se apertou alguma tecla muda a velocidade
                if event.key == pygame.K_LEFT:
                    player.speedx -= 6
                if event.key == pygame.K_RIGHT:
                    player.speedx += 6
                    
            #verifica se soltou alguma tecla
            elif event.type == pygame.KEYUP:
                #se soltou muda a velocidade
                if event.key == pygame.K_LEFT:
                    player.speedx += 6
                if event.key == pygame.K_RIGHT:
                    player.speedx -= 6
                
        #Atualiza os sprites
        all_sprites.update()
        
        #A cada loop redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        #Depois de desenhar tudo inverte o display
        pygame.display.flip()
finally:
    pygame.quit()
        
        
        
        
        