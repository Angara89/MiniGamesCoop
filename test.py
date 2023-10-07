import pygame

# Инициализация Pygame
pygame.init()

# Создание экрана (поверхности) Pygame
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Цвет клеток
cell_color = (255, 255, 255)

# Размеры клеток и отступы
cell_width = 50
cell_height = 50
indent_x = 10
indent_y = 10

# Количество клеток по вертикали и горизонтали
num_rows = 5
num_cols = 7

# Создание группы объектов Rect
cell_group = []

# Создание клеток с отступами
for row in range(num_rows):
    for col in range(num_cols):
        x = col * (cell_width + indent_x)
        y = row * (cell_height + indent_y)
        cell = pygame.Rect(x, y, cell_width, cell_height)
        cell_group.append(cell)

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очищаем экран
    screen.fill((0, 0, 0))

    # Рисуем клетки на экране
    for cell in cell_group:
        pygame.draw.rect(screen, cell_color, cell)

    pygame.display.update()

# Завершение Pygame
pygame.quit()
