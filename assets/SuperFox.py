#Bibliotecas e importações
import pygame
from os import path
import random
import time

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

#Classe jogador que representa a raposa
class Player(pygame.sprite.Sprite):
    
    #Construtor da classe
    def __init__(self, player_img, fox_walk, fox_jump):
        
        #Construtor da classe pai
        pygame.sprite.Sprite.__init__(self)
        
        #Imagem do player
        self.image = player_img
        self.walking = fox_walk
        self.pulando = fox_jump
        
        self.pulando = pygame.transform.scale(fox_jump, (70, 58))
        self.pulando.set_colorkey(BLACK)
        
        #Diminuindo o tamanho da imagem
        self.image = pygame.transform.scale(player_img, (70, 58))
        
        #Deixando transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhes sobre posicionamento
        self.rect = self.image.get_rect()
        
        #Posicao
        self.rect.x = 20
        self.rect.bottom = HEIGHT - 80
        
        #Estado do jogador
        self.state = PARADO
        
        self.animation = fox_walk
        
        #Velocidade
        self.speedx = 0
        self.speedy = 0
        
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        
        self.frame_ticks = 200
        
        self.parado = self.image
    
    def update(self):
        self.rect.x += self.speedx
        self.speedy -= gravidade
        self.rect.y += self.speedy
        
        #Mantém dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.y < 0:
            self.rect.y = 0

        if self.rect.bottom > HEIGHT - 80:
            self.rect.bottom = HEIGHT -80
            self.speedy = 0
            
        if self.rect.top < 0:
            self.rect.top = 0
            
        #Verifica o pulo, e muda imagem
        if self.speedy < 0:
            self.state = PULANDO
        
        #Define as colisões
        colisoes = pygame.sprite.spritecollide(self, blocos, False, pygame.sprite.collide_mask)
        
        #Bota a posição do personagem para antes da colisão
        for colisao in colisoes:
            #Indo para baixo
            if self.speedy > 0:
                self.rect.bottom = colisao.rect.top
                #Se colidiu, para de cair
                self.speedy = 0

            #Indo para cima 
            elif self.speedy < 0:
                self.rect.top = colisao.rect.bottom
                #Se colidiu, para de cair
                self.speedy = 0
        
        if self.state == ANDANDO:    
            #verifica o tick atual
            now = pygame.time.get_ticks()
        
            elapsed_ticks = now - self.last_update
        
            if elapsed_ticks > self.frame_ticks:
            
                self.last_update = now
            
                center = self.rect.center
                self.image = self.animation[self.frame]
                
                self.frame += 1
                
                if self.frame == len(self.animation):
                    self.frame = 0
                    
                self.rect = self.image.get_rect()
                self.rect.center = center
        
        elif self.state == PULANDO:
            self.image = self.pulando
            self.state = NO_PULO
                
        else:
            self.image = self.parado
            self.state = PARADO
        self.mask = pygame.mask.from_surface(self.image)
                
    #Classe de pulo
    def jump(self):
 
        self.speedy -= gravidade
        self.rect.y += self.speedy
    
class Mob(pygame.sprite.Sprite):
    
    def __init__(self, mob_walk):
        
        pygame.sprite.Sprite.__init__(self)
        
        #imagem
        self.animation = mob_walk
        
        self.image = pygame.image.load(path.join(img_dir, 'fox_static.png')).convert()
        
        teste = self.image
        
        self.image = pygame.transform.scale(teste, (70, 58))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randrange(860, 900)
        self.rect.bottom = HEIGHT - 85
        
        self.speedx = random.randrange(-5, -2)
        
        self.frame = 0
   
        self.last_update = pygame.time.get_ticks()
        
        self.frame_ticks = 200
    
    def update(self):
        
        self.rect.x += self.speedx
        
        now = pygame.time.get_ticks()
        
        elapsed_ticks = now - self.last_update
        
        if elapsed_ticks > self.frame_ticks:
            
            self.last_update = now
            
            center = self.rect.center
            self.image = self.animation[self.frame]
                
            self.frame += 1
                
            if self.frame == len(self.animation):
                self.frame = 0
                    
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.center = center
        
        if self.rect.x < 0:
            self.kill()
            for i in range(2):
                mob = Mob(assets['mob_walk'])
                all_sprites.add(mob)
                mobs.add(mob)
            
