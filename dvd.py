from os import get_terminal_size as gts
from time import sleep as sl
from random import randint as rd
from pixpile.pixpile import *

clr = "\033[0;0m\033[H\033[2J\033[3J"

def render(fps: int, rect_num: int) -> None:
    """Renders an "image" to the screen."""
    try:
        canvas = list(gts())
        canvas[1] += -1
        # rect = [sym[0], color[1], posx[2], posy[3], sizex[4], sizey[5], speedx[6], speedy[7], newcolor[8]]
        rects = []
        for r in range(1, rect_num+1):
            rects.append([str(r), rd(1, 15), rd(0, canvas[0]), rd(0, canvas[1]), 10, 5, rd(1, 2)*2, rd(1, 2), False])
        while True:
            draw_rectangle(",", 233, 0, 0, canvas[0], canvas[1])
            for rect in rects:
                draw_rectangle(rect[0], rect[1], rect[2], rect[3], rect[4], rect[5])
                rect[2], rect[6], rect[8] = check_collision(rect[2], 0, rect[4], canvas[0], rect[6])
                rect[3], rect[7], rect[8] = check_collision(rect[3], 0, rect[5], canvas[1], rect[7])
                if rect[8]:
                    rect[1] = rd(1, 255)
            canvas = list(gts())
            canvas[1] += -1
            sl(1/fps)
    except KeyboardInterrupt:
        return

def main():
    """A function responsible for initialization"""
    print(clr, end="")
    render(int(input("FPS:")), int(input("Num of Rectangles:")))
    print(clr, end="")

if __name__ == "__main__":
    main()
