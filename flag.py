'''
flag.py

Draws the Dominican Republic flag in color on a tkinter Canvas widget.
This is a condensed version of the previous flag.py script, 
including the drawPixel function

'''

import tkinter
import sys

cross_width = 60
height = 6 * cross_width
width = int(height * 3/2)

root = tkinter.Tk()
root.title('Dominican Republic Flag')
root.geometry(str(width) + 'x' + str(height))

canvas = tkinter.Canvas(root, highlightthickness = 0, background = '#ffffff')


def drawPixel(x, y, color):

    assert isinstance(x, int) and isinstance(y, int) and isinstance(color, str)
    canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = color)

#red color
red = '#CE1126'
#blue color
blue = '#002D62'

y = 0
while y < height:

    x = 0
    while x < width:

        #top left & bottom right rectangles (dark blue)
        if x < width * .444 and y < 2.5 * cross_width \
           or x > width * .555 and y > 3.5 * cross_width:
            drawPixel(x, y, blue)

        #bottom left & top right rectangles (red)                   
        elif x < width * .444 and y > 3.5 * cross_width \
            or  x > width * .555 and y < 2.5 * cross_width:
            drawPixel(x, y, red)

        x += 1
    y += 1



#Make the canvas visible by packing it into the root.
canvas.pack(expand = tkinter.YES, fill = "both")

sys.exit(0)
