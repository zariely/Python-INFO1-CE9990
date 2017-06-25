'''
flag.py

Draws the Dominican Republic flag in color on a tkinter Canvas widget.
This is a condensed version of the previous flag.py script

'''

import tkinter
import sys

#dimensions of entire flag, in pixels

cross_width = 60
height = 6 * cross_width
width = int(height * 3/2) #450px

#The root widget is the window that will contain everything we draw.
root = tkinter.Tk()
root.title('Dominican Republic Flag')
root.geometry(str(width) + 'x' + str(height))

#highlightthickness = 0 allows the canvas to occupy the entire root.
#also creates a white background
canvas = tkinter.Canvas(root, highlightthickness = 0, background = '#ffffff')

y = 0
while y < height:

    x = 0
    while x < width:

        #top left & bottom right rectangles (dark blue)
        if x < width * .444 and y < 2.5 * cross_width \
           or x > width * .555 and y > 3.5 * cross_width: 
            canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = '#002D62')           

        #bottom left & top right rectangles (red)           
        elif x < width * .444 and y > 3.5 * cross_width \
            or  x > width * .555 and y < 2.5 * cross_width:
            canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = '#CE1126')

        x += 1
    y += 1

#Make the canvas visible by packing it into the root.
canvas.pack(expand = tkinter.YES, fill = "both")

sys.exit(0)
