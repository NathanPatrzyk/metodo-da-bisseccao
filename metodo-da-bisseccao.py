from funcao import Funcao


def calcularBisseccao(f: Funcao, a: int, b: int, n: int):
    m = (a + b) / 2.0

    if n == 0:
        return m
    else:
        # CONTINUAR PROGRAMANDO A FUNÇÃO RECURSIVA ...


f = Funcao(1,0,-5,2)
print(str(f.a) + "x^3 + " + str(f.b) + "x^2 + " + str(f.c) + "x + " + str(f.d) + " = 0")
print(calcularBisseccao(f, -50, 50, 0))
