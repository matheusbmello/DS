import pygame
import os

# Inicializar o Pygame
pygame.init()

# Definir o tamanho da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Carregamento das imagens
image1 = pygame.image.load("inimigoparado1.png")
image2 = pygame.image.load("inimigoparado2.png")
image3 = pygame.image.load("inimigoparado3.png")

# Redimensionamento das imagens
tamanho_imagem = (100, 100)
image1_scaled = pygame.transform.scale(image1, tamanho_imagem)
image2_scaled = pygame.transform.scale(image2, tamanho_imagem)
image3_scaled = pygame.transform.scale(image3, tamanho_imagem)


# Definir o tempo de exibição de cada imagem (em segundos)
tempo_exibicao = 300

# Loop principal
executando = True
indice_imagem = 0

while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    # Atualizar o índice da imagem
    indice_imagem += 1

    # Verificar o limite do índice
    if indice_imagem == 3:
        indice_imagem = 0

    # Selecionar a imagem correspondente ao índice
    if indice_imagem == 0:
        imagem_surface = image1_scaled
    elif indice_imagem == 1:
        imagem_surface = image2_scaled
    elif indice_imagem == 2:
        imagem_surface = image3_scaled

    # Calcular as coordenadas para centralizar a imagem
    x = (largura_tela - tamanho_imagem[0]) // 2
    y = (altura_tela - tamanho_imagem[1]) // 2

    # Exibir a imagem na tela
    tela.blit(imagem_surface, (x, y))
    pygame.display.flip()

    # Aguardar o tempo de exibição
    pygame.time.wait(int(tempo_exibicao))

    # Limpar a tela
    tela.fill((255, 255, 255))

# Encerrar o Pygame
pygame.quit()
