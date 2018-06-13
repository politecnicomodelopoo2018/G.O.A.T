from Personas import  persones

class pasajeros(persones):

    vip = None
    necesidades = None

    def __init__(self, Nombre, Apellido, Fecha_nac, Dni, vip, necesidades):
        persones.__init__(Nombre, Apellido, Fecha_nac, Dni)

        self.vip = vip
        self.necesidades = necesidades

    def Dicc(self):

        diccionario={'Nombre':self.Nombre,
                     'Apellido':self.Apellido,
                     'Fecha_nac':self.Fecha_nac,
                     'Dni':self.Dni,
                     'Vip':self.vip,
                     'Necesidades':self.necesidades
                     }
        return diccionario

    def GetFecha(self):
        return self.Fecha_nac