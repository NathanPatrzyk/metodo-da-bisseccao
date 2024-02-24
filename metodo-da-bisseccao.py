from funcao import Funcao


def calcularBisseccao(f, a, b, n):
    m = (a + b) / 2.0

    if n == 0:
        return m
    if (f.calcularValor(a)*f.calcularValor(m)) < 0:
        return calcularBisseccao(f, a, m, n-1)
    else:
        return calcularBisseccao(f, m, b, n-1)


f = Funcao(1, 0, -4, 8)
print(str(f.a) + "x^3 + " + str(f.b) + "x^2 + " + str(f.c) + "x + " + str(f.d) + " = 0")
print()

solucao = calcularBisseccao(f, -50, 50, 0)
print("Solução encontrada com 0 iterações: x = " + str(solucao))
print("Teste da solução encontrada com 0 iterações: f(" + str(solucao) + ") = " + str(f.calcularValor(solucao)))
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