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
            continue
        case "n":
            break
        case _:
            print("Inválido: ")
            break
    print("Opção 1: Verificar e exibir se um número x é ou não divisível por 6;")
    print("Opção 2: Calcular o fatorial do número x;")
    print("Opção 3: Exibir todos os inteiros de 1 até um número x.\n")
    num = int(input("Digite o número: "))
    opcao = int(input("Qual opção desejada? [1/2/3]"))
    match opcao:
        case 1:
            if num % 6 == 0:
                print("O número é divisível por 6")
            else:
                print("O número não é divisível por 6")
        case 2:
            for