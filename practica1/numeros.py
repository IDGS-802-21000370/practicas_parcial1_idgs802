import os

class NumerosLista:
    # Declaración de propiedades
    numeros = []

    # Declaración de constructor
    def __init__(self):
        pass

    # Declaración de métodos de clase
    def ordenar_numeros(self):
        for i in range(10):
            n = input(f"Ingrese el número {i + 1}: ")
            numero = int(n)
            self.numeros.append(numero)

        self.numeros.sort()
        print("Números ordenados = ", self.numeros)

    def numeros_pares(self):
        pares = set()
        for numero in self.numeros:
            if numero % 2 == 0:
                pares.add(numero)

        print("Números pares = ", list(pares))

    def numeros_impares(self):
        impares = set()
        for numero in self.numeros:
            if numero % 2 != 0:
                impares.add(numero)

        print("Números impares = ", list(impares))


def main():
    os.system("cls")
    obj = NumerosLista()
    obj.ordenar_numeros()
    obj.numeros_pares()
    obj.numeros_impares()


if __name__ == "__main__":
    main()
