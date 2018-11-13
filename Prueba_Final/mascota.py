class mascota(object):
    nombre = None
    dueño = None

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
