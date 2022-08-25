from subprocess import getoutput as gout
from os import get_terminal_size as gts
from time import sleep as sl
from random import randint as rd

t_clr = gout("clear")
c_clr = "\033[0;0m"

canvas = list(gts())
canvas[1] += -2

def goto(pos_x: int, pos_y: int) -> (str or None):
    return f"\033[{pos_y};{pos_x}H"

def color(id: int, background: bool) -> str:
    if background:
        return f"\033[48;5;{id}m"
    else:
        return f"\033[38;5;{id}m"

def draw_rect(pos_x: int, pos_y: int, geom_x: int, geom_y: int, sym: str, color_id: int):
    print(f"{color(color_id, False)}", end="")
    for g_y in range(geom_y):
        print(goto(pos_x+1, pos_y+1+g_y)+sym*geom_x)

def render(fps: int, secret: bool) -> None:
    rsizey = 5
    rposy = rd(0, canvas[1]-rsizey)
    rspeedy = 1

    rsizex = rsizey*2
    rposx = rd(0, canvas[0]-rsizex)
    rspeedx = rspeedy*2
    
    rcolor = rd(1, 15)
    while True:
        if not secret:
            print(f"{t_clr}{goto(0, 0)}{color(0, True)}{color(233, False)}"+','*canvas[0]*canvas[1])
        draw_rect(rposx, rposy, rsizex, rsizey, '#', rcolor)
        sl(1/fps)
        
        rposy += rspeedy
        if rposy + rsizey >= canvas[1]:
            rspeedy = -rspeedy
            rposy = canvas[1] - rsizey
            rcolor = rd(1, 15)
        elif rposy <= 0:
            rspeedy = -rspeedy
            rposy = 0
            rcolor = rd(1, 15)

        rposx += rspeedx
        if rposx + rsizex >= canvas[0]:
            rspeedx = -rspeedx
            rposx = canvas[0] - rsizex
            rcolor = rd(1, 15)
        elif rposx <= 0:
            rspeedx = -rspeedx
            rposx = 0
            rcolor = rd(1, 15)

def main():
    try:
        print(c_clr, t_clr, render(10, False))
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()
