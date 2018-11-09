from Prueba_Final.Macota import mascota
class pez(mascota):
    vidas = 10




    def saludar(self,d,n):
        if d == self.dueño.getNombre() and n == self.dueño.getNombre():
            if self.vidas is not 0:
                self.vidas-=1
        else:
            self.vidas=0

    def alimentarse(self):
        self.vidas+=1

    def morido(self):
        if self.vidas == 0:
            return True
        return False
