def menu_mult (input, a, b):
    if input == 1:
        Mult_1(a, b)
'''
* <b>Funcao Multiplicacao - Caso 1</b>

 *Funcao que recebe valores inteiros > 0 para os registradores A e B, e imprime a multiplicacao entre esses registradores,
 armazenando o resultado no registrador A e utilizando os registradores auxiliares C e D, o valor de B e restaurado.
 A varivavel 'inst' representa a proxima instrucao.

 Segue abaixo as instrucoes:

    1: Faca ADD(D) va_para 2
    2: Faca SUB(A) va_para 3
    3: Se ZER(A) va_para 4 senao va_para 1

    4: Faca ADD (A) va_para 5
    5: Faca ADD(C) va_para 6
    6: Faca SUB(B) va_para 7
    7: Se ZER(B) va_para 8 senao va_para 4
    8: Faca SUB(D) va_para 9
    9: Se ZER(D) va_para 16 senao va_para 10

    10: Faca ADD(A) va_para 11
    11: Faca ADD(B) va_para 12
    12: Faca SUB(C) va_para 13
    13: Se ZER(C) va_para 14 senao va_para 10
    14: Faca SUB(D) va_para 15
    15: Se ZER(D) va_para 16 senao va_para 4

    16: Se ZER(C) va_para 20 senao va_para 17
    17: Faca ADD(B) va_para 18
    18: Faca SUB(C) va_para 16

'''
def Mult_1(a, b):
    c = 0
    d = 0

    inst = 0


    print("\n--Instrucoes--\n\n")
    print("1: Faca ADD(D) va_para 2\n")
    print("2: Faca SUB(A) va_para 3\n")
    print("3: Se ZER(A) va_para 4 senao va_para 1\n\n")

    print("4: Faca ADD (A) va_para 5\n")
    print("5: Faca ADD(C) va_para 6\n")
    print("6: Faca SUB(B) va_para 7\n")
    print("7: Se ZER(B) va_para 8 senao va_para 4\n")
    print("8: Faca SUB(D) va_para 9\n")
    print("9: Se ZER(D) va_para 16 senao va_para 10\n\n")

    print("10: Faca ADD(A) va_para 11\n")
    print("11: Faca ADD(B) va_para 12\n")
    print("12: Faca SUB(C) va_para 13\n")
    print("13: Se ZER(C) va_para 14 senao va_para 10\n")
    print("14: Faca SUB(D) va_para 15\n")
    print("15: Se ZER(D) va_para 16 senao va_para 4\n\n")

    print("16: Se ZER(C) va_para 20 senao va_para 17\n")
    print("17: Faca ADD(B) va_para 18\n")
    print("18: Faca SUB(C) va_para 16\n")
    print("\n(A, B, C, D    Proxima instrucao)\n\n")

    while d != 0:
        if inst != 4:
            while a != 0:
                if inst == 0:
                    inst = 1
                elif inst == 1:
                    d += 1
                    inst = 2
                elif inst == 2:
                    a += -1
                    inst = 3
                elif inst == 3:
                    if A != 0:
                        inst = 1
                print ("(%i, %i, %i, %i    %i)\n", a, b, c, d, inst)

        ###################################################

        if inst == 3 and d != 0:
            inst = 4
            print("(%i, %i, %i, %i    %i)\n", a, b, c, d, inst)

        ##################################################

        if inst == 4 and d != 0:
            while b != 0:
                if inst == 4:
                    a += 1
                    inst = 5
                elif inst == 5:
                    c += 1
                    inst = 6
                elif inst == 6:
                    b += -1
                    inst = 7
                elif inst == 7:
                    if b == 0:
                        inst = 8
                    else:
                        inst = 4
                print ("(%i, %i, %i, %i    %i)\n", a, b, c, d, inst)

        ###################################################

        if inst == 7 and d != 0:
            inst = 8
            print ("(%i, %i, %i, %i    %i)\n", a, b, c, d, inst)
            d += -1
            inst = 9
            print ("(%i, %i, %i, %i    %i)\n", a, b, c, d, inst)
        if d == 0:
            inst = 16
            print ("(%i, %i, %i, %i    %i)\n", a, b, c, d, inst)
        else:
            inst = 10
            print ("(%i, %i, %i, %i    %i)\n", a, b, c, d, inst)

        ###################################################

        if inst == 10 and d != 0:
            while c != 0:
                if inst == 10:
                    a += 1
                    inst = 11
                elif inst == 11:
                    b += -1
                    inst = 12
                elif inst == 12:
                    c += -1
                    inst = 13
                elif inst == 13:
                    if c !=  0:
                        inst = 10
                print ("%i, %i, %i, %i    %i)\n", a, b, c, d, inst)
        inst = 14
        print("%i, %i, %i, %i    %i)\n", a, b, c, d, inst)
        
        ###################################################

        if inst == 14 and d != 0:
            d += -1
            inst = 15
            print ("(%i, %i, %i, %i    %i)\n", a, b, c, d, inst)
            if d == 0:
                inst = 16
            else:
                inst = 4
            print ("(%i, %i, %i, %i    %i)\n", a, b, c, d, inst)

        ###################################################

        if inst == 16 and c != 0:
            while c != 0:
                if inst == 16:
                    if c == 0:
                        inst = 20
                    else:
                        inst = 17
                elif inst == 17:
                    b += -1
                    inst = 18
                elif inst == 18:
                    c += -1
                    inst = 16
                print ("(%i, %i, %i, %i    %i)\n", a, b, c, d, inst)

    print("(%i, %i, %i, %i    20)\n", a, b, c, d)
