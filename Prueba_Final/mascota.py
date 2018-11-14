class mascota(object):
    nombre = None
    dueño = None
    vidas = 3

    def __init__(self,nombre,dueño):
        self.nombre=nombre
        self.dueño=dueño


    def saludar(self):
        pass
    def get_nombre(self):
        return self.nombre
    def get_dueño(self):
        return self.dueño
    def mod_dueño(self,dueño):
        self.dueño=dueño
    def mod_nombre(self,nombre):
        self.nombre=nombre
    def get_nombre_dueño(self):
        return self.dueño.get_nombre()
    def alimentarse(self):
        self.vidas += 1
    def nombre_clase(self):
        return type(self).__name__