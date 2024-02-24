from funcao import Funcao


def calcularBisseccao(f, a, b, n):

    fa = f.calcularValor(a)
    fb = f.calcularValor(b)

    while n > 0:

        m = (a + b) / 2.0

        fm = f.calcularValor(m)

        if fa*fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm

        n = n-1

    return m


f = Funcao(1, 0, -4, 8)
print(str(f.a) + "x^3 + " + str(f.b) + "x^2 + " + str(f.c) + "x + " + str(f.d) + " = 0")
print()

solucao = calcularBisseccao(f, -50, 50, 1)
print("Solução encontrada com 1 iteração: x = " + str(solucao))
print("Teste da solução encontrada com 1 iteração: f(" + str(solucao) + ") = " + str(f.calcularValor(solucao)))
print()

solucao = calcularBisseccao(f, -50, 50, 5)
print("Solução encontrada com 5 iterações: x = " + str(solucao))
print("Teste da solução encontrada com 5 iterações: f(" + str(solucao) + ") = " + str(f.calcularValor(solucao)))
print()

solucao = calcularBisseccao(f, -50, 50, 10)
print("Solução encontrada com 10 iterações: x = " + str(solucao))
print("Teste da solução encontrada com 10 iterações: f(" + str(solucao) + ") = " + str(f.calcularValor(solucao)))
print()

solucao = calcularBisseccao(f, -50, 50, 20)
print("Solução encontrada com 20 iterações: x = " + str(solucao))
print("Teste da solução encontrada com 20 iterações: f(" + str(solucao) + ") = " + str(f.calcularValor(solucao)))
print()