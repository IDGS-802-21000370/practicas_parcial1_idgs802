import math
import os

class DistanciaNumeros():
    # Declaración de propiedades
    punto1X = 0.0
    punto1Y = 0.0
    punto2X = 0.0
    punto2Y = 0.0


    # Declaración de constructor
    def __init__(self, x1, y1, x2, y2):
        self.punto1X = x1
        self.punto1Y = y1
        self.punto2X = x2
        self.punto2Y = y2

    # Declaración de métodos de clase
    def formula_distancia(self):
        return math.sqrt((self.punto2X - self.punto1X)**2 + (self.punto2Y - self.punto1Y)**2)


def main():
    os.system("cls")
    x = DistanciaNumeros(2, 6, 7, 10)
    print(x.formula_distancia())


if __name__ == "__main__":
    main()
