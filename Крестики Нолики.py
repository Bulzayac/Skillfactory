field = '   0 1 2\n 0 - - -\n 1 - - -\n 2 - - -\n'
n = list(field)
win = 1


def step_x():
    print('ход первого игрока (x)')
    x2 = int(input('введите координату по горизонтали: '))
    x1 = int(input('введите координату по вертикали: '))
    return(x1,x2)


def input_x():
    x1, x2 = step_x()
    if (x1 == 0 and x2 == 0) and (n[12] != 'x') and (n[12] != 'o'):
        n.pop(12)
        n.insert(12, 'x')
        n1 = ''.join(n)
        print(n1)
    elif (x1 == 0 and x2 == 1) and (n[14] != 'x') and (n[14] != 'o'):
        n.pop(14)
        n.insert(14, 'x')
        n1 = ''.join(n)
        print(n1)
    elif (x1 == 0 and x2 == 2) and (n[16] != 'x') and (n[16] != 'o'):
        n.pop(16)
        n.insert(16, 'x')
        n1 = ''.join(n)
        print(n1)
    elif (x1 == 1 and x2 == 0) and (n[21] != 'x') and (n[21] != 'o'):
        n.pop(21)
        n.insert(21, 'x')
        n1 = ''.join(n)
        print(n1)
    elif (x1 == 1 and x2 == 1) and (n[23] != 'x') and (n[23] != 'o'):
        n.pop(23)
        n.insert(23, 'x')
        n1 = ''.join(n)
        print(n1)
    elif (x1 == 1 and x2 == 2) and (n[25] != 'x') and (n[25] != 'o'):
        n.pop(25)
        n.insert(25, 'x')
        n1 = ''.join(n)
        print(n1)
    elif (x1 == 2 and x2 == 0) and (n[30] != 'x') and (n[30] != 'o'):
        n.pop(30)
        n.insert(30, 'x')
        n1 = ''.join(n)
        print(n1)
    elif (x1 == 2 and x2 == 1) and (n[32] != 'x') and (n[32] != 'o'):
        n.pop(32)
        n.insert(32, 'x')
        n1 = ''.join(n)
        print(n1)
    elif (x1 == 2 and x2 == 2) and (n[34] != 'x') and (n[34] != 'o'):
        n.pop(34)
        n.insert(34, 'x')
        n1 = ''.join(n)
        print(n1)
    else:
        print('нет такой координаты или она уже занята, повторите ввод')
        step_x()
        input_x()


def step_o():
    print('ход второго игрока (o)')
    o2 = int(input('введите координату по горизонтали: '))
    o1 = int(input('введите координату по вертикали: '))
    return(o1,o2)


def input_o():
    o1, o2 = step_o()
    if (o1 == 0 and o2 == 0) and (n[12] != 'x') and (n[12] != 'o'):
        n.pop(12)
        n.insert(12, 'o')
        n1 = ''.join(n)
        print(n1)
    elif (o1 == 0 and o2 == 1) and (n[14] != 'x') and (n[14] != 'o'):
        n.pop(14)
        n.insert(14, 'o')
        n1 = ''.join(n)
        print(n1)
    elif (o1 == 0 and o2 == 2) and (n[16] != 'x') and (n[16] != 'o'):
        n.pop(16)
        n.insert(16, 'o')
        n1 = ''.join(n)
        print(n1)
    elif (o1 == 1 and o2 == 0) and (n[21] != 'x') and (n[21] != 'o'):
        n.pop(21)
        n.insert(21, 'o')
        n1 = ''.join(n)
        print(n1)
    elif (o1 == 1 and o2 == 1) and (n[23] != 'x') and (n[23] != 'o'):
        n.pop(23)
        n.insert(23, 'o')
        n1 = ''.join(n)
        print(n1)
    elif (o1 == 1 and o2 == 2) and (n[25] != 'x') and (n[25] != 'o'):
        n.pop(25)
        n.insert(25, 'o')
        n1 = ''.join(n)
        print(n1)
    elif (o1 == 2 and o2 == 0) and (n[30] != 'x') and (n[30] != 'o'):
        n.pop(30)
        n.insert(30, 'o')
        n1 = ''.join(n)
        print(n1)
    elif (o1 == 2 and o2 == 1) and (n[32] != 'x') and (n[32] != 'o'):
        n.pop(32)
        n.insert(32, 'o')
        n1 = ''.join(n)
        print(n1)
    elif (o1 == 2 and o2 == 2) and (n[34] != 'x') and (n[34] != 'o'):
        n.pop(34)
        n.insert(34, 'o')
        n1 = ''.join(n)
        print(n1)
    else:
        print('нет такой координаты или она уже занята, повторите ввод')
        step_o()
        input_o()


