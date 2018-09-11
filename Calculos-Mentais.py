from random import randint
from time import sleep, time

try:
    file = open('xp.txt', 'x')
    file.write('0')
    file.close()
except IOError:
    print(end='')


def read_data():
    with open('xp.txt') as file:
        var = file.read()
        return int(var)


xp_s = read_data()

titulos = {1: 'Novato', 2: 'Veterano', 3: 'Mestre', 4: 'Guru', 5: 'Lendário', 6: 'Guardião', 7: 'Deus'}


class Level(object):
    def __init__(self, xp, xpn):
        self.xp = xp
        self.xpn = xpn

    @property
    def d_level(self):
        if xp_s <= 100:
            self.xp += 1
            self.xpn -= 2
            return titulos[1]
        elif 100 < xp_s <= 200:
            self.xp += 2
            self.xpn -= 4
            return titulos[2]
        elif 200 < xp_s <= 400:
            self.xp += 4
            self.xpn -= 8
            return titulos[3]
        elif 400 < xp_s <= 800:
            self.xp += 8
            self.xpn -= 16
            return titulos[4]
        elif 800 < xp_s <= 1600:
            self.xp += 16
            self.xpn -= 32
            return titulos[5]
        elif 1600 < xp_s < 6400:
            self.xp += 32
            self.xpn -= 64
            return titulos[6]
        elif xp_s > 6400:
            self.xp += 64
            self.xpn -= 128
            return titulos[7]


perfil = Level(0, 0)
cont = xp_n = acertos = erros = 0


def separation():
    print('\033[1;30m==\033[0m' * 25)


separation()
print('\033[1;34m')
print('{:^50}'.format('Cálculos Mentais v0.0.7'))
print('\033[0m')
separation()

