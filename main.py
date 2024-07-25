import pygame
from utils import *
from commands import *
pygame.init()

CHAR_W = 80
CHAR_H = 25

win = pygame.display.set_mode(((CHAR_W*8)+10, (CHAR_H*16)+10))
pygame.display.set_caption("FowlKern")

lines = [
    "Welcome to FowlKern v1.0.0",
    "",
    ""
]
font = pygame.font.Font("assets/font.ttf", 16)
curLine = 0
cmd = ""
running_cmd = False

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key != pygame.K_RETURN:
                if event.key == pygame.K_BACKSPACE:
                    cmd = cmd[:-1]
                else:
                    cmd += event.unicode
            else:
                lines.pop()
                lines.append("")
                running_cmd = True
                draw_new_line(lines, cmd, running_cmd)
                match cmd:
                    case "ver":
                        ver(lines)
                    case "help":
                        help(lines)
                    case "clear":
                        lines = [""]
                    case "neofetch":
                        neofetch(lines)
                    case "":
                        lines.append("")
                    case _:
                        if cmd.startswith("echo "):
                            printf(lines, cmd.removeprefix("echo "), 2)
                        else:
                            printf(lines, "Not a command!", 2)
                cmd = ""
                running_cmd = False

    clock.tick(60)

    win.fill((0, 0, 0))

    draw_new_line(lines, cmd, running_cmd)

    if len(lines) > CHAR_H:
        lines.pop(0)

    curLine = 0
    for line in lines:
        text = font.render(line, False, (255, 255, 255), (0, 0, 0))
        win.blit(text, (5, 5+(curLine*16)))
        curLine += 1

    pygame.display.flip()

pygame.quit()