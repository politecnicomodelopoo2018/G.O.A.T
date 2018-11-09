from Prueba_Final.Macota import mascota
class pez(mascota):
    vidas = 1


    def saludar(self,d):
        if d.getNombre == self.dueño.getNombre():
            if self.vidas is not 0:
                self.vidas-=1
        else:
            self.vidas=0

    def alimentarse(self):
        self.vidas+=1

    def morido(self):
        if self.vidas is 0:
            return True
        return False
