# -------- IMPORTS --------
import pygame
import sys

# initialize pygame
pygame.init()

# font
font = pygame.font.SysFont("Arial", 18)

# -------- SCREEN SETTINGS --------
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# default color
color = BLACK

# drawing mode
mode = "draw"

# start position for shapes
start_pos = None

# fill background
screen.fill(WHITE)

# brush size
radius = 5
last_pos = None

# -------- MAIN LOOP --------
running = True
while running:

    for event in pygame.event.get():

        # close window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # keyboard controls
        if event.type == pygame.KEYDOWN:

            # exit program
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

            # change drawing modes
            if event.key == pygame.K_r:
                mode = "rectangle"

            if event.key == pygame.K_c:
                mode = "circle"

            if event.key == pygame.K_e:
                mode = "eraser"

            if event.key == pygame.K_d:
                mode = "draw"

            # color selection
            if event.key == pygame.K_1:
                color = BLACK

            if event.key == pygame.K_2:
                color = RED

            if event.key == pygame.K_3:
                color = GREEN

            if event.key == pygame.K_4:
                color = BLUE

        # mouse press
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos

        # mouse release (draw shapes)
        if event.type == pygame.MOUSEBUTTONUP:

            if mode == "rectangle":
                end_pos = event.pos

                rect = pygame.Rect(
                    start_pos[0],
                    start_pos[1],
                    end_pos[0]-start_pos[0],
                    end_pos[1]-start_pos[1]
                )

                pygame.draw.rect(screen, color, rect, 2)

            if mode == "circle":

                end_pos = event.pos

                radius = int(((end_pos[0]-start_pos[0])**2 +
                              (end_pos[1]-start_pos[1])**2) ** 0.5)

                pygame.draw.circle(screen, color, start_pos, radius, 2)

        # drawing with mouse
        if pygame.mouse.get_pressed()[0]:

            pos = pygame.mouse.get_pos()

            if last_pos is not None:

                if mode == "draw":
                    pygame.draw.line(screen, color, last_pos, pos, radius)

                if mode == "eraser":
                    pygame.draw.line(screen, WHITE, last_pos, pos, radius)

            last_pos = pos
        else:
            last_pos = None
# ---MENU
    controls = [
    "Controls:",
    "D - Draw",
    "R - Rectangle",
    "C - Circle",
    "E - Eraser",
    "1 - Black",
    "2 - Red",
    "3 - Green",
    "4 - Blue",
    "Q - Exit"
    ]

    y = 10
    for text in controls:
        label = font.render(text, True, BLACK)
        screen.blit(label, (10, y))
        y += 20


    pygame.display.update()