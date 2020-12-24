#by cybercat, PPryanik

import os
from random import shuffle, randrange, randint
from time import sleep
import datetime


def mk_matrix(size):
    return [[x + y for y in range(1, size + 1)] for x in range(0, size ** 2, size)]


def random_matrix(size):
    matrix = mk_matrix(size)
    for line in matrix:
        shuffle(line)
    shuffle(matrix)
    return matrix


def show(matrix):
    size = len(matrix)
    out = "  " + " ".join([str(elem) for elem in range(size + 1, size * 2 + 1)]) + "\n"
    for row in range(len(matrix)):
        out += str(row + 1) + " " + "|".join([str(elem) for elem in matrix[row]]) + "\n"
    print(out)


def mov_x(matrix, row, direct):
    row = row - 1
    matrix[row] = matrix[row][-1:] + matrix[row][:-1] if direct else matrix[row][1:] + matrix[row][:1]
    return True


def mov_y(matrix, column, direct):
    column = column - 1
    size = len(matrix)
    if direct:
        repeat = 1
    else:
        repeat = size - 1
    for _ in range(repeat):
        reserv = matrix[len(matrix) - 1][column] + 0
        for i in range(size):
            new_reserv = matrix[i][column]
            matrix[i][column] = reserv
            reserv = new_reserv
    return True


def start():
    banner = "               ,,                    ,,          \n" \
             "`7MN.   `7MF'  db                  `7MM          \n" \
             "  MMN.    M                          MM          \n" \
             '  M YMb   M  `7MM  M"""MMV M"""MMV   MM   .gP"Ya \n' \
             "  M  `MN. M    MM  '  AMV  '  AMV    MM  ,M'   Yb\n" \
             '  M   `MM.M    MM    AMV     AMV     MM  8M""""""\n' \
             "  M     YMM    MM   AMV  ,  AMV  ,   MM  YM.    ,\n" \
             ".JML.    YM  .JMML.AMMmmmM AMMmmmM .JMML. `Mbmmd'\n"
    print(banner)
    sleep(1)
    size = input('Чтобы начать игру, укажите размер поля (по умолчанию 3):')
    while True:
        if size == "":
            size = 3
            break
        elif size.isnumeric() is False:
            size = input('Проверьте правильность данных!:')
        elif int(size) < 2:
            size = input('Укажите число побольше!:')
        else:
            size = int(size)
            break
    level = input('Укажите уровень сложности\n(1 - Легкий, 2 - Средний, 3 - Сложный):')
    while True:
        if level == "":
            level = 2
            break
        elif (level == "1") or (level == "2") or (level == "3"):
            level = int(level)
            break
        else:
            level = input('\n 1 - Легкий\n 2 - Средний \n 3 - Сложный\n:')
    return size, level


def generation(matrix, size, level):
    level = (level + 1) * 2
    while level > 0:
        TF = randint(0, 1)
        PM = randint(0, 1)
        CM = randrange(1, size)
        if TF == 0:
            mov_x(matrix, CM, PM)
        elif TF == 1:
            mov_y(matrix, CM, PM)
        level = level - 1
    return matrix


def game(size, level):
    answer = mk_matrix(size)
    matrix = mk_matrix(size)
    matrix = generation(matrix, size, level)
    starttime = datetime.datetime.now()
    while matrix != answer:
        cls()
        show(matrix)
        rotate = input('Укажите номер поворота: ')
        while True:
            try:
                rotate = int(rotate)
                if rotate < 0:
                    PM = 0
                    rotate = -rotate
                else:
                    PM = 1
                if rotate <= size * 2 and rotate > 0:
                    break
                else:
                    rotate = input('Укажите корректный номер: ')
            except:
                rotate = input('Укажите корректный номер: ')
        if rotate > size:
            rotate = rotate - size
            mov_y(matrix, rotate, PM)
        else:
            mov_x(matrix, rotate, PM)
    endtime = datetime.datetime.now()
    cls()
    show(matrix)
    print('Поздравляем! Вы справились с головоломкой!')
    print('Потраченное время: ', endtime - starttime)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    size, level = start()
    game(size, level)
