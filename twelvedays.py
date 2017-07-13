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
    None
    ]

verses = lyrics[::-1]

for a in range(len(verses)):

    firstVerse = 'On the %s%s day of Christmas\nMy true love gave to me'
    lastVerse = 'And a partridge in a pair tree.'

    if a == 0:
        o = 'st'
        lastVerse = lastVerse[4:].capitalize()
    elif a == 1:
        o = 'nd'
    elif a == 2:
        o = 'rd'
    else:
        o = 'th'
        
    print(firstVerse %(a+1, o))

    for b in range(a, 0, -1):
        print(verses[b])
    print(lastVerse, '', sep='\n')
        
sys.exit(0)
