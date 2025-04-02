"""
Módulo para ordenar tres números ingresados por el usuario.
"""


class OrdenadorTresNumeros:
    """
    Clase para manejar la entrada, ordenación e impresión de tres números.
    """

    def __init__(self, numero1, numero2, numero3):
        """Inicializa los tres números."""
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3

    def ingresar_numeros(self):
        """Solicita al usuario que ingrese tres números."""
        self.numero1 = int(input("Ingresa el primer número: "))
        self.numero2 = int(input("Ingresa el segundo número: "))
        self.numero3 = int(input("Ingresa el tercer número: "))

    def ordenar_numeros(self):
        """Ordena los números en orden ascendente."""
        self.numero1, self.numero2, self.numero3 = sorted(
            [self.numero1, self.numero2, self.numero3]
        )

    def imprimir_numeros(self, mensaje):
        """Imprime los números con un mensaje descriptivo."""
        print(f"{mensaje}: {self.numero1}, {self.numero2}, {self.numero3}")


if __name__ == "__main__":
    NUMERO_1 = 5
    NUMERO_2 = 10
    NUMERO_3 = 1

    numeros = OrdenadorTresNumeros(NUMERO_1, NUMERO_2, NUMERO_3)

    numeros.imprimir_numeros("Números desordenados")
    numeros.ordenar_numeros()
    numeros.imprimir_numeros("Números ordenados")

    print("\nIngresa tus números:")
    numeros.ingresar_numeros()

    numeros.imprimir_numeros("Números desordenados")
    numeros.ordenar_numeros()
    numeros.imprimir_numeros("Números ordenados")
