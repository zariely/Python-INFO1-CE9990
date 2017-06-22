'''  
inout.py

This program calculates your height in meters, so that you can
share this info with people from all over the world!

'''

import sys

print('''Hello! I've created a calculator that converts units of measurements.
I can tell you your height in meters! What is your height?
''')


try:
    ht_ft = int(input('feet: '))
except ValueError:
    print('I\'m sorry, I didn\'t catch that. Please enter your height in feet.')
    try: 
        ht_ft = int(input('feet: '))
    except ValueError:
        print('Ok fine...I\'ll assume you\'re only two feet tall!')
        ht_ft = 2

    

try:
    ht_in = int(input(' and inches: '))
except ValueError:
    print('I\'ll assume you\'re just ', ht_ft, 'feet tall then.')
    ht_in = 0 

ft_to_in = ht_ft * 12

meter_ht = round((ft_to_in + ht_in) * 0.0254, 2)

print('That equals to ', meter_ht, ' meters!', sep='')

sys.exit(0)
