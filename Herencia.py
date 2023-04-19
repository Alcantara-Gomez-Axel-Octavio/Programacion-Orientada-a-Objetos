class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        raise NotImplementedError("Subclase debe implementar este método abstracto")
class Perro(Animal):
    def hablar(self):
        return "Guau!"
class Gato(Animal):
    def hablar(self):
        return "Miau!"
perro = Perro("Fido")
gato = Gato("Garfield")
print(perro.nombre + ": " + perro.hablar())  # Fido: Guau!
print(gato.nombre + ": " + gato.hablar())    # Garfield: Miau!