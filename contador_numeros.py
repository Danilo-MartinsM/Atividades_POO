import random
sequencia = []
repeticoes = int(input('Digite quantos numeros quer: '))
divisiveis = 0
par = 0
impar = 0
primo = 0
soma = 0
media = 0

for i in range(repeticoes):
    numero = random.randint(3, 99)
    sequencia.append(numero)
    soma = numero + soma
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

for i in sequencia:
    divisiveis = 0
    for c in range(1, i + 1):
        if i % c == 0:
            divisiveis += 1
    if divisiveis <= 2:
        primo += 1
    

media = soma / repeticoes

print(f'Sua sequencia é: {sequencia}')
print(f'Soma: {soma}')
print(f'Média: {media:.0f}')
print(f'Pares: {par}')
print(f'Ímpares: {impar}')
print(f'Primos: {primo}')