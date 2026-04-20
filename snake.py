# ---------------- IMPORTS ----------------
import pygame
import random
import sys

# initialize pygame
pygame.init()

# ---------------- SCREEN SETTINGS ----------------
CELL_SIZE = 20
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# ---------------- COLORS ----------------
WHITE = (255,255,255)
GREEN = (0,200,0)
RED = (200,0,0)
BLACK = (0,0,0)

# ---------------- FONTS ----------------
font = pygame.font.SysFont("Verdana",20)
game_over_font = pygame.font.SysFont("Verdana",60)

# create game over text
game_over_text = game_over_font.render("GAME OVER", True, BLACK)

# ---------------- GAME VARIABLES ----------------
snake = [(100,100),(80,100),(60,100)]  # snake body
direction = "RIGHT"

food = None

score = 0
level = 1
speed = 7

# ---------------- GENERATE FOOD ----------------
# generate random food position not on snake
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)

        if (x,y) not in snake:
            return (x,y)

food = generate_food()

# ---------------- MAIN GAME LOOP ----------------
running = True

while running:

    # -------- EVENTS --------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"

            if event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"

            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # -------- MOVE SNAKE --------
    head_x, head_y = snake[0]

    if direction == "UP":
        head_y -= CELL_SIZE
    if direction == "DOWN":
        head_y += CELL_SIZE
    if direction == "LEFT":
        head_x -= CELL_SIZE
    if direction == "RIGHT":
        head_x += CELL_SIZE

    new_head = (head_x, head_y)

    # -------- WALL COLLISION --------
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:

        screen.fill(RED)
        screen.blit(game_over_text,(WIDTH//4, HEIGHT//2))

        pygame.display.update()
        pygame.time.wait(2000)

        pygame.quit()
        sys.exit()

    # -------- SELF COLLISION --------
    if new_head in snake:

        screen.fill(RED)
        screen.blit(game_over_text,(WIDTH//4, HEIGHT//2))

        pygame.display.update()
        pygame.time.wait(2000)

        pygame.quit()
        sys.exit()

    snake.insert(0,new_head)

    # -------- FOOD COLLISION --------
    if new_head == food:

        score += 1
        food = generate_food()

        # level system (every 4 foods)
        if score % 4 == 0:
            level += 1
            speed += 2

    else:
        snake.pop()

    # -------- DRAW --------
    screen.fill(BLACK)

    # draw snake
    for block in snake:
        pygame.draw.rect(screen,GREEN,(block[0],block[1],CELL_SIZE,CELL_SIZE))

    # draw food
    pygame.draw.rect(screen,RED,(food[0],food[1],CELL_SIZE,CELL_SIZE))

    # draw score
    score_text = font.render("Score: " + str(score),True,WHITE)
    screen.blit(score_text,(10,10))

    # draw level
    level_text = font.render("Level: " + str(level),True,WHITE)
    screen.blit(level_text,(10,35))

    pygame.display.update()

    # control speed
    clock.tick(speed)