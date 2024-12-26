# HIT 137 Assignment 2 Q3
# Group Name: CAS/DAN 1
# Group Members:
# Lee Potter - S368675
# Sahil Badgal - S384037

from turtle import *


def draw_tree(recursion_depth, left_angle, right_angle, start_length, length_reduction_factor):
    draw_trunk(start_length)

    color('green')
    width(2)
    draw_branch(1, recursion_depth, True, left_angle, right_angle, start_length, length_reduction_factor)
    draw_branch(1, recursion_depth, False, left_angle, right_angle, start_length, length_reduction_factor)

def draw_trunk(start_length):
    up()
    right(90)
    forward(200)
    left(180)
    down()
    color('brown')
    width('4')
    forward(start_length)

def draw_branch(current_depth, recursion_depth, is_left, left_angle, right_angle, length, reduction_factor):
    if current_depth >= recursion_depth:
        return

    current_position = position()
    current_heading = heading()
    
    left(left_angle) if is_left else right(right_angle)
    forward(length)

    next_length =  length # - length * (reduction_factor / 100)

    draw_branch(current_depth + 1, recursion_depth, True, left_angle, right_angle, next_length, reduction_factor)
    goto(current_position)
    setheading(current_heading)
    draw_branch(current_depth + 1, recursion_depth, False, left_angle, right_angle, next_length, reduction_factor)


##### main entry point #####

left_angle = 20 # float(input('Left branch angle: '))
right_angle = 25 # float(input('Right branch angle: '))
start_length = 100 # float(input('Starting branch length: '))
recursion_depth = 5 # int(input('Recursion depth: '))
length_reduction_factor = 70 # float(input('Branch length reduction factor %: '))


draw_tree(recursion_depth, left_angle, right_angle, start_length, length_reduction_factor)


mainloop()