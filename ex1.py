'''
Desenvolva um programa que solicite números inteiros ao usuário e calcule a soma deles até que o 0 seja digitado.
'''

num = 8
soma = 0

while num != 0:
    num = int(input("Insira um número inteiro: "))
    soma += num

print(soma)