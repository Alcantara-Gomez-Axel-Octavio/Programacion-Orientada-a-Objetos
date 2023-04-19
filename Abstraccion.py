from abc import ABC, abstractmethod
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.1416 * self.radio ** 2
cuadrado = Cuadrado(5)
circulo = Circulo(3)
print(cuadrado.area())  # 25
print(circulo.area())   # 28.2744