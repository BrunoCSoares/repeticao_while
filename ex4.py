'''
Faça um programa que verifique se uma "senha” numérica digitada pelo usuário está correta. O programa deve repetir o pedido até que o usuário escreva o valor correto. A senha correta deve estar definida no próprio programa.
'''

senha = int(input("Defina a senha: "))
tentativa = 0

while True:
    tentativa = int(input("Digite a senha: "))
    if tentativa != senha:
        print("Senha incorreta\n")
        continue
    else:
        print("Acesso liberado")
        break
