import pygame
import time
import random
import sys

pygame.init()
from Food import food
from SurfaceSnake import Surface
surface = Surface()
from SnakeBody import Body
snake = Body(surface.green, 10)
surface.chek_errors()
surface.Set_surface()
food = food(surface.green, surface.disWight, surface.disHeight)
while True:
    snake.change_to = surface.event_loop(snake.change_to)
    snake.validate_direction()
    surface.score, food.foodPos = snake.body_mech(surface.score, food.foodPos, surface.disWight, surface.disHeight)
    snake.draw_snake(surface.playSurface, surface.white)
    
    food.drawfood(surface.playSurface)
    snake.chek_for_bound(surface.game_over, surface.disWight, surface.disHeight)
    surface.score()
    surface.refresh_screen()

