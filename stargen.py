# Star gen!
# By Ash Thompson
# amt4049@rit.edu
# 9/11/2022
#
# Draws a star with an arbitrary number of points with Turtle!

import turtle as t
import tkinter
from math import pi, sin, cos, ceil

def t_init():
    # Screen init
    t.screensize(500, 500)
    t.setworldcoordinates(-250, -250, 250, 250)
    t.bgcolor("black")

    # Turtle init
    t.hideturtle()
    t.pencolor("red")
    t.width(10)
    t.speed("fast")
    

def gen_coords(num_points, radius):
    """
    Generates a circluar pattern of coordinates
    """
    # 5 points is the first star, arbitrary limit of 100-pointed max
    result = []
    if num_points < 5 or num_points > 100:
        return []
    
    theta = 2 * pi / num_points
    alpha = pi / 2
    for i in range(num_points):
        # TODO: Rotate these points so the top of the star always points up
        result.append([radius * cos(theta * i + alpha), radius * sin(theta * i + alpha)])
    
    return result

def does_skip_hit_all_points(coords, skip):
    """
    return True if skipping x coordinates results in all coordinates being
    touched. 1 < skip < len(coords) / 2
    """
    coords_touched = [False for i in range(len(coords))]
    num_points = len(coords)
    i = 0
    while coords_touched[i%num_points] == False:
        coords_touched[i%num_points] = True
        i += skip+1
    
    # If there are any untouched points left, return false
    return not list(filter(lambda x: x==False, coords_touched))


def draw_star(coords, skip):
    t.up()
    t.setpos(coords[-skip])
    t.down()
    for i in range(len(coords)):
        t.setpos(coords[(skip * i) % len(coords)])
    t.done()

if __name__ == "__main__":
    points = int(input("Enter the number of points for the star: "))
    coords = gen_coords(points, 200)
    skip = 2
    while not does_skip_hit_all_points(coords, skip) and skip < ceil(points / 2):
        skip += 1
    
    if skip >= ceil(points / 2):
        # Break for now, try 2-shapes and 3-shapes later
        print("No star possible")
    else:
        t_init()
        draw_star(coords, skip+1)
    