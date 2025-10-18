conversao = int(input('Digite o tipo de conversão quer fazer: \n1. Para decimal \n2. Para binário \n3. Para Hexadecimal \n'))
tipo = int(input('Digite em qual base o número está: \n1. Binário \n2. Octal \n3. Hexadecimal\n'))
numero = int(input('Digite o numero: '))
numero_convertido = ''
base = 0
if tipo == 1:
   base = 2
elif tipo == 2:
   base = 8
elif tipo == 3:
   base = 16
decimal = 0
decimal_para_hex = {
    0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
    6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B",
    12: "C", 13: "D", 14: "E", 15: "F"
}
hex_para_decimal = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
}

if base == 16:
    numero_invertido = str(numero).upper()[::-1]
else:
    numero_invertido = [int(x) for x in str(numero)[::-1]]

if conversao == 1:
   for i in range(len(numero_invertido)):
      decimal += numero_invertido[i] * (tipo ** i)
   print(decimal)
elif conversao == 2:
   while True:
      numero_convertido = str(numero % 2) + numero_convertido
      numero = numero // 2
      if numero == 0:
         break
elif conversao != 1 and conversao != 2:
    print('Digite um número válido!!')
print(numero_convertido)
      




