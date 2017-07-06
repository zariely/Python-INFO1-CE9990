'''
for.py
This program loops through an array of colors.
'''

import sys


favColor = str.lower(input('What\'s your favorite color? '))


availableColors = ['blue', 'red', 'yellow', 'pink', 'green', 'teal',\
                   'purple', 'brown', 'gray', 'orange', 'fuschia', 'black',\
                   'white', 'turquoise', 'coral', 'indigo', 'charcoal']

for i in range(len(availableColors)):
    if favColor == 'black' or favColor == 'white':
        favColor = favColor.title()
        print(favColor, 'is not a color!')
        break

    else:
        print('I like', favColor, 'too!')
        break
    
sys.exit(0)       
