import pygame
import sys

pygame.init()

w = 600
h = 600
n = 10
cell = w // n

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Co Caro")

font = pygame.font.SysFont(None, 40)

bg = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
blue = (0, 0, 200)
green = (0, 150, 0)

board = [["" for j in range(n)] for i in range(n)]
turn = "X"
win = None

def draw():
    screen.fill(bg)
    for i in range(n):
        for j in range(n):
            rect = pygame.Rect(j * cell, i * cell, cell, cell)
            pygame.draw.rect(screen, black, rect, 1)
            if board[i][j] != "":
                color = red if board[i][j] == "X" else blue
                t = font.render(board[i][j], True, color)
                r = t.get_rect(center=rect.center)
                screen.blit(t, r)

def kt():
    def check(x, y, dx, dy):
        val = board[x][y]
        dem = 0
        for k in range(5):
            nx = x + dx * k
            ny = y + dy * k
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == val:
                dem += 1
            else:
                break
        return dem == 5

    for i in range(n):
        for j in range(n):
            if board[i][j] != "":
                if (
                    check(i, j, 1, 0)
                    or check(i, j, 0, 1)
                    or check(i, j, 1, 1)
                    or check(i, j, 1, -1)
                ):
                    return board[i][j]
    return None

def draw_win(text):
    txt = font.render(text, True, green)
    r = txt.get_rect(center=(w//2, h//2))
    screen.blit(txt, r)

run = True
while run:
    draw()
    if win:
        draw_win(f"{win} win!")
    pygame.display.flip()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.MOUSEBUTTONDOWN and not win:
            x, y = pygame.mouse.get_pos()
            i = y // cell
            j = x // cell
            if board[i][j] == "":
                board[i][j] = turn
                win = kt()
                turn = "O" if turn == "X" else "X"

pygame.quit()
sys.exit()