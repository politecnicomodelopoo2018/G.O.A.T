from Personas import  persones

class tripulantes (persones):

    def __init__(self,Nombre, Apellido, Fecha_nac, Dni):
        persones.__init__(Nombre, Apellido, Fecha_nac, Dni)

        self.Idiomas = []
        self.Modelos = []






