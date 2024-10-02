'''
Desenvolva um programa que solicite ao usuário números positivos até que o valor 0 seja pressionado. Em seguida, calcule a média aritmética de todos os números recebidos (exceto o número 0). Além disso, apresente o maior e o menor número digitado.
'''

somaPositivos = 0
qtdNumerosPositivos = 0
num = int(input("Digite um número positivo: "))

while num != 0:
    if num > 0:
        somaPositivos += num
        qtdNumerosPositivos += 1
        if qtdNumerosPositivos == 1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num

    num = int(input("Digite um número positivo: "))

mediaPositivos = somaPositivos/qtdNumerosPositivos
print(f"A media dos positicos é {mediaPositivos}")
print(f"O maior número positivo é {maior}")
print((f"O menor número positivo é {menor}"))