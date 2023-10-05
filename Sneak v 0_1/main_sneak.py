import pygame

pygame.init()

# Создаем окно
screenWidth = 800  # Ширина окна
screenHeight = 600  # Высота окна
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Перемещаемое окно")

class MovableWindow:
    def __init__(self, x, y, width, height, window_color, background_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.window_color = window_color
        self.background_color = background_color
        self.inner_rect = pygame.Rect(x + 10, y + 10, width / 4, height / 4)
        self.inner_color = (255, 0, 0)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        # Проверяем, чтобы окно не выходило за границы основного окна
        self.rect.x = max(0, min(self.rect.x, screenWidth - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, screenHeight - self.rect.height))

        # Обновляем положение внутреннего прямоугольника
        self.inner_rect.x = self.rect.x + 10
        self.inner_rect.y = self.rect.y + 10

    def move_inner_rect(self, dx, dy):
        self.inner_rect.x += dx
        self.inner_rect.y += dy

        # Проверяем, чтобы внутренний прямоугольник не выходил за границы окна
        self.inner_rect.x = max(self.rect.left + 10, min(self.rect.right - self.inner_rect.width - 10, self.inner_rect.x))
        self.inner_rect.y = max(self.rect.top + 10, min(self.rect.bottom - self.inner_rect.height - 10, self.inner_rect.y))

    def draw(self, surface):
        # Заполняем фон окна заданным цветом
        pygame.draw.rect(surface, self.background_color, self.rect)
        # Рисуем рамку окна заданным цветом
        pygame.draw.rect(surface, self.window_color, self.rect, 2)  # 2 - ширина рамки
        # Рисуем внутренний прямоугольник
        pygame.draw.rect(surface, self.inner_color, self.inner_rect)

# Цвета
window_color = (0, 0, 255)  # Цвет окна
background_color = (50, 50, 50)  # Цвет фона

# Создаем объект перемещаемого окна
window = MovableWindow(100, 100, 400, 400, window_color, background_color)

running = True
move_speed = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        window.move(-move_speed, 0)
    if keys[pygame.K_RIGHT]:
        window.move(move_speed, 0)
    if keys[pygame.K_UP]:
        window.move(0, -move_speed)
    if keys[pygame.K_DOWN]:
        window.move(0, move_speed)

    # Добавляем управление внутренним прямоугольником (WASD)
    if keys[pygame.K_w]:
        window.move_inner_rect(0, -move_speed)
    if keys[pygame.K_s]:
        window.move_inner_rect(0, move_speed)
    if keys[pygame.K_a]:
        window.move_inner_rect(-move_speed, 0)
    if keys[pygame.K_d]:
        window.move_inner_rect(move_speed, 0)

    screen.fill((0, 0, 0))  # Заполняем фон основного окна

    # Рисуем перемещаемое окно
    window.draw(screen)

    pygame.display.update()

pygame.quit()
