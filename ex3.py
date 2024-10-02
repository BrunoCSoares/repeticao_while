'''
Mostrar todos os inteiros entre dois números digitados pelo usuário. Exemplo: usuário digita os números 8 e 15, e aparecem em tela: 9, 10, 11, 12, 13, 14.
'''

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

if inicio < fim:
    cont = inicio + 1
    while cont <= fim - 1:
        print(cont)
        cont += 1
else:
    print("O início deve ser maior que o fim")