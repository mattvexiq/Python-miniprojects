# PONG pygame

import random
import pygame, sys
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH // 2
HALF_PAD_HEIGHT = PAD_HEIGHT // 2
#ball_pos = [0, 0]
#ball_vel = [0, 0]
paddle1_vel = 0
paddle2_vel = 0
l_score = 0
r_score = 0

# canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Hello World')


class paddle:
    paddle_pos = []
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.paddle_pos = [width, height]
        self.color = color

    def paddle_movement(self, paddle_vel):
        if self.paddle_pos[1] > HALF_PAD_HEIGHT and self.paddle_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
            self.paddle_pos[1] += paddle_vel
        elif self.paddle_pos[1] == HALF_PAD_HEIGHT and paddle_vel > 0:
            self.paddle_pos[1] += paddle_vel
        elif self.paddle_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle_vel < 0:
            self.paddle_pos[1] += paddle_vel

    def draw_paddle(self, canvas):
        pygame.draw.polygon(canvas, self.color, [[self.paddle_pos[0] - HALF_PAD_WIDTH, self.paddle_pos[1] - HALF_PAD_HEIGHT],
                                            [self.paddle_pos[0] - HALF_PAD_WIDTH, self.paddle_pos[1] + HALF_PAD_HEIGHT],
                                            [self.paddle_pos[0] + HALF_PAD_WIDTH, self.paddle_pos[1] + HALF_PAD_HEIGHT],
                                            [self.paddle_pos[0] + HALF_PAD_WIDTH, self.paddle_pos[1] - HALF_PAD_HEIGHT]], 0)





class ball:
    def __init__(self, ball_pos, ball_vel):
        self.ball_pos = ball_pos
        self.ball_vel = ball_vel

    def ball_init(self, boolean):
        #global ball_pos, ball_vel  # these are vectors stored as lists
        self.ball_pos = [WIDTH // 2, HEIGHT // 2]
        horz = random.randrange(2, 4)
        vert = random.randrange(1, 3)

        if boolean == False:
            horz = - horz

        self.ball_vel = [horz, -vert]

    def ball_movement(self, paddle1, paddle2, r_score, l_score):
        self.ball_pos[0] += int(self.ball_vel[0])
        self.ball_pos[1] += int(self.ball_vel[1])

        # ball collision check on top and bottom walls
        if int(self.ball_pos[1]) <= BALL_RADIUS:
            self.ball_vel[1] = - self.ball_vel[1]
        if int(self.ball_pos[1]) >= HEIGHT + 1 - BALL_RADIUS:
            self.ball_vel[1] = - self.ball_vel[1]

        # ball collison check on gutters or paddles
        if int(self.ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH and int(self.ball_pos[1]) in range(paddle1.paddle_pos[1] - HALF_PAD_HEIGHT,paddle1.paddle_pos[1] + HALF_PAD_HEIGHT,1):
            self.ball_vel[0] = -self.ball_vel[0]
            self.ball_vel[0] *= 1.1
            self.ball_vel[1] *= 1.1
        elif int(self.ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH:
            r_score += 1
            self.ball_init(True)

        if int(self.ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH and int(self.ball_pos[1]) in range(paddle2.paddle_pos[1] - HALF_PAD_HEIGHT, paddle2.paddle_pos[1] + HALF_PAD_HEIGHT, 1): # ALERT: CALLS PADDLE
            self.ball_vel[0] = -self.ball_vel[0]
            self.ball_vel[0] *= 1.1
            self.ball_vel[1] *= 1.1
        elif int(self.ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH:
            l_score += 1
            self.ball_init(False)

    def draw_ball(self, canvas):
        pygame.draw.circle(canvas, RED, self.ball_pos, 20, 0)

#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def keydown(event):
    global paddle1_vel, paddle2_vel

    temp_vel = keydown_helper(event, K_UP, K_DOWN)
    if temp_vel != None:
        paddle2_vel = temp_vel
    temp_vel = keydown_helper(event, K_w, K_s)
    if temp_vel != None:
        paddle1_vel = temp_vel

def keydown_helper(event, up, down):
    if event.key == up:
        return -8
    elif event.key == down:
        return 8

# Key up
#   reset velocities
def keyup(event):
    global paddle1_vel, paddle2_vel

    temp_vel = keyup_helper(event, K_UP, K_DOWN)
    if temp_vel != None:
        paddle1_vel = temp_vel
    temp_vel = keyup_helper(event, K_w, K_s)
    if temp_vel != None:
        paddle1_vel = temp_vel

def keyup_helper(event, up, down):
    if event.key in (up, down):
        return 0

def draw(canvas, paddle1, paddle2, ball):
    global l_score, r_score

    canvas.fill(BLACK)
    pygame.draw.line(canvas, WHITE, [WIDTH // 2, 0], [WIDTH // 2, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1)
    pygame.draw.circle(canvas, WHITE, [WIDTH // 2, HEIGHT // 2], 70, 1)

    paddle1.paddle_movement(paddle1_vel)
    paddle2.paddle_movement(paddle2_vel)
#continue
    ball.draw_ball(canvas)
    paddle1.draw_paddle(canvas)
    paddle2.draw_paddle(canvas)
    ball.ball_movement(paddle1, paddle2, r_score, l_score)

    draw_scoreboard(canvas, l_score, 50, 20)
    draw_scoreboard(canvas, r_score, 470, 20)



def draw_scoreboard(canvas, score, x, y):
    myfont = pygame.font.SysFont("Comic Sans MS", 20)
    label = myfont.render("Score " + str(score), 1, (255, 255, 0))
    canvas.blit(label, (x, y))


#init()
paddle1 = paddle(HALF_PAD_WIDTH - 1, HEIGHT // 2, RED)
paddle2 = paddle(WIDTH + 1 - HALF_PAD_WIDTH, HEIGHT // 2, GREEN)
ball1 = ball([0, 0], [0, 0])
# game loop
while True:

    draw(window, paddle1, paddle2, ball1)

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps.tick(60)
