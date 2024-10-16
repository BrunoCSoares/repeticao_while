'''
Desenvolva um programa que solicite números inteiros ao usuário e calcule a soma deles até que o 0 seja digitado.
'''

soma = 0

num = int(input("Insira um número inteiro: "))

while num != 0:
    soma += num
    num = int(input("Insira um número inteiro: "))

print(soma)