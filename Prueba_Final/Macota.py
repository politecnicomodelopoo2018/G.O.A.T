class mascota(object):
    nombre = None
    dueño = None


    def __init__(self,N,D):
        self.nombre=N
        self.dueño=D

    def saludar(self):
        pass
    def getNombre(self):
        return self.nombre
    def morido(self):
        return False
    def alimentarse(self):
        pass
