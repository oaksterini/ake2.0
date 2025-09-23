import pygame
from random import randrange

pygame.init()
window = 600
tile_size = window // 12
range = (tile_size // 2, window - tile_size // 2, tile_size)
get_random_position = lambda: [randrange(*range), randrange(*range)]
snake = pygame.rect.Rect([0,0,tile_size - 2,tile_size-2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0,0)
time, time_step = 0, 110
food = snake.copy()
food.center = get_random_position()
screen = pygame.display.set_mode((window, window))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and snake_dir != (0, tile_size):
                snake_dir = (0, -tile_size)
            if event.key == pygame.K_s and snake_dir != (0, -tile_size):
                snake_dir = (0, tile_size)
            if event.key == pygame.K_a and snake_dir != (tile_size, 0):
                snake_dir = (-tile_size, 0)
            if event.key == pygame.K_d and snake_dir != (-tile_size, 0):
                snake_dir = (tile_size, 0)
        
        
    if snake.center == food.center:
        while True:
            new_pos = get_random_position()
            if all(segment.center != new_pos for segment in segments):
                food.center = new_pos
                break
        length += 1
        

    pygame.draw.rect(screen, "red", food)
    
    for i, segment in enumerate(segments):
        color = (0,255,0) if i == -1 else (0,150,0)  # Huvudet är sista segmentet
        pygame.draw.rect(screen, color, segment)


    time_now = pygame.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
        if snake.collidelist(segments[:-1])!= -1:
            pygame.quit()
            exit()
        if snake.left < 0 or snake.right > window or snake.top < 0 or snake.bottom > window:
            pygame.quit()
            exit()
        
    
    pygame.display.flip()
    clock.tick(20)