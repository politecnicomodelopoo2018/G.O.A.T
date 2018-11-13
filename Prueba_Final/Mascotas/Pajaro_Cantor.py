from Prueba_Final.mascota import mascota
class pajaro_cantor(mascota):
    canto = None
    def __init__(self,nombre,dueño,canto):
        mascota.__init__(nombre,dueño)
        self.canto=canto

    def saludar(self, nombre, nombre_dueño):
        if nombre == self.nombre:
            if nombre_dueño == self.dueño.get_nombre():
                return self.canto
            return ""
