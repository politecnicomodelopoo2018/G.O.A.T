class mascota(object):
    def __init__(self,N,D,T):
        self.Nombre = str(N)
        self.Dueno = str(D)
        self.Tipo = str(T)
        self.Saludo_extrano = None
        self.Saludo = None
        self.saludos()



    def saludos(self):
        if self.Tipo == "Pajarito":
            self.Saludo = "pio"
        if self.Tipo == "Perro":
            self.Saludo = "guau"
        if self.Tipo == "Gato":
            self.Saludo = "miau"
        self.Saludo_extrano = self.Saludo.upper()






    def pajaro_cantor(self,r,S):
        self.Cantor = r
        self.Saludo  = S
        if self.Cantor:
            self.Saludo_extrano = ""

    def modificar(self,N,D):
        self.Nombre = N
        self.Dueno = D


    def saludar(self):
        return self.Saludo

    def salduar_extrano(self):
        return self.Saludo_extrano
