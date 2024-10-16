'''
Escreva um programa que contenha o seguinte menu:

Opção 1: Verificar e exibir se um número x é ou não divisível por 6;

Opção 2: Calcular o fatorial do número x;

Opção 3: Exibir todos os inteiros de 1 até um número x.

O programa deverá solicitar ao usuário a leitura de um número x e a opção desejada até que o usuário digite “N” para encerrar o programa. OBS: o programa deverá solicitar o número e a opção enquanto do usuário escolha “S”.
'''

while True:
    continuar = input("Continuar? [s/n]: ")
    match continuar:
        case "s":
            pass
        case "n":
            break
        case _:
            print("Inválido!")
            break

    print("Opção 1: Verificar e exibir se um número x é ou não divisível por 6;")
    print("Opção 2: Calcular o fatorial do número x;")
    print("Opção 3: Exibir todos os inteiros de 1 até um número x.\n")

    num = int(input("Digite o número: "))
    opcao = int(input("Qual opção desejada? [1/2/3]: "))

    match opcao:
        case 1:
            if num % 6 == 0:
                print(f"O número {num} é divisível por 6.")
            else:
                print(f"O número {num} não é divisível por 6.")
        case 2:
            fatorial = 1
            for i in range(1, num + 1):
                fatorial *= i
            print(f"O fatorial de {num} é {fatorial}.")
        case 3:
            print(f"Os inteiros de 1 até {num} são: ", end="")
            for i in range(1, num + 1):
                print(i, end=" ")
            print()
        case _:
            print("Opção inválida!")
