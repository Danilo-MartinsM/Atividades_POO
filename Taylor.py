import math

angulo = float(input("Digite o angulo em graus: "))


class conversor:
    def anguloParaRadiano(self, angulo):
        return angulo * (math.pi / 180)
        
class Taylor:
    def cosseno(self, cos = 0, x = 0):
        converter = conversor()
        radiano = converter.anguloParaRadiano(x)
        for n in range(0, 10):
            cos += (-1) ** n / math.factorial(2 * n) * radiano ** (2 * n)
        return cos

    def seno(self, sen = 0, x = 0):
        converter = conversor()
        radiano = converter.anguloParaRadiano(x)
        for n in range(0, 10):
            sen += (-1) ** n / math.factorial(2 * n + 1) * radiano ** (2 * n + 1)
        return sen

    def tangente(self, tan = 0, x = 0):
        converter = conversor()
        radiano = converter.anguloParaRadiano(x)
        for n in range(0, 10):
            tan += ()

calculadora = Taylor()
cosseno = calculadora.cosseno(x=angulo)
seno = calculadora.seno(x=angulo)

print(f'COSSENO: {cosseno}')
print(f'SENO: {seno}')