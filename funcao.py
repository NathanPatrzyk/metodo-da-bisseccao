class Funcao:
    def __init__(self, a, b, c, d):
        # f(x) = ax^3 + bx^2 + cx + d
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d

    def setA(self, a):
        self.__a = a
    def getA(self):
        return self.__a

    def setB(self, b):
        self.__b = b
    def getB(self):
        return self.__b

    def setC(self, c):
        self.__c = c
    def getC(self):
        return self.__c

    def setD(self, d):
        self.__d = d
    def getD(self):
        return self.__d

    a = property(getA, setA)
    b = property(getB, setB)
    c = property(getC, setC)
    d = property(getD, setD)
