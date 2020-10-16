class Particula:
    def __init__(self, id=0, origen_x=0, 
                origen_y=0, destino_x=0, 
                destino_y=0, velocidad=0, 
                red=0, green=0, blue=0, distancia=0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia

    def __str__(self):
        return (
            'Id:  ' + str(self.__id) + '\n' +
            'Origen x:  ' + str(self.__origen_x) + '\n' +
            'Origen y:  ' + str(self.__origen_y) + '\n' +
            'Destino x:  ' + str(self.__destino_x) + '\n' +
            'Destino y:  ' + str(self.__destino_y) + '\n' +
            'Velocidad:  ' + str(self.__velocidad) + '\n' +
            'Red:  ' + str(self.__red) + '\n' +
            'Green:  ' + str(self.__green) + '\n' +
            'Blue:  ' + str(self.__blue) + '\n' +
            'Distancia:  ' + str(self.__distancia) + '\n'
            )

l01 = Particula(id=2306, origen_x=34, origen_y=47, 
                destino_x=90, destino_y=23, velocidad=80, red=90, 
                green=2, blue=34, distancia=5.0)
print(l01)