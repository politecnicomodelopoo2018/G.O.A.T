from Prueba_Final.Dueño import dueño
from Prueba_Final.Pez import pez
class menu(object):

    def __init__(self):
        self.mascotas=[]
        self.inicial()

    def inicial(self):
        print("1) ABM")
        print("2) Saludar")
        print("3) Alimentarse")
        a = int(input())
        if a is 1:
            self.ABM()
        if a is 2:
            self.saludar()
        if a is 3:
            self.alimentarse()

    def ABM(self):
        print("1) Alta")
        print("2) Baja")
        print("3) Modif")
        a = int(input())
        if a is 1:
            self.Alta()

    def Alta(self):
        print("Ingresa tu nombre")
        Dnombre= str(input())
        print("Ingresa el nombre de la mascota")
        Mnombre=str(input())
        print("Ingresa el tipo de animal")
        tipo=str(input())
        d = dueño(Dnombre)
        if tipo == "Pez":
            m = pez(Mnombre,d)
        self.mascotas.append(m)
        self.inicial()
    def saludar(self):
        print("Ingrese Nombre de la mascota")
        Mn=str(input())
        print("Ingrese su nombre")
        Dn = str(input())
        for a in self.mascotas:
            a.saludar(Dn,Mn)
            if a.morido():
                self.mascotas.remove(a)
                print("Esta morido")
        self.inicial()
    def alimentarse(self):
        print("Ingrese Nombre de la mascota")
        Mn = str(input())
        for a in self.mascotas:
            if Mn == a.getNombre():
                a.alimentarse()
        self.inicial()

