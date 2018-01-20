from random import randint
from time import sleep, time

try:
    file = open('xp.txt', 'x')
    file.write('0')
    file.close()
except IOError:
    print(end='')

file = open('xp.txt', 'r')
nivel = file.read()
nivel_int = int(nivel)

tit = ''
dif = 0
if nivel_int < 100:
    tit = 'LvL Novato'
    dif = 0
elif 100 <= nivel_int < 200:
    tit = 'LvL Veterano'
    dif = 1
elif 300 <= nivel_int < 400:
    tit = 'LvL Mestre'
    dif = 2
elif 500 <= nivel_int < 800:
    tit = 'LvL Guru'
    dif = 3
elif 1000 <= nivel_int < 1600:
    tit = 'LvL Lendário'
    dif = 4
elif 2000 <= nivel_int < 3200:
    tit = 'LvL Guardião'
    dif = 5
elif nivel_int >= 6400:
    tit = 'LvL Deus'
    dif = 6


xps_no_save = cont = 0

def separation():
    print('\033[1;30m==\033[0m' * 25)


separation()
print('\033[1;34m')
print('{:^50}'.format('Cálculos Mentais v0.0.5'))
print('\033[0m')
separation()

while True:
    while True:
        if cont > 0:
            print('\nVocê está com {} xps não salvos.\n'.format(xps_no_save))
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
        op = str(input('Qual operação [+-*/] ?')).strip()[0]
        if op in '+-*/':
            break
    acertos = erros = 0
    separation()
    print('\nPara sair de qualquer operação insira [-666].\n')
    separation()
    sleep(3)
    if op in '+':
        while True:
            x = randint(n_min, n_max)
            y = randint(n_min, n_max)
            r_a = x + y
            t0 = time()
            r_p = int(input('[{}] {} + {} = '.format(tit, x, y)))
            if r_p == -666:
                break
            if r_a == r_p:
                print('{} + {} = \033[1;32m{}\033[0m [{:.2f}s]\n'.format(x, y, r_a, time() - t0))
                acertos += 1
                if dif == 0:
                    xps_no_save += 1
                elif dif == 1:
                    xps_no_save += 2
                elif dif == 2:
                    xps_no_save += 3
                elif dif == 3:
                    xps_no_save += 4
                elif dif == 4:
                    xps_no_save += 5
                elif dif == 5:
                    xps_no_save += 6
                elif dif == 6:
                    xps_no_save += 7
            else:
                print('{} + {} = \033[1;31m{}\033[0m [{:.2f}s]\n'.format(x, y, r_a, time() - t0))
                erros += 1
                if dif == 0:
                    xps_no_save -= 2
                elif dif == 1:
                    xps_no_save -= 4
                elif dif == 2:
                    xps_no_save -= 6
                elif dif == 3:
                    xps_no_save -= 8
                elif dif == 4:
                    xps_no_save -= 10
                elif dif == 5:
                    xps_no_save -= 12
                elif dif == 6:
                    xps_no_save -= 14
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
            r_p = int(input('[{}] {} - {} = '.format(tit, x, y)))
            if r_p == -666:
                break
            if r_a == r_p:
                print('{} - {} = \033[1;32m{}\033[0m [{:.2f}s]\n'.format(x, y, r_a, time() - t0))
                acertos += 1
                if dif == 0:
                    xps_no_save += 2
                elif dif == 1:
                    xps_no_save += 4
                elif dif == 2:
                    xps_no_save += 6
                elif dif == 3:
                    xps_no_save += 8
                elif dif == 4:
                    xps_no_save += 10
                elif dif == 5:
                    xps_no_save += 12
                elif dif == 6:
                    xps_no_save += 14
            else:
                print('{} - {} = \033[1;31m{}\033[0m [{:.2f}s]\n'.format(x, y, r_a, time() - t0))
                erros += 1
                if dif == 0:
                    xps_no_save -= 4
                elif dif == 1:
                    xps_no_save -= 8
                elif dif == 2:
                    xps_no_save -= 12
                elif dif == 3:
                    xps_no_save -= 16
                elif dif == 4:
                    xps_no_save -= 20
                elif dif == 5:
                    xps_no_save -= 24
                elif dif == 6:
                    xps_no_save -= 28
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
            r_p = int(input('[{}] {} * {} = '.format(tit, x, y)))
            if r_p == -666:
                break
            if r_a == r_p:
                print('{} * {} = \033[1;32m{}\033[0m [{:.2f}s]\n'.format(x, y, r_a, time() - t0))
                acertos += 1
                if dif == 0:
                    xps_no_save += 4
                elif dif == 1:
                    xps_no_save += 8
                elif dif == 2:
                    xps_no_save += 12
                elif dif == 3:
                    xps_no_save += 16
                elif dif == 4:
                    xps_no_save += 20
                elif dif == 5:
                    xps_no_save += 24
                elif dif == 6:
                    xps_no_save += 28
            else:
                print('{} * {} = \033[1;31m{}\033[0m [{:.2f}s]\n'.format(x, y, r_a, time() - t0))
                erros += 1
                if dif == 0:
                    xps_no_save -= 8
                elif dif == 1:
                    xps_no_save -= 16
                elif dif == 2:
                    xps_no_save -= 24
                elif dif == 3:
                    xps_no_save -= 32
                elif dif == 4:
                    xps_no_save -= 40
                elif dif == 5:
                    xps_no_save -= 48
                elif dif == 6:
                    xps_no_save -= 54
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
            r_p = str(input('[{}] {} / {} = '.format(tit, x, y)))
            ra_ = str(r_a)
            ra_2 = ('{}'.format(ra_))[0:4]
            if r_p == '-666':
                break
            if ra_2 == r_p:
                print('{} / {} = \033[1;32m{}\033[0m [{:.2f}s]\n'.format(x, y, ra_2, time() - t0))
                acertos += 1
                if dif == 0:
                    xps_no_save += 8
                elif dif == 1:
                    xps_no_save += 16
                elif dif == 2:
                    xps_no_save += 24
                elif dif == 3:
                    xps_no_save += 32
                elif dif == 4:
                    xps_no_save += 40
                elif dif == 5:
                    xps_no_save += 48
                elif dif == 6:
                    xps_no_save += 58
            else:
                print('{} / {} = \033[1;31m{}\033[0m [{:.2f}s]\n'.format(x, y, ra_2, time() - t0))
                erros += 1
                if dif == 0:
                    xps_no_save -= 16
                elif dif == 1:
                    xps_no_save -= 32
                elif dif == 2:
                    xps_no_save -= 48
                elif dif == 3:
                    xps_no_save -= 64
                elif dif == 4:
                    xps_no_save -= 80
                elif dif == 5:
                    xps_no_save -= 96
                elif dif == 6:
                    xps_no_save -= 116
        separation()
        print('\nNúmero de acertos {}\nNúmero de erros {}\n'.format(acertos, erros))
        separation()
        sleep(3)
    while True:
        sair = str(input('Deseja sair do programa? [S/N]')).strip().upper()[0]
        separation()
        if sair in 'SsNn':
            break
    if sair in 'Ss':
        print('\nSalvando a experiência...')
        sleep(3)
        break

file = open('xp.txt', 'r')
xp_salvo = file.read()
xp_s_int = int(xp_salvo)
no_save_more_save = xp_s_int + xps_no_save

file = open('xp.txt', 'w')
x = str(no_save_more_save)
file.write(x)
file.close()

#Kastarut - Contato = fb.com/kastarut
 
