class Habitacion:
    def __init__(self, metros_cuadrados):
        self.metros_cuadrados = metros_cuadrados
class Casa:
    def __init__(self, habitaciones):
        self.habitaciones = habitaciones
    def calcular_metros_cuadrados(self):
        total_metros_cuadrados = 0
        for habitacion in self.habitaciones:
            total_metros_cuadrados += habitacion.metros_cuadrados
        return total_metros_cuadrados
# Creamos dos objetos de la clase Habitacion
habitacion1 = Habitacion(15)
habitacion2 = Habitacion(20)
# Creamos un objeto de la clase Casa con las dos habitaciones
casa1 = Casa([habitacion1, habitacion2])
# Calculamos el total de metros cuadrados de la casa
total_metros_cuadrados = casa1.calcular_metros_cuadrados()
print(f"La casa tiene un total de {total_metros_cuadrados} metros cuadrados.")