def proverka_xwin():
    global win
    if(n[12] == 'x') and (n[14] == 'x') and (n[16] == 'x'):
        print('победил первый игрок')
        win = win + 1
        return(win)
    elif (n[21] == 'x') and (n[23] == 'x') and (n[25] == 'x'):
        print('победил первый игрок')
        win = win + 1
        return (win)
    elif (n[30] == 'x') and (n[32] == 'x') and (n[34] == 'x'):
        print('победил первый игрок')
        win = win + 1
        return (win)
    elif (n[12] == 'x') and (n[21] == 'x') and (n[30] == 'x'):
        print('победил первый игрок')
        win = win + 1
        return (win)
    elif (n[14] == 'x') and (n[23] == 'x') and (n[32] == 'x'):
        print('победил первый игрок')
        win = win + 1
        return (win)
    elif (n[16] == 'x') and (n[25] == 'x') and (n[34] == 'x'):
        print('победил первый игрок')
        win = win + 1
        return (win)
    elif (n[12] == 'x') and (n[23] == 'x') and (n[34] == 'x'):
        print('победил первый игрок')
        win = win + 1
        return (win)
    elif (n[16] == 'x') and (n[23] == 'x') and (n[30] == 'x'):
        print('победил первый игрок')
        win = win + 1
        return (win)
    elif '-' not in n:
        print('ничья')
        win = win + 1
        return (win)


def proverka_owin():
    global win
    if(n[12] == 'o') and (n[14] == 'o') and (n[16] == 'o'):
        print('победил второй игрок')
        win = win + 1
        return(win)
    elif (n[21] == 'o') and (n[23] == 'o') and (n[25] == 'o'):
        print('победил второй игрок')
        win = win + 1
        return (win)
    elif (n[30] == 'o') and (n[32] == 'o') and (n[34] == 'o'):
        print('победил второй игрок')
        win = win + 1
        return (win)
    elif (n[12] == 'o') and (n[21] == 'o') and (n[30] == 'o'):
        print('победил второй игрок')
        win = win + 1
        return (win)
    elif (n[14] == 'o') and (n[23] == 'o') and (n[32] == 'o'):
        print('победил второй игрок')
        win = win + 1
        return (win)
    elif (n[16] == 'o') and (n[25] == 'o') and (n[34] == 'o'):
        print('победил второй игрок')
        win = win + 1
        return (win)
    elif (n[12] == 'o') and (n[23] == 'o') and (n[34] == 'o'):
        print('победил второй игрок')
        win = win + 1
        return (win)
    elif (n[16] == 'o') and (n[23] == 'o') and (n[30] == 'o'):
        print('победил второй игрок')
        win = win + 1
        return (win)
    elif '-' not in n:
        print('ничья')
        win = win + 1
        return (win)

while win == 1:
    step_x()
    input_x()
    proverka_xwin()
    while win == 1:
        step_o()
        input_o()
        proverka_owin()
        while win == 1:
            step_x()
            input_x()
            proverka_xwin()
            while win == 1:
                step_o()
                input_o()
                proverka_owin()
                while win == 1:
                    step_x()
                    input_x()
                    proverka_xwin()
                    while win == 1:
                        step_o()
                        input_o()
                        proverka_owin()
                        while win == 1:
                            step_x()
                            input_x()
                            proverka_xwin()
                            while win == 1:
                                step_o()
                                input_o()
                                proverka_owin()
                                while win == 1:
                                    step_x()
                                    input_x()
                                    proverka_xwin()