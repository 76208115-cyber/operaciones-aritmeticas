class OperacionesAritmeticas:
    def __init__(self, numero1=0, numero2=0):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar_dos_numeros(self):
        return self.numero1 + self.numero2


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

operaciones = OperacionesAritmeticas(numero1, numero2)
print("La suma es: ", operaciones.sumar_dos_numeros())
