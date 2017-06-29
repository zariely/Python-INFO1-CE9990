'''
graphpaper.py
 
This program prints out a grid based on user input.
 
'''
 
 
import sys
 
#variables
plus = '+'
dash = '-'
pipe = '|'
space = ' '


row = int(input('How many rows of boxes? '))
col = int(input('How many columns of boxes? '))
width = int(input('How many columns of spaces in each box? '))
height = int(input('How many rows of spaces in each box? '))
 

a = plus + (width * dash + plus) * col
b = pipe + (height * space + pipe) * row

x = 0
while x < row:
    print(a)
    x += 1

    y = 0
    while y < col:
        print(b)
        y += 1
print(a)

sys.exit(0)
