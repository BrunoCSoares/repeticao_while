'''
Desenvolva um programa que recebe as notas dos alunos de uma turma. Seu programa deverá ser interrompido quando uma nota negativa for digitada.

Durante o processamento seu programa deverá contar o número de alunos nas seguintes condições:

- média abaixo de 3.5 (reprovados direto)

- média entre 3,5 e 7 (exame)

- acima de 7 (aprovados)

Calcule a média aritmética da turma e informe o resultado no final.

E exiba na tela a quantidade de alunos: reprovados direto, exame aprovado.
'''

somaMed = 0
somaQtd = 0
repro = 0
exame = 0
apro = 0

while True:
    nota = float(input("Insira a nota do aluno: "))
    if nota < 0:
        break
    elif nota <= 3.5:
        repro += 1
    elif nota <= 7:
        exame += 1
    elif nota > 7 and nota < 10:
        apro += 1
    else:
        print("Inválido")
        break
    somaQtd += 1
    somaMed += nota

if somaQtd != 0:
    media = somaMed / somaQtd

print(f"A média da turma foi {media}")
print(repro, "alunos foram reporvaos direto")
print(exame, "alunos ficaram para exame")
print(apro, "alunos foram aprovados")