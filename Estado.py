class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
persona1 = Persona("Juan", 30)
persona1.hablar()  # Hola, mi nombre es Juan y tengo 30 años.
persona1.edad = 31
persona1.hablar()  # Hola, mi nombre es Juan y tengo 31 años.