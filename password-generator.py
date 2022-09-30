import time
from random import randint

for i in range(1,45):
    print('')

str = ''

for i in range(1,1000):
    count = randint(1,100)
    while (count > 0):
        str += ' '
        count -= 1

    if (i % 10 ==0):
        print(str + 'Happy Dusshera 2022')
    else:
        print(str + '*')
    