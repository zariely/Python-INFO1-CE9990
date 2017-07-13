'''
twelvedays.py

This program prints out the lyrics
in the song "Twelve Days of CHRISTmas"

'''

import sys

lyrics = [
    'Twelve drummers drumming',
    'Eleven pipers piping',
    'Ten lords a-leaping',
    'Nine ladies dancing',
    'Eight maids a-milking',
    'Seven swans a-swimming',
    'Six geese a-laying',
    'Five Golden Rings',
    'Four colly birds',
    'Three French hens',
    'Two turtledoves',
    None, #later becomes index 1
    None #later becomes index 0 
    ]

firstVerse = 'On the {}{} day of Christmas\nMy true love gave to me'
verses = lyrics[::-1]

for a in range(1, len(verses)):
    
    lastVerse = 'And a partridge in a pair tree.'

    if a == 1:
        o = 'st'
        lastVerse = lastVerse[4:].capitalize()
    elif a == 2:
        o = 'nd'
    elif a == 3:
        o = 'rd'
    else:
        o = 'th'
        
    print(firstVerse.format(a, o))

    for b in range(a, 1, -1):
        print(verses[b])
    print(lastVerse)
    print()
        
sys.exit(0)
