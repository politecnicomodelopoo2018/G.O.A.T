class persones(object):
    Nombre=None
    Apellido=None
    Fecha_nac = None
    Dni = None

    def __init__(self, Nombre, Apellido, Fecha_nac, Dni):

        self.Nombre = Nombre
        self.Apellido= Apellido
        self.Fecha_nac = Fecha_nac
        self.Dni = Dni


    def Retornar(self):
        Dicc = {'Nombre': self.Nombre,
                'Apellido': self.Apellido,
                'Fecha_nac': str(self.Fecha_nac),
                'Dni': self.Dni}
        return Dicc

