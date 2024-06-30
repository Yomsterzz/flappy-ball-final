import pgzrun
import random

WIDTH = 800
HEIGHT = 600
TITLE = "Flappy Ball!"

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

r2 = random.randint(0,255)
g2 = random.randint(0,255)
b2 = random.randint(0,255)

color = (r,g,b)
color2 = (r2,g2,b2)
radius = random.randint(25,50)
gravity = 4000.0

class Ball:
    def __init__(self, color, radius, x, y):
        self.color = color
        self.radius = 40
        self.x = x
        self.y = y
        self.xvel = 200
        self.yvel = 0

    
    def draw_ball(self):
        self.pos = (self.x, self.y)
        screen.draw.filled_circle(self.pos, self.radius, self.color)
    
ball1 = Ball(color, radius, WIDTH//2, 50)
ball2 = Ball(color2, 50, 50, 50)

def draw():
    screen.clear()
    ball1.draw_ball()
    ball2.draw_ball()

def update(c):
    #applying gravity
    bally = ball1.yvel
    ball1.yvel += gravity * c
    ball1.y += (bally + ball1.yvel) * 0.5 * c

    #adding bounce
    if ball1.y > HEIGHT - ball1.radius:
        ball1.y = HEIGHT - ball1.radius
        ball1.yvel = -ball1.yvel * 0.9
    
    #changing x-axis movement
    ball1.x += ball1.xvel * c
    if ball1.x > WIDTH - ball1.radius or ball1.x < ball1.radius:
        ball1.xvel = -ball1.xvel


def on_key_down(key):
    if key == keys.SPACE:
        ball1.yvel = -2000


pgzrun.go()