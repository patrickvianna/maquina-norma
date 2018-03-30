opcao = 1
while opcao > 0 :
    print("\n--- Menu ---\n")
    print("1 - Soma\n")
    print("2 - Multiplicao\n")
    print("3 - Fatorial\n")
    print("0 - Sair\n")
    opcao = int(input())

    if opcao == 1:
        A = 0
        B = 0

        print("\n--- Escolha o tipo ---\n\n")
        print("1 - Caso 1\nA:= A + B, onde registrador A armazena soma e B fica zerado.\n\n")
        print("2 - Caso 2\nA:= A + B usando C, onde registrador C armazena soma e A e B ficam zerados.\n\n")
        print("3 - Caso 3\nA:= A + B usando C, onde registrador A armazena a soma B tem seu valor original restaurado\ncom o auxilio do registrador C, e C fica zerado.\n\n")
        print("4 - Voltar para o menu\n")
        opcao = int(input())

        if opcao < 4 or opcao > 0:
            while A < 0:
                A = int(input("Inicialize o registrador A: "))
                if A < 0:
                    print("Digite um numero positivo.\n")

            while B < 0:
                B = int(input("Inicialize o registrador B: "))
                if B < 0:
                    print("Digite um numero positivo.\n")

            #CHAMADA
        
    elif opcao == 2:
        print("\n--- Escolha o tipo ---\n\n")
        print("1 - Caso 1\nA:= A * B usando C, D, onde o registrador A armazena o produto, B tem seu valor\nrestaurado, C e D ficam zerados\n\n")
        print("2 - Caso 2\nA:= A * B usando C, D, onde o registrador D armazena o produto, A e B ficam zerados, C fica\ncom algum resíduo.\n\n")
        print("4 - Voltar para o menu\n")
        opcao = int(input)

    elif opcao == 3:
        print("\n1 - Entrar com numero\n")
        print("\n4 - Voltar para o menu\n")
        opcao = int(input())
        if opcao == 1:
            A = 0
            while A <= 0 :
                A = int(input("Inicialize o registrador A: "))
                if A < 0 :
                    print("Digite um numero maior que zero.\n")


    elif opcao == 0:
        break