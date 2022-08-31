from os import get_terminal_size as gts
from time import sleep as sl
from random import randint as rd
from pixpile.pixpile import *

clr = "\033[0;0m\033[H\033[2J\033[3J"

def render(fps: int) -> None:
    """Renders an "image" to the screen."""
    try:
        canvas = list(gts())
        canvas[1] += -1
        rsizey = 5
        rsizex = rsizey*2
        rposy = rd(0, canvas[1]-rsizey)
        rposx = rd(0, canvas[0]-rsizex)
        rspeedy = 1
        rspeedx = rspeedy*2
        rcolor = rd(1, 15)
        while True:
            draw_rectangle(",", 233, 0, 0, canvas[0], canvas[1])
            draw_rectangle("#", rcolor, rposx, rposy, rsizex, rsizey)
            rposy, rspeedy, newcolor = check_collision(rposy, rsizey, rspeedy, canvas[1])
            rposx, rspeedx, newcolor = check_collision(rposx, rsizex, rspeedx, canvas[0])
            if newcolor:
                rcolor = rd(1, 15)
            canvas = list(gts())
            canvas[1] += -1
            sl(1/fps)
    except KeyboardInterrupt:
        return

def main():
    """A function responsible for initialization"""
    print(clr, end="")
    render(10)
    print(clr, end="")

if __name__ == "__main__":
    main()
