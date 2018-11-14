from Prueba_Final.mascota import mascota
class perro(mascota):

    def saludar(self, nombre_dueño):
        saludo = "guau"*self.vidas
        if nombre_dueño == self.dueño.get_nombre():
            return saludo
        return saludo.upper()
    def entristeser(self):
        if self.vidas is not 1:
            self.vidas-=1