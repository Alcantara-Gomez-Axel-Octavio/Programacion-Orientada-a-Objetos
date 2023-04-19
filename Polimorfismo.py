class Animal:
    def hablar(self):
        pass
class Perro(Animal):
    def hablar(self):
        return "Guau guau"
class Gato(Animal):
    def hablar(self):
        return "Miau miau"
class Vaca(Animal):
    def hablar(self):
        return "Muu muu"
# Función que acepta un objeto de tipo Animal y llama a su método hablar
def hacer_hablar(animal):
    print(animal.hablar())
# Creamos diferentes objetos de tipo Animal
perro = Perro()
gato = Gato()
vaca = Vaca()
# Llamamos a la función hacer_hablar con cada uno de los objetos
hacer_hablar(perro)  # Imprime "Guau guau"
hacer_hablar(gato)   # Imprime "Miau miau"
hacer_hablar(vaca)   # Imprime "Muu muu"