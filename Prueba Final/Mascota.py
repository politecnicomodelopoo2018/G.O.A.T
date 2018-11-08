class mascota(object):

    Nombre = None
    Dueno = None
    Saludo = None
    Saludo_extrano = None
    Tipo = None

    def __init__(self,N,D,T):
        self.Nombre = N
        self.Dueno = D
        self.Tipo = T

        if self.Tipo is "Pajarito":
            self.Saludo = "pio"
        elif self.Tipo is "Perro":
            self.Saludo = "guau"
        elif self.Tipo is "Gato":
            self.Saludo = "miau"

        self.Saludo_extrano = self.Saludo.upper()



    def pajaro_cantor(self,r,S):
        self.Cantor = r
        self.Saludo  = S
        if self.Cantor:
            self.Saludo_extrano = None

    def modificar(self,N,D):
        self.Nombre = N
        self.Dueno = D


    def saludar(self):
        return self.Saludo

    def salduar_extrano(self):
        return self.Saludo_extrano
