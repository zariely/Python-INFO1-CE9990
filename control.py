'''
control.py

This program determines your astrological sign,
based on the date ranges on this website:
http://www.astrology-zodiac-signs.com/

'''

while True: 
    birthday = str(input('Want to find out your astrological sign? \nPlease enter your birth month and day (i.e. "October 03"): \n'))

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
        month = 0


    #January 20 - February 18
    if (month == 1 and (20 <= bday <= 31)) or (month == 2 and (1 <= bday <= 18)):
        print('You are an Aquarius! \n')


    #February 19 - March 20  
    elif (month == 2 and (19 <= bday <= 29)) or (month == 3 and (1 <= bday <= 20)):
        print('You are a Pisces! \n')


    #March 21 - April 19 
    elif (month == 3 and (21 <= bday <= 31)) or (month == 4 and (1 <= bday <= 19)):
        print('You are an Aries! \n')


    #April 20 - May 20  
    elif (month == 4 and (20 <= bday <= 30)) or (month == 5 and (1 <= bday <= 20)):
        print('You are a Taurus! \n')


    #May 21 - June 20 
    elif (month == 5 and (21 <= bday <= 31)) or (month == 6 and (1 <= bday <= 20)):
        print('You are a Gemini! \n')


    #June 21 - July 22 
    elif (month == 6 and (21 <= bday <= 30)) or (month == 7 and (1 <= bday <= 22)):
        print('You are a Cancer! \n')


    #July 23 - August 22  
    elif (month == 7 and (23 <= bday <= 31)) or (month == 8 and (1 <= bday <= 22)):
        print('You are a Leo! \n')


    #August 23 - September 22
    elif (month == 8 and (23 <= bday <= 31)) or (month == 9 and (1 <= bday <= 22)):
        print('You are a Virgo! \n')


    #September 23 - October 22 
    elif (month == 9 and (23 <= bday <= 30)) or (month == 10 and (1 <= bday <= 22)):
        print('You are a Libra! \n')


    #October 23 - November 21 
    elif (month == 10 and (23 <= bday <= 31)) or (month == 11 and (1 <= bday <= 21)):
        print('You are a Scorpio! \n')


    #November 22 - December 21 
    elif (month == 11 and (22 <= bday <= 30)) or (month == 12 and (1 <= bday <= 21)):
        print('You are a Sagittarius! \n')


    #December 22 - January 19
    elif (month == 12 and (22 <= bday <= 31)) or (month == 1 and (1 <= bday <= 19)):
        print('You are a Capricorn! \n')


    else:
        print('I have no idea what your sign is! \n')


