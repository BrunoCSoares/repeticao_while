'''
O dono de uma mercearia da zona rural do interior de SP necessita automatizar o processo de totalização das compras de seus clientes, porém ele não tem condições financeiras para adquirir os equipamentos necessários para leitura de códigos de barras e afins. Dessa forma, o funcionário do caixa terá que digitar os preços dos produtos e as quantidades para que as compras dos clientes sejam totalizadas. Escreva

um programa que calcule o total da compra do cliente, sendo que o usuário deverá digitar os preços e as quantidades dos produtos e, quando a compra terminar, digitar 0 (zero) no valor do preço para finalizar e informar o valor a pagar ao cliente.
'''

total_compra = 0

while True:
    preco = float(input("Digite o preço do produto (ou 0 para finalizar): "))
    if preco == 0:
        break
    quantidade = int(input("Digite a quantidade do produto: "))
    total_compra += preco * quantidade

print(f"Valor total a pagar: R$ {total_compra:.2f}")
