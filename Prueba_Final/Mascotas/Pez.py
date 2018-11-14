from Prueba_Final.mascota import mascota
class pez(mascota):
    vidas = 10
    def __init__(self,nombre,dueño):
        mascota.__init__(nombre,dueño)


    def saludar(self, nombre, nombre_dueño):
            if nombre_dueño == self.dueño.get_nombre():
                self.vidas-=1
            else:
                self.vidas=0

    def muerto(self):
        if self.vidas == 0:
            return True
        return False
