from random import randint
from time import time

try:
    file = open('xp.txt', 'x')
    file.write('0')
    file.close()
except IOError:
    print(end='')


def read_data():
    with open('xp.txt') as file:
        value = file.read()
        return int(value)


levels = {1: 'Newbie', 2: 'Veteran', 3: 'Wise', 4: 'Legendary'}


def lvl():
    if read_data() <= 100:
        return levels[1]
    elif 100 < read_data() <= 500:
        return levels[2]
    elif 500 < read_data() <= 1000:
        return levels[3]
    elif 1000 < read_data():
        return levels[4]


class Calculation:
    def __init__(self, x, y, xp, lil_break):
        self.x = x
        self.y = y
        self.xp = xp
        self.lil_break = False

    def plus(self):
        t0 = time()
        r = int(input(f'[{lvl()}]: {self.x} + {self.y} = '))
        print(f'{self.x} + {self.y} = {self.x + self.y} [{time() - t0:.2f}s]')
        if r == -666:
            self.lil_break = True
            return
        if r == self.x + self.y:
            self.xp += 1
            print('[+1 xp]')
        elif r != self.x + self.y:
            self.xp -= 1
            print('[-1 xp]')

    def minus(self):
        t0 = time()
        r = int(input(f'[{lvl()}]: {self.x} - {self.y} = '))
        print(f'{self.x} - {self.y} = {self.x - self.y} [{time() - t0:.2f}s]')
        if r == -666:
            self.lil_break = True
            return
        if r == self.x - self.y:
            self.xp += 2
            print('[+2 xp]')
        elif r != self.x - self.y:
            self.xp -= 2
            print('[-2 xp]')

    def times(self):
        t0 = time()
        r = int(input(f'[{lvl()}]: {self.x} * {self.y} = '))
        print(f'{self.x} * {self.y} = {self.x * self.y} [{time() - t0:.2f}s]')
        if r == -666:
            self.lil_break = True
            return
        if r == self.x * self.y:
            self.xp += 3
            print('[+3 xp]')
        elif r != self.x * self.y:
            self.xp -= 3
            print('[-3 xp]')

    def division(self):
        t0 = time()
        r = str(input(f'[{lvl()}]: {self.x} / {self.y} = '))
        print(f'{self.x} / {self.y} = {self.x / self.y:.2f} [{time() - t0:.2f}s]')
        if r == '-666':
            self.lil_break = True
            return
        if r in str(self.x / self.y):
            self.xp += 4
            print('[+4 xp]')
        elif r not in str(self.x / self.y):
            self.xp -= 4
            print('[-4 xp]')


while True:
    mm = [int(input('> ')), int(input('< '))]
    if mm[0] < mm[1]:
        break
    else:
        print('Try again, ', end='')


def random():
    return randint(mm[0], mm[1])


c = Calculation(0, 0, 0, False)

while True:
    c.lil_break = False
    while True:
        operation = str(input('Which operation? [+-*/] ')).strip()
        if operation in '+-*/':
            break
        print('Try again, ', end='')
    if operation == '+':
        while True:
            c.x = random()
            c.y = random()
            c.plus()
            print()
            if c.lil_break:
                break
    elif operation == '-':
        while True:
            c.x = random()
            c.y = random()
            c.minus()
            print()
            if c.lil_break:
                break
    elif operation == '*':
        while True:
            c.x = random()
            c.y = random()
            c.times()
            print()
            if c.lil_break:
                break
    elif operation == '/':
        while True:
            c.x = random()
            c.y = random() + 1
            c.division()
            print()
            if c.lil_break:
                break

    lil_break2 = str(input('Exit? [Y/N]')).upper()
    if lil_break2 in 'Y':
        break

c.xp += read_data()
file = open('xp.txt', 'w')
file.write(str(c.xp))
file.close()
