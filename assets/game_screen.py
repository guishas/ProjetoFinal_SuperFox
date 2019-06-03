# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:18:30 2019

@author: Usuario
"""
from config import img_dir, snd_dir, fnt_dir, WIDTH, HEIGHT, FPS, BLACK, WHITE, YELLOW, gravidade, PARADO, PULANDO, ANDANDO, NO_PULO, CAINDO, SHOOTING, QUIT, DONE
import pygame
import random
from os import path
import time
import json

#Classe jogador que representa a raposa
class Player(pygame.sprite.Sprite):
    
    #Construtor da classe
    def __init__(self, player_img, fox_walk, fox_jump, all_sprites, blocos):
        
        #Construtor da classe pai
        pygame.sprite.Sprite.__init__(self)
        
        #Imagem do player
        self.image = player_img
        self.walking = fox_walk
        self.pulando = fox_jump
        
        self.pulando = pygame.transform.scale(fox_jump, (48, 60))
        self.pulando.set_colorkey(WHITE)
        self.blocos = blocos
        #Diminuindo o tamanho da imagem
        self.image = pygame.transform.scale(player_img, (48, 60))
        
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
        
        #Define as colisões
        colisoes = pygame.sprite.spritecollide(self, self.blocos, False, pygame.sprite.collide_mask)
        
        #Bota a posição do personagem para antes da colisão
        for colisao in colisoes:
            #Indo para baixo
            if self.speedy > 0:
                self.rect.bottom = colisao.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = PARADO
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = colisao.rect.bottom
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = PARADO

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
    
    def __init__(self, mob_walk, assets, all_sprites, mobs):
        
        pygame.sprite.Sprite.__init__(self)
        
        #imagem
        self.animation = mob_walk
        
        self.image = pygame.image.load(path.join(img_dir, 'fox_static.png')).convert()
        self.assets = assets
        self.all_sprites = all_sprites
        self.mobs = mobs
        
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
            mob = Mob(self.assets['mob_walk'],self.assets, self.all_sprites, self.mobs)
            self.all_sprites.add(mob)
            self.mobs.add(mob)
            
class Bird(pygame.sprite.Sprite):
    
    def __init__(self, mob_fly, assets, all_sprites, birds):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.animation = mob_fly
        
        self.image = pygame.image.load(path.join(img_dir, 'fox_static.png')).convert()
        self.assets = assets
        self.all_sprites = all_sprites
        self.birds = birds
        
        teste = self.image
        
        self.image = pygame.transform.scale(teste, (70, 58))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randrange(860, 900)
        self.rect.bottom = HEIGHT - 280
        
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
            bird = Bird(self.assets['mob_fly'], self.assets, self.all_sprites, self.birds)
            self.all_sprites.add(bird)
            self.birds.add(bird)
        
        
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
    
    def __init__(self, x, y, assets):
        
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
    
    def __init__(self, x, y, assets):
        
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
    
    def __init__(self, x, y, assets):
        
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
                
def game_screen(screen, assets):
    
    #Ajuste de velocidade
    clock = pygame.time.Clock()
        
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
    

    
    #Cria coisas
    pipe = Pipes(assets['pipe_img'])
    
    #Grupos Geral
    blocos = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    fireballs = pygame.sprite.Group()
    birds = pygame.sprite.Group()
    
    #Grupo sprites
    all_sprites = pygame.sprite.Group()
    #Cria um player
    player = Player(assets['player_img'], assets['fox_walk'], assets['fox_jump'], all_sprites, blocos)
    all_sprites.add(player)
    all_sprites.add(pipe)
    all_sprites.add(birds)
    all_sprites.add(mobs)
    
    
    #Cria mobs
    for i in range(4):
        mob = Mob(assets['mob_walk'],assets, all_sprites, mobs)
        mobs.add(mob)
        all_sprites.add(mob)
        
    for i in range (3):
        bird = Bird(assets['mob_fly'],assets, all_sprites, birds)
        all_sprites.add(bird)
        birds.add(bird)
        
    #Cria blocos
    for x in range(0, len(listaPosicaoBlocos), 1):
        bloco=BlocoTijolo(listaPosicaoBlocos[x][0], listaPosicaoBlocos[x][1], assets)
        all_sprites.add(bloco)
        blocos.add(bloco)
    
    #Cria blocos amarelos(itens)
    for x in range(0, len(listaPosicaoBlocosAmarelos), 1):
        blocoItem=BlocoAmarelo(listaPosicaoBlocosAmarelos[x][0], listaPosicaoBlocosAmarelos[x][1], assets)
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
        #highscore
        with open('highscores.txt', 'r') as arq:
            highscore = json.load(arq)
        #Musica do jogo
        music_sound.play(loops=-1)
        #Loop principal
        PLAYING = 10
        DYING = 11
        

        
    
        reloading = False
        
        score = 0
        state = PARADO
        ammo = 20
        startTime = pygame.time.get_ticks()
        
        state = PLAYING
        
        while state != DONE:
            
            #Ajusta o tick do jogo
            clock.tick(FPS)
            #Eventos pygame
            for event in pygame.event.get():
            
                #verifica se foi fechado
                if event.type == pygame.QUIT:
                    state = DONE
                    
                
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
                            
                    if not reloading:
                        if event.key == pygame.K_q:
                            if ammo > 0:
                                fireball = Fireball(assets['fireball'], (player.rect.x+50), (player.rect.y+5))
                                all_sprites.add(fireball)
                                fireballs.add(fireball)
                                fireball_sound.play()
                                ammo -= 1
                                if ammo <= 0:
                                    ammo = 0
                                
                    if event.key == pygame.K_r and not reloading and ammo < 20:
                        startTime = pygame.time.get_ticks()
                        reloading = True
                        
                #verifica se soltou alguma tecla
                elif event.type == pygame.KEYUP:
                    #se soltou muda a velocidade
                    if event.key == pygame.K_LEFT:
                        player.speedx += 4
                        player.state = PARADO
                        
                    if event.key == pygame.K_RIGHT:
                        player.speedx -= 4
                        player.state = PARADO
             
            if reloading:
                now = pygame.time.get_ticks()
                diferenca = now - startTime
                if diferenca > 2000:
                    reloading = False
                    ammo = 20
                    
            #Atualiza os sprites
            all_sprites.update()
            
            if state == PLAYING:
            
                hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_mask)
                if hits:
                    state = DYING
                
                hits = pygame.sprite.groupcollide(mobs, fireballs, True, True, pygame.sprite.collide_mask)
                for hit in hits:
                    mob = Mob(assets['mob_walk'], assets, all_sprites, birds)
                    all_sprites.add(mob)
                    mobs.add(mob)
                    destruction_sound.play()
                    explosao = Explosion(hit.rect.center, assets['explosion_anim'])
                    all_sprites.add(explosao)
                    score += 100
                
                hits = pygame.sprite.spritecollide(player, birds, False, pygame.sprite.collide_mask)
                if hits:
                    state = DYING                      
                        
                hits = pygame.sprite.groupcollide(birds, fireballs, True, True, pygame.sprite.collide_mask)
                for hit in hits:
                    bird = Bird(assets['mob_fly'], assets, all_sprites, birds)
                    all_sprites.add(bird)
                    birds.add(bird)
                    destruction_sound.play()
                    explosao = Explosion(hit.rect.center, assets['explosion_anim'])
                    all_sprites.add(explosao)
                    score += 100
            elif state == DYING:
                highscore.append(score)
                highscore.sort(reverse=True)
                music_sound.stop()
                death_sound.play()
                player.kill()
                time.sleep(3)
                state = DONE
                with open('highscores.txt', 'w') as arq:
                    json.dump(highscore, arq)
                    
            #A cada loop redesenha o fundo e os sprites
            screen.fill(BLACK)
            screen.blit(background, background_rect)
            all_sprites.draw(screen)
            
            #colocando o score na tela
            text_surface = score_font.render('{:08d}'.format(score), True, YELLOW)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (WIDTH/2, 10)
            screen.blit(text_surface, text_rect)
                
    
            #colocando munição na tela
            text_surface = score_font.render(' X{0}'.format(ammo), True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.bottomleft = (WIDTH - 140, 45)
            img_rect = fireballimg.get_rect()
            img_rect.topright = (WIDTH - 120, 10)
            screen.blit(text_surface, text_rect)
            screen.blit(fireballimg, img_rect)
            
            #Colocando highscore na tela
            highscore_surface = score_font.render('HIGHSCORE: {}'.format(highscore[0]), True, YELLOW)
            highscore_rect = highscore_surface.get_rect()
            highscore_surface = pygame.transform.scale(highscore_surface, (175,20))
            highscore_rect.topleft = (10,10)
            screen.blit(highscore_surface, highscore_rect)
            
            #Depois de desenhar tudo inverte o display
            pygame.display.flip()

    finally:    
        return DONE


       
