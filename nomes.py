nome = input("Digite seu nome: ").title()
nome = nome.split()
nome_formatado = str()

quantidade = 0
for i in nome:
    quantidade += 1
    if i == 'Da' or i == 'Do' or i == 'Dos' or i == 'Das' or i == 'De' or i == 'E':
        i = i.lower()
    nome_formatado += str(i) + ' '

print(f'Quantidade de nomes: {quantidade}')
print(f'Nome formatado: {nome_formatado}')