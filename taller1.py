class Calculadora:
    def _init_(self, n1, n2):
        self.n1 = float(n1)
        self.n2 = float(n2)

    def sumar(self):
        suma = self.n1 + self.n2
        print("el resultado de la suma es: ", suma)

    def restar(self):
        resta = self.n1 - self.n2
        print("el resultado de la resta es: ", resta)

    def multiplicar(self):
        multiplicacion = self.n1 * self.n2
        print("el resultado de la multiplicación es: ", multiplicacion)

    def dividir(self):
        division = self.n1 / self.n2
        print("el resultado de la división es: ", division)
