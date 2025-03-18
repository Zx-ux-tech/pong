import pygame
import random

# Inicializa o Pygame
pygame.init()

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong - Defenda a Bolinha")

# Configurações da barra do jogador
paddle_width = 100
paddle_height = 15
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - paddle_height - 10
paddle_speed = 10

# Configurações da bolinha
ball_radius = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = random.choice([5, -5])
ball_speed_y = 5

# Pontuação
score = 0
font = pygame.font.SysFont(None, 30)

# Configurações dos blocos
block_width = 60
block_height = 20
block_margin = 10
blocks = []

# Função para criar os blocos
def create_blocks():
    global blocks
    blocks = []
    block_rows = 5
    block_columns = screen_width // (block_width + block_margin)
    
    for row in range(block_rows):
        for col in range(block_columns):
            block_x = col * (block_width + block_margin)
            block_y = row * (block_height + block_margin)
            blocks.append(pygame.Rect(block_x, block_y, block_width, block_height))

# Função para exibir a pontuação na tela
def display_score(score):
    score_text = font.render(f"Pontuação: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Função principal do jogo
def game_loop():
    global paddle_x, ball_x, ball_y, ball_speed_x, ball_speed_y, score, blocks

    # Criação dos blocos
    create_blocks()

    # Loop principal do jogo
    running = True
    while running:
        screen.fill(BLACK)  # Preenche o fundo de preto

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimentação da barra
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
            paddle_x += paddle_speed

        # Movimentação da bolinha
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Colisão com as paredes (horizontal)
        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
            ball_speed_x *= -1

        # Colisão com a parte superior
        if ball_y - ball_radius <= 0:
            ball_speed_y *= -1

        # Colisão com a barra
        if (ball_y + ball_radius >= paddle_y and paddle_x <= ball_x <= paddle_x + paddle_width):
            ball_speed_y *= -1

        # Colisão com a parede inferior (perdeu)
        if ball_y + ball_radius >= screen_height:
            running = False  # Fim de jogo

        # Verificação de colisão com os blocos
        ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
        for block in blocks[:]:
            if ball_rect.colliderect(block):
                # Rebote da bolinha
                ball_speed_y *= -1
                # Remove o bloco da lista
                blocks.remove(block)
                # Aumenta a pontuação
                score += 10
                break

        # Desenha os blocos
        for block in blocks:
            pygame.draw.rect(screen, GREEN, block)

        # Desenha a barra do jogador
        pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

        # Desenha a bolinha
        pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

        # Exibe a pontuação
        display_score(score)

        # Atualiza a tela
        pygame.display.update()

        # Controle de FPS
        pygame.time.Clock().tick(60)

    pygame.quit()
    input("Pressione Enter para sair...") 

# Inicia o jogo
game_loop()
