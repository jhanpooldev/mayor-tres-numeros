class OrdenadorTresNumeros:

    def __init__(self, numero1, numero2, numero3):
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3

    def ingresar_numeros(self):
        self.numero1 = int(input("Ingresa el primer número: "))
        self.numero2 = int(input("Ingresa el segundo número: "))
        self.numero3 = int(input("Ingresa el tercer número: "))

    def ordenar_numeros(self):
        self.numero1, self.numero2, self.numero3 = sorted([self.numero1, self.numero2, self.numero3])

    def imprimir_numeros(self, mensaje):
        print(f"{mensaje}: {self.numero1}, {self.numero2}, {self.numero3}")

if __name__ == "__main__":
    numero1 = 5
    numero2 = 10
    numero3 = 1

    numeros = OrdenadorTresNumeros(numero1, numero2, numero3)

    numeros.imprimir_numeros("Números desordenados")

    numeros.ordenar_numeros()

    numeros.imprimir_numeros("Números ordenados")

    print("\n ingresa tus  números:")
    numeros.ingresar_numeros()

    numeros.imprimir_numeros("Números desordenados")

    numeros.ordenar_numeros()

    numeros.imprimir_numeros("Números ordenados")

