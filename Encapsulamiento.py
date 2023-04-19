class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
        self.__edad = edad
persona1 = Persona("Juan", 30)
print(persona1.get_nombre())  # Juan
print(persona1.get_edad())    # 30
persona1.set_nombre("Pedro")
persona1.set_edad(25)
print(persona1.get_nombre())  # Pedro
print(persona1.get_edad())    # 25