#dice roller
import sys,math
from random import randint #.1 clean up code
while True:
    print('Choose your dice, or coin: coin, d4, d6 d8, d10, or d20 Press Q to quit')#.2 clarify instructions
    dice=input()
    if dice==('coin'):
        for i in range(1):
            randomNumber=(randint(1,2)) #no random. required!
        if randomNumber==1:
            print(' You got Heads')
        elif randomNumber==2:
            print('You got Tails')
    if dice==('d4'):
        print('You got a '+str(randint(1,4)))#add you got a (str)
    if dice==('d6'):
        print('You got a '+str(randint(1,6)))
    if dice==('d8'):
        print('You got a '+str(randint(1,8)))
    if dice==('d10'):
        print('You got a '+str(randint(1,10)))
    if dice==('d12'):
        print(('You got a '+str(randint(1,12)))#.2 add d12
    if dice==('d20'):
        print('You got a '+str(randint(1,20)))
    if dice==('q'):
        print('Thanks for playing!')
        sys.exit()
