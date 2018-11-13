class dueño(object):
    nombre = None

    def __init__(self,nombre):
        self.nombre=nombre

    def get_nombre(self):
        return self.nombre
    def modif(self,nombre):
        self.nombre=nombre