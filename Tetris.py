import pygame
import random
pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Comic Sans MS', 30)

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 700

RED, GREEN, BLUE, BLACK = (255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0)

wn = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pygame.display.set_caption("Tetris")

wn.fill(BLACK)

figures = [
    [[1, 5, 9, 13], [4, 5, 6, 7]],
    [[0, 4, 8, 9], [6, 8, 9, 10], [1, 2, 6, 10], [8, 9, 10, 12]],
    [[5, 6, 9, 10]],
    [[1, 5, 9, 8], [4, 5, 6, 10], [1, 2, 5, 9], [5, 9, 10, 11]],
    [[5, 8, 9, 10], [2, 5, 6, 10], [4, 5, 6, 9], [2, 6, 7, 10]],
    [[2, 5, 6, 9], [4, 5, 9, 10]],
    [[0, 4, 5, 9], [5, 6, 8, 9]]
]

old_figures = []

class Label:
    def __init__(self, size) -> None:
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.text_surface = self.font.render("Score = 0", False, (255, 255, 255))
        self.surface = pygame.surface.Surface(size)
        self.score = 0
        self.surface.set_colorkey((0, 0, 0))

    def draw(self):
        wn.blit(self.surface, (0, 0))
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.text_surface, (25, 25))

    def update(self):
        self.text_surface = self.font.render(f"Score = {self.score}", False, (255, 255, 255))

class Figure:
    def __init__(self, x, y, speed) -> None:
        self.figure = random.choice(figures)
        self.x = x
        self.y = y
        self.rotation = 0
        self.color = random.randint(1, 3)
        self.speed = speed

class Tetris:
    def __init__(self, width, height, score) -> None:
        self.width = width
        self.height = height
        self.Grid = [[0 for i in range(width)] for j in range(height)]
   
    def draw_grid(self):
        for i in range(len(self.Grid)):
            for j in range(len(self.Grid[i])):
                if self.Grid[i][j] == 0:
                    pygame.draw.rect(wn, BLACK, pygame.Rect(j * SCREEN_WIDTH/self.width, i * SCREEN_HEIGHT/self.height, SCREEN_WIDTH/self.width, SCREEN_HEIGHT/self.height))
                elif self.Grid[i][j] == 1:
                    pygame.draw.rect(wn, RED, pygame.Rect(j * SCREEN_WIDTH/self.width, i * SCREEN_HEIGHT/self.height, SCREEN_WIDTH/self.width, SCREEN_HEIGHT/self.height))
                elif self.Grid[i][j] == 2:
                    pygame.draw.rect(wn, GREEN, pygame.Rect(j * SCREEN_WIDTH/self.width, i * SCREEN_HEIGHT/self.height, SCREEN_WIDTH/self.width, SCREEN_HEIGHT/self.height))
                elif self.Grid[i][j] == 3:
                    pygame.draw.rect(wn, BLUE, pygame.Rect(j * SCREEN_WIDTH/self.width, i * SCREEN_HEIGHT/self.height, SCREEN_WIDTH/self.width, SCREEN_HEIGHT/self.height))

    def get_figure(self):
        Faller.figure = random.choice(figures)
        Faller.rotation = 0
        Faller.color = random.randint(1, 3)
        Faller.x = 3
        Faller.y = 0

    def clear(self):
        for i in range(4):
            for j in range(4):
                if j + (i * 4) in Faller.figure[Faller.rotation]:
                    self.Grid[int(Faller.y) + i][Faller.x + j] = 0

    def draw(self):
        for i in range(4):
            for j in range(4):
                if j + (i * 4) in Faller.figure[Faller.rotation]:
                    self.Grid[int(Faller.y) + i][Faller.x + j] = Faller.color

    def collides(self, xchange, ychange):
        for i in range(4):
            for j in range(4):
                try:
                    if j + (i * 4) in Faller.figure[Faller.rotation]:
                        if self.Grid[int(Faller.y) + ychange + i][Faller.x + xchange + j] != 0 or Faller.x + xchange + j < 0:
                            return True
                except IndexError:
                    return True
        return False

    def rotate(self):
        if Faller.rotation + 1 < len(Faller.figure):
            Faller.rotation += 1
            if self.collides(0, 0):
                Faller.rotation -= 1
        else:
            Faller.rotation = 0
            if self.collides(0, 0):
                    Faller.rotation += (len(Faller.figure) - 1)

    def game_over(self):
        for i in range(4):
            for j in range(4):
                if j + (i * 4) in Faller.figure[Faller.rotation]:
                    if int(Faller.y) + i <= 1:
                        return True
        return False

    def tetris(self):
        for i in range(self.height - 1):
            if self.check_row(1 + i):
                Score.score += 10
                Score.update()
                for j in range(1 + i):
                    for k in range(self.width):
                        self.Grid[i + 1 - j][k] = self.Grid[i - j][k]

    def check_row(self, row):
        for column in range(self.width):
            if self.Grid[row][column] == 0:
                return False
        return True
       
Faller = Figure(3, 0, .05)
Game = Tetris(10, 20, 0)
Score = Label((200, 200))

clock = pygame.time.Clock()
playing = True

while playing:

    Game.clear()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            playing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if not Game.collides(-1, 0):
                    Faller.x -= 1

            if event.key == pygame.K_RIGHT:
                if not Game.collides(1, 0):
                    Faller.x += 1

            if event.key == pygame.K_r:
                Game.rotate()

    Faller.y += Faller.speed

    if Game.collides(0, 1):

        if Game.game_over():
            break
        Game.draw()
        Game.tetris() #checks for tetris

        figures.remove(Faller.figure) #makes sure you don't get the same figure too much
        if figures == []:
            figures = old_figures
        old_figures.append(Faller.figure)
       
        Game.get_figure() #gets new figure

    Game.draw() #adjusts grid
    Game.draw_grid() #updates screen
    Score.draw() #draws score

    pygame.display.flip()
    clock.tick(144)
   
pygame.quit()