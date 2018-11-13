from Prueba_Final.mascota import mascota
class perro(mascota):

    def saludar(self,nombre,nombre_dueño):
        if nombre == self.nombre:
            if nombre_dueño == self.dueño.get_nombre():
                return"guau"
            return "GUAU"
