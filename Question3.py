# HIT 137 Assignment 2 Q3
# Group Name: CAS/DAN 1
# Group Members:
# Lee Potter - S368675
# Sahil Badgal - S384037

# Question 3 completed by Lee Potter

from turtle import *

# moves turtle position lower down window to give more room for drawing tree
# and set angle ready to draw vertical branch
def move_to_start():
    up()
    right(90)
    forward(200)
    left(180)
    down()

# move to given position and orientation without drawing
def move_position(p, o):
    up()
    goto(p)
    setheading(o)
    down()

# recursive function
def draw_branch(recursion_depth, left_angle, right_angle, length, reduction_factor, current_depth=0, is_left=False, branch_width=10):
    if current_depth >= recursion_depth:
        return
    
    width(branch_width)
    
    # draw the branch
    if current_depth == 0:
        color('brown')
    else:
        color('green')
        left(left_angle) if is_left else right(right_angle)
    forward(length)

    current_position = position()
    current_heading = heading()
    
    next_length =  length * (reduction_factor / 100)
    next_width = branch_width * (reduction_factor / 100)
    # ensure we always have width of at least 1 pixel
    if next_width < 1: next_width = 1

    # draw left and right branches recursively, resetting turtle position between function calls
    draw_branch(recursion_depth, left_angle, right_angle, next_length, reduction_factor, current_depth + 1, True, next_width)
    move_position(current_position, current_heading)
    draw_branch(recursion_depth, left_angle, right_angle, next_length, reduction_factor, current_depth + 1, False, next_width)
    

##### main entry point #####
left_angle = float(input('Left branch angle (degrees): '))
right_angle = float(input('Right branch angle (degrees): '))
start_length = float(input('Starting branch length (pixels): '))
recursion_depth = int(input('Recursion depth: '))
length_reduction_factor = float(input('Branch length reduction factor (percent): '))

# move starting position partway down the window to space tree more evenly
move_to_start()

# draw the tree using recursive function
draw_branch(recursion_depth, left_angle, right_angle, start_length, length_reduction_factor)

# pause to display image
mainloop()