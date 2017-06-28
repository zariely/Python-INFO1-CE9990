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


if bmonth == 'january':
    month = 0
elif bmonth == 'february':
    month = 31
elif bmonth == 'march':
    month = 59
elif bmonth == 'april':
    month = 90
elif bmonth == 'may':
    month = 120
elif bmonth == 'june':
    month = 151
elif bmonth == 'july':
    month = 181
elif bmonth == 'august':
    month = 212
elif bmonth == 'september':
    month = 243
elif bmonth == 'october':
    month = 273
elif bmonth == 'november':
    month = 304
elif bmonth == 'december':
    month = 334   
else:
    month = 366

daterange = month + bday

#January 20 - February 18
if 20 <= daterange <= 49:
    print('You are an Aquarius!', end=e)

#February 19 - March 20  
elif 50 <= daterange <= 79:
    print('You are a Pisces!', end=e)

#March 21 - April 19 
elif 80 <= daterange <= 109:
    print('You are an Aries!', end=e)

#April 20 - May 20  
elif 110 <= daterange <= 140:
    print('You are a Taurus!', end=e)

#May 21 - June 20 
elif 141 <= daterange <= 171:
    print('You are a Gemini!', end=e)

#June 21 - July 22 
elif 172 <= daterange <= 203:
    print('You are a Cancer!', end=e)

#July 23 - August 22  
elif 204 <= daterange <= 234:
    print('You are a Leo!', end=e)

#August 23 - September 22
elif 235 <= daterange <= 265:
    print('You are a Virgo!', end=e)

#September 23 - October 22 
elif 266 <= daterange <= 295:
    print('You are a Libra!', end=e)

#October 23 - November 21 
elif 296 <= daterange <= 325:
    print('You are a Scorpio!', end=e)

#November 22 - December 21 
elif 326  <= daterange <= 355:
    print('You are a Sagittarius!', end=e)

#December 22 - January 19
elif  (356 <= daterange <= 365) or (1 <= daterange <= 19):
    print('You are a Capricorn!', end=e)

else:
    print('I have no idea what your sign is!', end=e)
    sys.exit(1)

sys.exit(0)