while True:
    while True:
        if cont > 0:
            print('\nVocê está com {} xps não salvos.\n'.format(xp_n))
            separation()
        n_min = int(input('Número mínimo: '))
        n_max = int(input('Número máximo: '))
        if n_min <= n_max:
            break
        print('\nErro, número mínimo é maior do que número máximo, insira um valor válido.')
        print('Exemplo: Mínimo == 1\n         Máximo == 100\n')
        sleep(3)
    separation()
    cont += 1
    while True:
        print('Obs: ao insirir interrogaçao a operaçao sera aleatoria.')
        op = str(input('Qual operação [+-*/?] ?')).strip()[0]
        if op in '+-*/?':
            break
    separation()
    print('\nPara sair de qualquer operação insira [-666].\n')
    separation()
    sleep(3)

    if op in '?':
        while True:
            x = randint(n_min, n_max)
            y = randint(n_min, n_max)
            rand = randint(1, 4)
            r_a = x + y
            r_b = x - y
            r_c = x * y
            r_d = x / y
            t0 = time()
            if rand == 1:
                r_p = int(input('[{}] {} + {} = '.format(perfil.d_level, x, y)))
                if r_p == -666:
                    break
                if r_a == r_p:
                    print('{} + {} = \033[1;32m{}\033[0m [{:.2f}s]\n'.format(x, y, r_a, time() - t0))
                    acertos += 1
                    xp_n = perfil.xp
                else:
                    print('{} + {} = \033[1;31m{}\033[0m [{:.2f}s]\n'.format(x, y, r_a, time() - t0))
                    erros += 1
                    xp_n = perfil.xpn

            if rand == 2:
                r_p = int(input('[{}] {} - {} = '.format(perfil.d_level, x, y)))
                if r_p == -666:
                    break
                if r_b == r_p:
                    print('{} - {} = \033[1;32m{}\033[0m [{:.2f}s]\n'.format(x, y, r_b, time() - t0))
                    acertos += 1
                    xp_n = perfil.xp
                else:
                    print('{} - {} = \033[1;31m{}\033[0m [{:.2f}s]\n'.format(x, y, r_b, time() - t0))
                    erros += 1
                    xp_n = perfil.xpn

            if rand == 3:
                r_p = int(input('[{}] {} * {} = '.format(perfil.d_level, x, y)))
                if r_p == -666:
                    break
                if r_c == r_p:
                    print('{} * {} = \033[1;32m{}\033[0m [{:.2f}s]\n'.format(x, y, r_c, time() - t0))
                    acertos += 1
                    xp_n = perfil.xp
                else:
                    print('{} * {} = \033[1;31m{}\033[0m [{:.2f}s]\n'.format(x, y, r_c, time() - t0))
                    erros += 1
                    xp_n = perfil.xpn

            if rand == 4:
                r_p = str(input('[{}] {} / {} = '.format(perfil.d_level, x, y)))
                ra_ = str(r_d)
                ra_2 = ('{}'.format(ra_))[0:4]
                if r_p == '-666':
                    break
                if ra_2 == r_p:
                    print('{} / {} = \033[1;32m{}\033[0m [{:.2f}s]\n'.format(x, y, ra_2, time() - t0))
                    acertos += 1
                    xp_n = perfil.xp
                else:
                    print('{} / {} = \033[1;31m{}\033[0m [{:.2f}s]\n'.format(x, y, ra_2, time() - t0))
                    erros += 1
                    xp_n = perfil.xpn

    if op in '+':
        while True:
            x = randint(n_min, n_max)
            y = randint(n_min, n_max)
            r_a = x + y
            t0 = time()
            r_p = int(input('[{}] {} + {} = '.format(perfil.d_level, x, y)))
            if r_p == -666:
                break
            if r_a == r_p:
                print('{} + {} = \033[1;32m{}\033[0m [{:.2f}s]\n'.format(x, y, r_a, time() - t0))
                acertos += 1
                xp_n = perfil.xp
            else:
                print('{} + {} = \033[1;31m{}\033[0m [{:.2f}s]\n'.format(x, y, r_a, time() - t0))
                erros += 1
                xp_n = perfil.xpn
        separation()
        print('\nNúmero de acertos {}\nNúmero de erros {}\n'.format(acertos, erros))
        separation()
        sleep(3)
    if op in '-':
        while True:
            x = randint(n_min, n_max)
            y = randint(n_min, n_max)
            r_a = x - y
            t0 = time()
            r_p = int(input('[{}] {} - {} = '.format(perfil.d_level, x, y)))
            if r_p == -666:
                break
            if r_a == r_p:
                print('{} - {} = \033[1;32m{}\033[0m [{:.2f}s]\n'.format(x, y, r_a, time() - t0))
                acertos += 1
                xp_n = perfil.xp
            else:
                print('{} - {} = \033[1;31m{}\033[0m [{:.2f}s]\n'.format(x, y, r_a, time() - t0))
                erros += 1
                xp_n = perfil.xpn
        separation()
        print('\nNúmero de acertos {}\nNúmero de erros {}\n'.format(acertos, erros))
        separation()
        sleep(3)
    if op in '*':
        while True:
            x = randint(n_min, n_max)
            y = randint(n_min, n_max)
            r_a = x * y
            t0 = time()
            r_p = int(input('[{}] {} * {} = '.format(perfil.d_level, x, y)))
            if r_p == -666:
                break
            if r_a == r_p:
                print('{} * {} = \033[1;32m{}\033[0m [{:.2f}s]\n'.format(x, y, r_a, time() - t0))
                acertos += 1
                xp_n = perfil.xp
            else:
                print('{} * {} = \033[1;31m{}\033[0m [{:.2f}s]\n'.format(x, y, r_a, time() - t0))
                erros += 1
                xp_n = perfil.xpn
        separation()
        print('\nNúmero de acertos {}\nNúmero de erros {}\n'.format(acertos, erros))
        separation()
        sleep(3)
    if op in '/':
        print('Observação: O programa só reconhece quatro digitos no total, exemplos: 0.23, 1.5, 1.45, 10.2, 99.0...')
        while True:
            x = randint(n_min, n_max)
            y = randint(n_min, n_max)
            r_a = x / y
            t0 = time()
            r_p = str(input('[{}] {} / {} = '.format(perfil.d_level, x, y)))
            ra_ = str(r_a)
            ra_2 = ('{}'.format(ra_))[0:4]
            if r_p == '-666':
                break
            if ra_2 == r_p:
                print('{} / {} = \033[1;32m{}\033[0m [{:.2f}s]\n'.format(x, y, ra_2, time() - t0))
                acertos += 1
                xp_n = perfil.xp
            else:
                print('{} / {} = \033[1;31m{}\033[0m [{:.2f}s]\n'.format(x, y, ra_2, time() - t0))
                erros += 1
                xp_n = perfil.xpn
        separation()
        print('\nNúmero de acertos {}\nNúmero de erros {}\n'.format(acertos, erros))
        separation()
        sleep(3)
    while True:
        sair = str(input('Deseja sair do programa? [S/N]')).strip().upper()[0]
        separation()
        if sair in 'SN':
            break
    if sair in 'S':
        print('\nSalvando a experiência...')
        sleep(3)
        break

xp_t = xp_s + xp_n
file = open('xp.txt', 'w')
file.write(str(xp_t))
file.close()
