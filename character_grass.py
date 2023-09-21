from pico2d import *
import math


def run_circle():
    #print('CIRCLE')

    cx, cy, r = 400, 300, 200
    for deg in range(-90, 270+1, 5):
        x = cx + r*math.cos(math.radians(deg))
        y = cy + r*math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.05)
    character.draw_now(x, y)
    pass

def run_rectangle():
    #print('RECTANGLE')

    #bottom line
    for x in range(50, 750+1, 5):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        delay(0.05)
    pass


open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

while(True):
    #run_circle()
    run_rectangle()
    break

close_canvas()
