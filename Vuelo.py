class Vuelo(object):

    Avion = None
    Fecha_hora = None
    Origen = None
    Destino = None

    def __init__(self,Avion, Fecha_hora, Origen, Destino):

        self.Avion = Avion
        self.Fecha_hora = Fecha_hora
        self.Origen = Origen
        self.Destino = Destino
        self.pasajeros = []
        self.tripulantes = []
