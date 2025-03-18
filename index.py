import pygame
import random

# Inicializa o Pygame
pygame.init()

# Definir cores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)  # Adicionando a cor branca

# Configurações da tela
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-Man")

# Configurações do Pac-Man
pacman_radius = 20
pacman_x = screen_width // 2
pacman_y = screen_height // 2
pacman_speed = 5

# Configurações dos Fantasmas
ghost_radius = 20
ghosts = [
    {"x": random.randint(0, screen_width), "y": random.randint(0, screen_height), "color": RED},
    {"x": random.randint(0, screen_width), "y": random.randint(0, screen_height), "color": GREEN},
    {"x": random.randint(0, screen_width), "y": random.randint(0, screen_height), "color": BLUE}
]

# Pontos
points = []
for _ in range(10):
    points.append({"x": random.randint(0, screen_width), "y": random.randint(0, screen_height)})

# Função para desenhar o Pac-Man
def draw_pacman(x, y):
    pygame.draw.circle(screen, YELLOW, (x, y), pacman_radius)

# Função para desenhar os fantasmas
def draw_ghosts(ghosts):
    for ghost in ghosts:
        pygame.draw.circle(screen, ghost["color"], (ghost["x"], ghost["y"]), ghost_radius)

# Função para desenhar os pontos
def draw_points(points):
    for point in points:
        pygame.draw.circle(screen, WHITE, (point["x"], point["y"]), 5)

# Função para mover os fantasmas
def move_ghosts(ghosts, pacman_x, pacman_y):
    for ghost in ghosts:
        if ghost["x"] < pacman_x:
            ghost["x"] += 1
        elif ghost["x"] > pacman_x:
            ghost["x"] -= 1

        if ghost["y"] < pacman_y:
            ghost["y"] += 1
        elif ghost["y"] > pacman_y:
            ghost["y"] -= 1

# Função principal do jogo
def game_loop():
    global pacman_x, pacman_y, ghosts, points

    # Inicialização
    running = True
    clock = pygame.time.Clock()

    # Loop principal do jogo
    while running:
        screen.fill(BLACK)  # Preenche o fundo de preto

        # Processa os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimentação do Pac-Man
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and pacman_x > pacman_radius:
            pacman_x -= pacman_speed
        if keys[pygame.K_RIGHT] and pacman_x < screen_width - pacman_radius:
            pacman_x += pacman_speed
        if keys[pygame.K_UP] and pacman_y > pacman_radius:
            pacman_y -= pacman_speed
        if keys[pygame.K_DOWN] and pacman_y < screen_height - pacman_radius:
            pacman_y += pacman_speed

        # Movimenta os fantasmas
        move_ghosts(ghosts, pacman_x, pacman_y)

        # Desenha o Pac-Man
        draw_pacman(pacman_x, pacman_y)

        # Desenha os fantasmas
        draw_ghosts(ghosts)

        # Desenha os pontos
        draw_points(points)

        # Verifica colisões com os pontos
        for point in points[:]:
            if abs(pacman_x - point["x"]) < pacman_radius and abs(pacman_y - point["y"]) < pacman_radius:
                points.remove(point)

        # Verifica colisões com os fantasmas (Fim de Jogo)
        for ghost in ghosts:
            if abs(pacman_x - ghost["x"]) < pacman_radius + ghost_radius and abs(pacman_y - ghost["y"]) < pacman_radius + ghost_radius:
                running = False
                print("Você foi pego por um fantasma! Fim de jogo.")

        # Atualiza a tela
        pygame.display.update()

        # Controla a taxa de atualização (FPS)
        clock.tick(30)

    pygame.quit()

# Inicia o jogo
game_loop()
