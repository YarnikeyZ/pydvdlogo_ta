from os import get_terminal_size as gts
from time import sleep as sl
from random import randint as rd
from sys import argv
from pixpile.pixpile import *

clr = "\033[0;0m\033[H\033[2J\033[3J"

def render(fps: int) -> None:
    """Renders an "image" to the screen."""
    try:
        canvas = list(gts())
        # rect = [sym[0], color[1], posx[2], posy[3], sizex[4], sizey[5], speedx[6], speedy[7], newcolor[8]]
        rect = ["#", rd(1, 15), rd(0, canvas[0]), rd(0, canvas[1]), 10, 5, 2, 1, False]
        while True:
            print(draw_rectangle(",", 233, 0, 0, canvas[0], canvas[1]))
            print(draw_rectangle(rect[0], rect[1], rect[2], rect[3], rect[4], rect[5]))
            rect[2] += rect[6]
            rect[3] += rect[7]
            rect[2], rect[3], rect[4], rect[5], rect[6], rect[7], rect[8] = check_collision([rect[2], rect[3], rect[4], rect[5], rect[6], rect[7]], [0, 0, canvas[0], canvas[1], 0, 0], 0)
            if rect[8]:
                rect[1] = rd(1, 255)
            canvas = list(gts())
            sl(1/fps)
    except KeyboardInterrupt:
        return

def main():
    """A function responsible for initialization"""
    print(clr, end="")
    try:
        render(int(argv[1]))
    except IndexError:
        render(int(input("FPS:")))
    print(clr, end="")

if __name__ == "__main__":
    main()
