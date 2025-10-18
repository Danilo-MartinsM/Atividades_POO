conversao = int(input('Digite o tipo de conversão quer fazer: \n1. Para decimal \n2. Para binário \n3. Para Hexadecimal \n'))
tipo = int(input('Digite em qual base o número está: \n1. Decimal \n2. Binário \n3. Octal \n4. Hexadecimal\n'))
numero = input('Digite o número: ')
numero_convertido = ''
base = 0

if tipo == 1:
   base = 10
elif tipo == 2:
   base = 2
elif tipo == 3:
   base = 8
elif tipo == 4:
   base = 16

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

numero_invertido = str(numero).upper()[::-1]
numero_convertido = 0

if conversao == 1: #Para Decimal
   if base == 16:
      for i in range(len(numero_invertido)):
         numero_convertido += hex_para_decimal[numero_invertido[i]] * (base ** i)
   else:
      for i in range(len(numero_invertido)):
         numero_convertido += int(numero_invertido[i]) * (base ** i)
   print('Em decimal:', numero_convertido)

elif conversao == 2: #Para binário
   numero = int(numero)
   while numero > 0:
      numero_convertido = str(numero % 2) + numero_convertido
      numero = numero // 2
   print('Em binário:', numero_convertido)

elif conversao == 3:  # Para hexadecimal
   numero = numero_convertido
   numero_convertido = ''
   while numero > 0:
      resto = numero % 16
      numero_convertido = decimal_para_hex[resto] + numero_convertido
      numero //= 16
   print('Em hexadecimal:', numero_convertido)


