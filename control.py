'''
control.py

This program determines your astrological sign, based on the date ranges on these websites:
http://www.astrology-zodiac-signs.com/
https://www.epochconverter.com/days/2017

'''
import sys

e = '\n\n'

birthday = str(input('Want to find out your astrological sign? \nPlease enter your birth month and day (i.e. "October 03"): \n'))

#gets the substring of the birthday input minus last 3 characters
bmonth = str.lower(birthday[:-3])

#gets the last 2 characters and converts to int
bday = int(birthday[-2:])

#creates a list, starting with 0 
month = [
    None, #placeholder
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december'
    ]

month = month.index(bmonth)

#December 22 - January 19
if month == 12 and bday >= 22 or month == 1 and bday <= 19:
    print('You are a Capricorn!', end=e)
        
    #January 20 - February 18
elif month < 2 or month == 2 and bday <= 18:
    print('You are an Aquarius!', end=e)

    #February 19 - March 20
elif month < 3 or month == 3 and bday <= 20:
    print('You are a Pisces!', end=e)

    #March 21 - April 19 
elif month < 4 or month == 4 and bday <= 19:
    print('You are an Aries!', end=e)

    #April 20 - May 20  
elif month < 5 or month == 5 and bday <= 20:
    print('You are a Taurus!', end=e)

    #May 21 - June 20 
elif month < 6 or month == 6 and bday <= 20:
    print('You are a Gemini!', end=e)

    #June 21 - July 22 
elif month < 7 or month == 7 and bday <= 22: 
    print('You are a Cancer!', end=e)

    #July 23 - August 22  
elif month < 8 or month == 8 and bday <= 22:
    print('You are a Leo!', end=e)

    #August 23 - September 22
elif month < 9 or month == 9 and bday <= 22:
    print('You are a Virgo!', end=e)

    #September 23 - October 22 
elif month < 10 or month == 10 and bday <= 22:
    print('You are a Libra!', end=e)

    #October 23 - November 21 
elif month < 11 or month == 11 and bday <= 21:
    print('You are a Scorpio!', end=e)

    #November 22 - December 21 
elif month < 12 or month == 12 and bday <= 21:
    print('You are a Sagittarius!', end=e)

else:
    print('I have no idea what your sign is!', end=e)
    sys.exit(1)

sys.exit(0)
