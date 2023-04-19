class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad    
    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
persona1 = Persona("Juan", 30)
persona2 = Persona("Ana", 25)
persona1.hablar()  # Hola, mi nombre es Juan y tengo 30 años.
persona2.hablar()  # Hola, mi nombre es Ana y tengo 25 años.
