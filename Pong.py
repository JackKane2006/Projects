import pygame
import random
pygame.init()

pygame.display.set_caption("Pong")

RED, GREEN, BLUE, BLACK = (255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0)

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 700

BAR_WIDTH, BAR_HEIGHT, BALL_WIDTH = SCREEN_WIDTH/32, SCREEN_HEIGHT/4, SCREEN_WIDTH/30

wn = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

class Bar:
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.width = BAR_WIDTH
        self.height = BAR_HEIGHT
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_bar(self):
        pygame.draw.rect(wn, self.color, self.rect)

class Ball:
    def __init__(self, x, y, dx, dy) -> None:
        self.dx = dx
        self.dy = dy
        self.width = BALL_WIDTH
        self.rect = pygame.Rect(x, y, BALL_WIDTH, BALL_WIDTH)

    def draw_ball(self):
        pygame.draw.rect(wn, GREEN, self.rect)

class Label:
    def __init__(self, size) -> None:
        self.font = pygame.font.SysFont("Comic Sans MS", 80)
        self.text_surface = self.font.render("0 : 0", False, GREEN)
        self.surface = pygame.surface.Surface(size)
        self.surface.set_colorkey((0, 0, 0))
        self.blue_score = 0
        self.red_score = 0

    def draw(self):
        wn.blit(self.surface, (SCREEN_WIDTH/2 - self.surface.get_width() / 2, 0))
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.text_surface, (self.surface.get_width() / 2 - self.text_surface.get_width() / 2, 0))

    def update(self):
        self.text_surface = self.font.render(f"{self.blue_score} : {self.red_score}", False, GREEN)

class Pong:

    def reset_ball(): #resets screen after a score
            ball.rect.left = SCREEN_WIDTH/2 - ball.rect.width/2
            ball.rect.top = SCREEN_HEIGHT/2 - ball.rect.width/2
            ball.dx = random.choice([15, -15])
            Pong.redraw_screen()
            pygame.display.flip()

    def redraw_screen(): #erases everything then draws it again
        wn.fill(BLACK)
        bar1.draw_bar()
        bar2.draw_bar()
        ball.draw_ball()
        score.draw()
   
    def ball_bounce(): #for bouncing off the walls
        if ball.rect.top < 0:
            ball.dy = 10
        if ball.rect.top > SCREEN_HEIGHT - ball.rect.width:
            ball.dy = -10
   
    def check_bar_collides(bar, base): #detects collisions, finds which side of the bar the ball is on, then determines how close to the edge it is and adjusts speed. Also switches y direction if the ball bounces off the top or the edge
        if ball.rect.colliderect(bar):
            if ball.rect.centery <= bar.rect.centery:
                ball.dx = base * (1 + (bar.rect.centery - ball.rect.centery) / (BAR_HEIGHT/2))
                if ball.rect.top < bar.rect.top:
                    ball.dy = -15
            else:
                ball.dx = base * (1 + (ball.rect.centery - bar.rect.centery) / (BAR_HEIGHT/2))
                if ball.rect.bottom > bar.rect.bottom:
                    ball.dy = 15
   
wn.fill(BLACK)
 
bar1 = Bar(0 + SCREEN_HEIGHT/12, SCREEN_HEIGHT/2 - BAR_HEIGHT/2, BLUE)

bar2 = Bar(SCREEN_WIDTH/1.06255 - BAR_WIDTH, SCREEN_HEIGHT/2 - BAR_HEIGHT/2, RED)

ball = Ball(SCREEN_WIDTH/2 - BALL_WIDTH/2, SCREEN_HEIGHT/2 - BALL_WIDTH/2, 10, 10)

score = Label((200, 200))
score.draw()

clock = pygame.time.Clock()
playing = True

while playing:

    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    Pong.ball_bounce()
    Pong.check_bar_collides(bar1, 15)
    Pong.check_bar_collides(bar2, -15)

    ball.rect.move_ip(ball.dx, ball.dy)

    if pressed[pygame.K_w] and bar1.rect.top > 0:
        bar1.rect.top -= 15

    elif pressed[pygame.K_s] and bar1.rect.top < SCREEN_HEIGHT - bar1.rect.height:
        bar1.rect.top += 15

    if pressed[pygame.K_UP] and bar2.rect.top > 0:
        bar2.rect.top -= 15

    elif pressed[pygame.K_DOWN] and bar2.rect.top < SCREEN_HEIGHT - bar2.rect.height:
        bar2.rect.top += 15
   
    if ball.rect.left <= 0:
        score.red_score += 1
        score.update()

        Pong.reset_ball()
        if score.red_score >= 10:
            print("RED WINS!")
            break

    elif ball.rect.left >= SCREEN_WIDTH:
        score.blue_score += 1
        score.update()

        Pong.reset_ball()
        if score.blue_score >= 10:
            print("BLUE WINS!")
            break

    Pong.redraw_screen()
    pygame.display.flip()
    clock.tick(60)
   
pygame.quit()
