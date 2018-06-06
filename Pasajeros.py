from Personas import  persones

class pasajeros(persones):

    vip = None
    necesidades = None

    def __init__(self, Nombre, Apellido, Fecha_nac, Dni, vip, necesidades):
        persones.__init__(Nombre, Apellido, Fecha_nac, Dni)

        self.vip = vip
        self.necesidades = necesidades

        