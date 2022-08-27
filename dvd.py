from os import get_terminal_size as gts
from time import sleep as sl
from random import randint as rd

clr = "\033[0;0m\033[H\033[2J\033[3J"

def draw_rect(posx: int, posy: int, geomx: int, geomy: int, sym: str, color_id: int):
    """Draws a rectangle with the specified parameters at the specified coordinates."""
    line = sym*geomx
    print(f"\033[38;5;{color_id}m", end="")
    for g_y in range(geomy):
        print(f"\033[{posy+1+g_y};{posx+1}H{line}")

def check_col(pos, size, speed, canvas, rcolor):
    """Checks collisions with the edges of the screen."""
    pos += speed
    if pos + size >= canvas:
        speed = -speed
        pos = canvas - size
        rcolor = rd(1, 15)
        return pos, speed, rcolor
    elif pos <= 0:
        speed = -speed
        pos = 0
        rcolor = rd(1, 15)
        return pos, speed, rcolor
    return pos, speed, rcolor

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
            draw_rect(0, 0, canvas[0], canvas[1], ",", 233)
            draw_rect(rposx, rposy, rsizex, rsizey, "#", rcolor)
            rposy, rspeedy, rcolor = check_col(rposy, rsizey, rspeedy, canvas[1], rcolor)
            rposx, rspeedx, rcolor = check_col(rposx, rsizex, rspeedx, canvas[0], rcolor)
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
