import os

def menu_soma(input, a, b) :
    if input == 1:

        Soma1(a, b)

    elif input == 2:
        Soma2(a, b)

    elif input == 3:
        Soma3(a, b)

    else:
        return

'''

FUNÇÃO CASO 1

Funcao que recebe valores inteiros > 0, para os registradores A e B, e imprime a soma entre esses registradores, armazenandoem A e B fica zerado.

Segue abaixo as intrucoes:

    1: Faca ADD(A) va_para 2
    2: Faca SUB(B) va_para 3
    3: Se ZER(B) entao va_para 4 senao va_para 1

'''

def Soma1(a, b):
    c = 0
    d = 0
    inst = 0

    print("\n--Instrucoes--\n\n")
    print("1: Faca ADD(A) va_para 2\n")
    print("2: Faca SUB(B) va_para 3\n")
    print("3: Se ZER(B) entao va_para 4 senao va_para 1\n\n")
    print("\n(A, B, C, D    Proxima instrucao)\n\n")

    while b != 0:
        if inst == 0:
            inst = 1
        elif inst == 1:
            a += 1
            inst = 2
        elif inst == 2:
            b += -1
            inst = 3
        elif inst == 3:
            if b == 0:
                inst = 4
            else:
                inst = 1

        print ("(%i, %i, %i, %i    %i)\n" %a %b %c %d %inst)

    print("(%i, %i, %i, %i)\n\n", a, b, c, d)

'''

Função caso 2

Funcao que recebe valores inteiros > 0, para os registradores A e B, e imprime a soma entre esses registradores, armazenando no registrador auxiliar C, A e B ficam zerados.

Segue abaixo as intrucoes:

    1: Faca ADD(C) va_para 2
    2: Faca SUB(A) va_para 3
    3: Se ZER(A) va_para 4 senao va_para 1
    4: Faca ADD(C) va_para 5
    5: Faca SUB(B) va_para 6
    6: Se ZER(B) va_para 7 senao va_para 4
'''

def Soma2(a, b):
    c = 0
    d = 0
    inst = 0
    
    print("\n--Instrucoes--\n\n")
    print("1: Faca ADD(C) va_para 2\n")
    print("2: Faca SUB(A) va_para 3\n")
    print("3: Se ZER(A) va_para 4 senao va_para 1\n")
    print("4: Faca ADD(C) va_para 5\n")
    print("5: Faca SUB(B) va_para 6\n")
    print("6: Se ZER(B) va_para 7 senao va_para 4\n\n")
    print("\n(A, B, C, D    Proxima instrucao)\n\n")

    while b != 0:
        if inst == 0:
            inst = 1
        elif inst == 1:
            c += 1
            inst = 2
        elif inst == 2:
            a += -1
            inst = 3
        elif inst == 3:
            if a == 0:
                inst = 4
            else:
                inst = 1
        elif inst == 4:
            c += 1
            inst = 5
        elif inst == 5:
            b += -1
            inst = 6
        elif inst == 6:
            if b == 0:
                inst = 7
            else:
                inst = 4
        print ("(%i, %i, %i, %i    %i)\n", a, b, c, d, inst)
    print("(%i, %i, %i, %i)\n\n", a, b, c, d)

'''

 <b>Funcao Soma - Caso3</b>

 Funcao que recebe valores inteiros > 0 para os registradores A e B, e imprime a soma entre esses registradores,
 armazenando no registrador A, e utilizando o registrador auxiliar C, e restaurado o valor de B.

 Segue abaixo as intrucoes:

    1: Faca ADD(A) va_para 2

    2: Faca ADD(C) va_para 3

    3: Faca SUB(B) va_para 4

    4: Se ZER(B) entao va_para 5 senao va_para 1

    5: Faca ADD(B) va_para 6

    6: Faca SUB(C) va_para 7

    7: Se ZER(C) entao va_para 8 senao va_para 5

'''

def Soma3(a, b):
    c = 0
    d = 0
    inst = 0
    
    print("\n--Instrucoes--\n\n")
    print("1: Faca ADD(A) va_para 2\n")
    print("2: Faca ADD(C) va_para 3\n")
    print("3: Faca SUB(B) va_para 4\n")
    print("4: Se ZER(B) entao va_para 5 senao va_para 1\n")
    print("5: Faca ADD(B) va_para 6\n")
    print("6: Faca SUB(C) va_para 7\n")
    print("7: Se ZER(C) entao va_para 8 senao va_para 5\n\n")
    print("\n(A, B, C, D    Proxima instrucao)\n\n")

    while b != 0:
        if inst == 0:
            inst = 1
        elif inst == 1:
            a += 1
            inst = 2
        elif inst == 2:
            c += 1
            inst = 3
        elif inst == 3:
            b += -1
            inst = 4
        elif inst == 4:
            if b == 0:
                inst = 5
            else:
                inst = 1
        print ("(%i, %i, %i, %i    %i)\n", a, b, c, d, inst)

    inst = 5

    while c != 0:
        if inst == 5:
            b += 1
            inst = 6
        elif inst == 6:
            c += -1
            inst = 7
        elif inst == 7:
            if c == 0:
                inst = 8
            else:
                inst = 5
        print ("(%i, %i, %i, %i    %i)\n", a, b, c, d, inst)
    print("(%i, %i, %i, %i)\n\n", a, b, c, d)
