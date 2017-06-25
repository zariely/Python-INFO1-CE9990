'''
flag.py

Draws the Dominican Republic flag in color on a tkinter Canvas widget.

'''

import tkinter
import sys

#dimensions of entire flag, in pixels

cross_width = 50
height = 6 * cross_width  #300px
width = int(height * 3/2) #450px

#The root widget is the window that will contain everything we draw.
root = tkinter.Tk()
root.title('Dominican Republic Flag')
root.geometry(str(width) + 'x' + str(height))

#highlightthickness = 0 allows the canvas to occupy the entire root.
canvas = tkinter.Canvas(root, highlightthickness = 0)


y = 0
while y < height:

    x = 0
    while x < width:

        #top left dark blue
        #coordinates: 0,0 to ~200,125
        if x < (width * .444) and y < (2.5 * cross_width):
            canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = '#002D62')
            

        #bottom left red (leaves 50 px of negative space)
        #coordinates: 0,175 to ~200,300          
        elif x < width * .444 and y > (3.5 * cross_width):  
             canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = '#CE1126')
    
            
        #top right red
        #coordinates: ~250,0 to 450,125
        elif x > (width * .555) and y < (2.5 * cross_width):
            canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = '#CE1126')

        
        #bottom right dark blue
        #coordinates: ~250,175 to 450,300
        elif x > width * .555 and y > (3.5 * cross_width):  
             canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = '#002D62')
             

        #cross (negative space)            
        else:
            canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = '#ffffff')

        x += 1
    y += 1



#Make the canvas visible by packing it into the root.
canvas.pack(expand = tkinter.YES, fill = "both")

sys.exit(0)
