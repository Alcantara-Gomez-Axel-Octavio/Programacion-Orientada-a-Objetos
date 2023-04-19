class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
#Un objeto y accedemos a sus atributos
persona1 = Persona("Juan", 25)
print(persona1.nombre)  # Imprime "Juan"
print(persona1.edad)    # Imprime 25