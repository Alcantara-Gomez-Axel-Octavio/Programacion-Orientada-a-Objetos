class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.1416 * (self.radio ** 2)
# Creamos un objeto de la clase Circulo y llamamos a su método
circulo1 = Circulo(5)
print(circulo1.area())  # Imprime 78.53975