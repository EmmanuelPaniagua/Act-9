from particula import Particula

class Administrador:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostar(self):
        for particula in self.__particulas:
            print(particula)


l01 = Particula(id="2306", origen_x="34", origen_y="47", destino_x="90", destino_y="23", velocidad="80", red="90",  green="2", blue="34", distancia="")
Administrador = Administrador()
Administrador.agregar_inicio(l01)
Administrador.mostar()