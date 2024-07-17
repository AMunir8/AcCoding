# importing libraries
import pygame
import time
import random

snake_speed = 15

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
orange = pygame.Color(255, 82, 0)
acblue = pygame.Color(0, 100, 255)
pink = pygame.Color(255, 0, 155)

# Initializing pygame
pygame.init()

# Initializing game window
pygame.display.set_caption('Coding Camp Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True

#set default snake direction to right
direction = 'RIGHT'
change_to = direction

score = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)

    score_surface = score_font.render('Score: ' + str(score), True, color)

    score_rect = score_surface.get_rect()

    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('comic sans ms', 50) ##customize
    game_over_surface = my_font.render('Your Score is: ' + str(score), True, acblue) ##customize
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)

    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)

    pygame.quit()
    quit()

while True:

    for event in pygame.event.get():
        #checking which direction key is pressed and changing to that direction

    #changing direction to direction pressed

    #changing snake position


    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        snake_speed += 1
        fruit_spawn = False
    else:
        snake_body.pop()
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(pink) ##customize colour of window

    for pos in snake_body:
        pygame.draw.rect(game_window, acblue, pygame.Rect(pos[0], pos[1], 10, 10)) #customize colour of snake

    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10)) #customize colour of fruit

    #Game over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    #Touch the snake-body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    #display score
    show_score(1, white, 'comic sans ms', 20) ##customize

    pygame.display.update()

    fps.tick(snake_speed)





