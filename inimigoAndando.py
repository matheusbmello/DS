import pygame
import os

# Inicialização do Pygame
pygame.init()

# Definição das cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definição da largura e altura da tela
screen_width = 800
screen_height = 600

# Criação da tela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Personagem Andando")

# Carregamento das imagens
image1 = pygame.image.load("inimigo_andando1.png")
image2 = pygame.image.load("inimigo_andando2.png")
image3 = pygame.image.load("inimigo_andando3.png")
image4 = pygame.image.load("inimigo_andando4.png")
image5 = pygame.image.load("inimigo_andando5.png")
image6 = pygame.image.load("inimigo_andando6.png")

# Redimensionar a imagem
tamanho_imagem = (100, 100)
image1_scaled = pygame.transform.scale(image1, tamanho_imagem)
image2_scaled = pygame.transform.scale(image2, tamanho_imagem)
image3_scaled = pygame.transform.scale(image3, tamanho_imagem)
image4_scaled = pygame.transform.scale(image4, tamanho_imagem)
image5_scaled = pygame.transform.scale(image5, tamanho_imagem)
image6_scaled = pygame.transform.scale(image6, tamanho_imagem)

# Definição inicial da imagem atual do personagem
character_image = image1

# Posição inicial do personagem
character_rect = character_image.get_rect()
character_rect.centerx = screen_width // 2
character_rect.centery = screen_height // 2

# Velocidade de movimento do personagem
character_speed = 5

# Controle para alternar entre as imagens
image_index = 0

# Variável para controlar o flip horizontal
flip = False

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
    if image_index % 6 == 0:
        character_image = image1_scaled
    elif image_index % 6 == 1:
        character_image = image2_scaled
    elif image_index % 6 == 2:
        character_image = image3_scaled
    elif image_index % 6 == 3:
        character_image = image4_scaled
    elif image_index % 6 == 4:
        character_image = image5_scaled
    elif image_index % 6 == 5:
        character_image = image6_scaled

    # Limpeza da tela
    screen.fill(WHITE)

    # Desenho do personagem na tela
    if flip:
        character_image_flipped = pygame.transform.flip(
            character_image, True, False)
        screen.blit(character_image_flipped, character_rect)
    else:
        screen.blit(character_image, character_rect)

    # Atualização da tela
    pygame.display.flip()

    # Aguarda um curto intervalo de tempo para reduzir a velocidade de alternância das imagens
    pygame.time.delay(100)

# Encerramento do Pygame
pygame.quit()
