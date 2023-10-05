import pygame

pygame.init()
# TODO сделат классы для легкого взаимодействия с блоками, также сделать интерфейс взаимодействия с основынм циклом программы
# Создаем окно
screenWidth = 800  # Ширина окна
screenHeight = 600  # Высота окна
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Создание текстуры")

# Создаем пустую поверхность (текстуру) размером 100x100 пикселей
texture_width = 100
texture_height = 100
texture = pygame.Surface((texture_width, texture_height))

# Заполняем текстуру цветом
texture.fill((255, 0, 0))  # Красный цвет

# Рисуем круг на текстуре
pygame.draw.circle(texture, (0, 0, 255), (texture_width // 2, texture_height // 2), 40)  # Синий круг

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Заполняем фон основного окна

    # Отображаем текстуру на экране
    screen.blit(texture, (100, 100))  # Размещаем текстуру на координатах (100, 100)

    pygame.display.update()

pygame.quit()