class Pipes(pygame.sprite.Sprite):
    
    def __init__(self, pipe_img):
        
        pygame.sprite.Sprite.__init__(self)
        
        #imagem
        self.image = pipe_img
        
        self.image = pygame.transform.scale(pipe_img, (70, 60))
        
        self.image = pygame.transform.rotate(self.image, 90)
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = 740
        self.rect.y = HEIGHT - 150

class BlocoTijolo(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        
        pygame.sprite.Sprite.__init__(self)
        
        #Imagem
        brick_img = assets['bloco_tijolo']
        self.image = brick_img
        
        #Diminuindo a imagem
        self.image = pygame.transform.scale(brick_img, (40, 40))
        
        #Imagem transparente
        self.image.set_colorkey(BLACK)
        
        #Posicionamento
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        
        #posicao
        self.rect.x = x
        self.rect.y = y
        
listaPosicaoBlocos=[(100, 250), (140, 250), (180, 250),(260, 250),(220, 110),(260, 110),(340, 110),(380, 110),(380, 250),(420, 250),(460, 250),(500, 250),(540, 250)]

class BlocoAmarelo(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        
        pygame.sprite.Sprite.__init__(self)
        
        #imagem
        blocoItem_img = assets['bloco_item']
        self.image = blocoItem_img
        
        self.image = pygame.transform.scale(blocoItem_img, (40, 40))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        
        #posicao
        self.rect.x = x
        self.rect.y = y
        
listaPosicaoBlocosAmarelos=[(220, 250),(300, 110)]

class BlocoUsado(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        
        pygame.sprite.Sprite.__init__(self)
        
        blocoUsado_img = assets['bloco_usado']
        self.image = blocoUsado_img
        
        self.image = pygame.transform.scale(blocoUsado_img, (40, 40))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect.x = x
        self.rect.y = y

class Fireball(pygame.sprite.Sprite):
    
    def __init__(self, fireball, x, y):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = fireball
        
        self.image.set_colorkey(BLACK)
        
        self.image = pygame.transform.scale(fireball, (35, 30))
        
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.speedx = 7
        
        self.rect.x = x
        self.rect.y = y
    
    def update(self):    
        self.rect.x += self.speedx
        
        #se passar do fim da tela, morre
        if self.rect.x > WIDTH:
            self.kill()
            
class Explosion(pygame.sprite.Sprite):
    
    def __init__(self, center, explosion_anim):

        pygame.sprite.Sprite.__init__(self)
        
        #Carrega a animacao
        self.explosion_anim = explosion_anim
        
        #Inicia o processo de animacao colocando a primeira imagem na tela
        self.frame = 0
        self.image = self.explosion_anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
            
        #guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()
        
        #Controle de ticks da animacao
        self.frame_ticks = 50
    
    def update(self):
        #Verifica o tick atual
        now = pygame.time.get_ticks()
        
        #Verifica quantos ticks se passaram desde a ultima mudança de frame
        elapsed_ticks = now - self.last_update
        
        #Se ja esta na hora de mudar a imagem
        if elapsed_ticks > self.frame_ticks:
            
            #Marca o tick da nova imagem
            self.last_update = now
            
            #avança um quadro
            self.frame += 1
            
            #Verifica se ja chegou no final da animacao
            if self.frame == len(self.explosion_anim):
                #se sim, tchau!
                self.kill()
            else:
                #Se ainda nao, troca imagem
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
        
            
#função assets (imagens e sons)
def load_assets(img_dir, snd_dir):
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
    return assets

#Inicializacao do pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()

#Tamanho da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Nome do jogo
pygame.display.set_caption("SuperFox by TeamAura")

#Ajuste de velocidade
clock = pygame.time.Clock()

#carrega todos os assets e guarda em um dicionario
assets = load_assets(img_dir, snd_dir)
    
#Carrega o fundo do jogo
background = assets['background']
background = pygame.transform.scale(background, (800, 500))
background_rect = background.get_rect()
background_rect2 = background_rect.copy()
background_rect2.x += background_rect2.width

#Carrega os sons do jogo
pygame.mixer.music.set_volume(0.2)
jump_sound = assets['jump_sound']
music_sound = assets['music_sound']
fireball_sound = assets['fireball_sound']
death_sound = assets['death_sound']
destruction_sound = assets['destruction_sound']

#Cria um player
player = Player(assets['player_img'], assets['fox_walk'], assets['fox_jump'])

#Cria coisas
pipe = Pipes(assets['pipe_img'])
    
#Grupos Geral
blocos = pygame.sprite.Group()
pipes = pygame.sprite.Group()
mobs = pygame.sprite.Group()
fireballs = pygame.sprite.Group()


#Grupo sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(pipe)

#Cria mobs
for i in range(5):
    mob = Mob(assets['mob_walk'])
    mobs.add(mob)
    all_sprites.add(mob)
    
#Cria blocos
for x in range(0, len(listaPosicaoBlocos), 1):
    bloco=BlocoTijolo(listaPosicaoBlocos[x][0], listaPosicaoBlocos[x][1])
    all_sprites.add(bloco)
    blocos.add(bloco)

#Cria blocos amarelos(itens)
for x in range(0, len(listaPosicaoBlocosAmarelos), 1):
    blocoItem=BlocoAmarelo(listaPosicaoBlocosAmarelos[x][0], listaPosicaoBlocosAmarelos[x][1])
    all_sprites.add(blocoItem)
    blocos.add(blocoItem)

#CArrega o placar de score
score_font = assets['score_font']


fireballimg = assets['fireball']
fireballimg = pygame.transform.scale(fireballimg, (35, 35))
fireballimg.set_colorkey(BLACK)

fox_life = assets['fox_life']
fox_life = pygame.transform.scale(fox_life, (80, 80))
fox_life.set_colorkey(BLACK)


#comando para evitar travamentos
try:
    
    #Musica do jogo
    music_sound.play(loops=-1)
    #Loop principal
    running = True
    
    score = 0
    lifes = 3
    ammo = 20
    
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
                    player.speedx -= 4
                    player.state = ANDANDO
                    
                if event.key == pygame.K_RIGHT:
                    player.speedx += 4
                    player.state = ANDANDO
                #Jump

                if event.key == pygame.K_SPACE:

                    if player.rect.bottom == HEIGHT - 80 or player.rect.bottom == HEIGHT - 250 or player.rect.bottom == HEIGHT - 390:
                        player.state = PULANDO
                        jump_sound.play()
                        player.speedy -= 14
                
                if event.key == pygame.K_q:
                    fireball = Fireball(assets['fireball'], (player.rect.x+50), (player.rect.y+5))
                    all_sprites.add(fireball)
                    fireballs.add(fireball)
                    fireball_sound.play()
                    ammo -= 1
                    
            #verifica se soltou alguma tecla
            elif event.type == pygame.KEYUP:
                #se soltou muda a velocidade
                if event.key == pygame.K_LEFT:
                    player.speedx += 4
                    player.state = PARADO
                    
                if event.key == pygame.K_RIGHT:
                    player.speedx -= 4
                    player.state = PARADO
                    
        #Atualiza os sprites
        all_sprites.update()
        
        hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_mask)
        if hits:
            player.kill()
            for i in mobs:
                mob.kill()
            lifes -= 1
            if lifes == 0:   
                death_sound.play()
                music_sound.stop()
                player.kill()
                time.sleep(3)
                running =  False
            else: 
                player = Player(assets['player_img'], assets['fox_walk'], assets['fox_jump'])
                all_sprites.add(player)

        
        hits = pygame.sprite.groupcollide(mobs, fireballs, True, True, pygame.sprite.collide_mask)
        for hit in hits:
            mob = Mob(assets['mob_walk'])
            all_sprites.add(mob)
            mobs.add(mob)
            destruction_sound.play()
            explosao = Explosion(hit.rect.center, assets['explosion_anim'])
            all_sprites.add(explosao)
            score += 100
            
        #background_rect.x -= 5
        #background_rect2.x -= 5
        #if background_rect.right < 0:
            #background_rect.x += background_rect.width*2
        #if background_rect2.right <0:
            #background_rect2.x += background_rect2.width*2
        
        #A cada loop redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        #colocando o score na tela
        text_surface = score_font.render('{:08d}'.format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH/2, 10)
        screen.blit(text_surface, text_rect)
        
        #colocando a vida na tela
        text_surface = score_font.render(chr(9829) * lifes, True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (WIDTH - 790, 10)
        screen.blit(text_surface, text_rect)
            
        #colocando munição na tela
        text_surface = score_font.render(' X{0}'.format(ammo), True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (WIDTH - 140, 45)
        img_rect = fireballimg.get_rect()
        img_rect.topright = (WIDTH - 120, 10)
        screen.blit(text_surface, text_rect)
        screen.blit(fireballimg, img_rect)
        
        #Depois de desenhar tudo inverte o display
        pygame.display.flip()
finally:
    pygame.quit()
        
        
        
        
        