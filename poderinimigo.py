import pygame
import os

# Inicializa o Pygame
pygame.init()

# Configura a janela do jogo
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Carregamento de imagens
image1 = pygame.image.load("poder_inimigo1.png")
image2 = pygame.image.load("poder_inimigo2.png")
image3 = pygame.image.load("poder_inimigo3.png")
image4 = pygame.image.load("poder_inimigo4.png")
image5 = pygame.image.load("poder_inimigo5.png")
image6 = pygame.image.load("poder_inimigo6.png")
image7 = pygame.image.load("poder_inimigo7.png")

# Redimensionar a imagem
tamanho_imagem = (150, 100)
image1_scaled = pygame.transform.scale(image1, tamanho_imagem)
image2_scaled = pygame.transform.scale(image2, tamanho_imagem)
image3_scaled = pygame.transform.scale(image3, tamanho_imagem)
image4_scaled = pygame.transform.scale(image4, tamanho_imagem)
image5_scaled = pygame.transform.scale(image5, tamanho_imagem)
image6_scaled = pygame.transform.scale(image6, tamanho_imagem)
image7_scaled =  pygame.transform.scale(image7, tamanho_imagem)

# Definição inicial da imagem atual do personagem
character_image = image1

# Posição inicial do personagem
character_rect = character_image.get_rect()
character_rect.centerx = WIDTH // 2
character_rect.centery = HEIGHT // 2

# Velocidade de movimento do personagem
character_speed = 5

# Controle para alternar entre as imagens
image_index = 0

# Variável para controlar o flip horizontal
flip = False

# Loop principal do jogo
jogando = True
while jogando:
    # Processa os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False

    # Verificação das teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_rect.x -= character_speed
        flip = False
        image_index += 1
    if keys[pygame.K_RIGHT]:
        character_rect.x += character_speed
        flip = True
        image_index += 1
    if keys[pygame.K_UP]:
        character_rect.y -= character_speed
        image_index += 1
    if keys[pygame.K_DOWN]:
        character_rect.y += character_speed
        image_index += 1

    # Alterna entre as imagens do personagem
    if image_index % 7 == 0:
        character_image = image1_scaled
    elif image_index % 7 == 1:
        character_image = image2_scaled
    elif image_index % 7 == 2:
        character_image = image3_scaled
    elif image_index % 7 == 3:
        character_image = image4_scaled
    elif image_index % 7 == 4:
        character_image = image5_scaled
    elif image_index % 7 == 5:
        character_image = image6_scaled
    elif image_index % 7 == 6:
        character_image = image7_scaled

    # Limpa a tela
    screen.fill((255, 255, 255))

    if flip:
        character_image_flipped = pygame.transform.flip(
            character_image, True, False)
        screen.blit(character_image_flipped, character_rect)
    else:
        screen.blit(character_image, character_rect)
        
    # Atualiza a tela
    pygame.display.flip()

    # Aguarda um curto intervalo de tempo para reduzir a velocidade de alternância das imagens
    pygame.time.delay(100)

# Encerra o Pygame
pygame.quit()