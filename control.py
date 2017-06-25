'''
control.py

This program determines your astrological sign, based on the date
ranges on this website: http://www.astrology-zodiac-signs.com/

'''

e = '\n\n'

while True: 
    birthday = input('Want to find out your astrological sign?\nPlease enter your birth month and day (i.e. "October 03"): \n')

    #gets the substring of the birthday input minus last 3 characters
    bmonth = str.lower(birthday[:-3])

    #gets the last 2 characters and converts to int
    bday = int(birthday[-2:])
        
    if bmonth == 'january':
        month = 1
    elif bmonth == 'february':
        month = 2
    elif bmonth == 'march':
        month = 3
    elif bmonth == 'april':
        month = 4
    elif bmonth == 'may':
        month = 5
    elif bmonth == 'june':
        month = 6
    elif bmonth == 'july':
        month = 7
    elif bmonth == 'august':
        month = 8
    elif bmonth == 'september':
        month = 9
    elif bmonth == 'october':
        month = 10
    elif bmonth == 'november':
        month = 11
    elif bmonth == 'december':
        month = 12   
    else:
        month = 13 #outside of he range below
        

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
