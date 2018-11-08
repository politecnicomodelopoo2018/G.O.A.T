from Prueba_Final.Mascota import mascota
class Menu(object):
    def __init__(self):
        self.mascotas = []
        self.inicial()
    def inicial(self):
        print("1) ABM")
        print("2) Saludar")
        rta = int(input())
        if rta is 1:
            self.ABM()
        elif rta is 2:
            self.Saludar()
    def Saludar(self):
        print("Ingrese nombre de la mascota")
        mas = str(input())
        print("Ingresa tu nombre")
        dueno = str(input())

        for a in self.mascotas:
            j=False
            if a.Nombre == mas:
                if a.Dueno == dueno:
                    j = True
                if j :
                    print(a.saludar())
                else:
                    print(a.salduar_extrano())
        self.inicial()

    def ABM(self):
        print("1) Alta")
        print("2) Baja")
        print("3) Modificacion")
        rta = int(input())

        if rta is 1:
            self.Alta()
        if rta is 2:
            self.Baja()

        if rta is 3:
            self.Modif()



    def Alta(self):
        print("Ingrese Nombre")
        Nombre = str(input())
        print("Ingrese Dueno")
        Dueno = str(input())
        print("Ingrese Tipo")
        Tipo = str(input())

        a = mascota(Nombre,Dueno,Tipo)

        if Tipo == "Pajarito":
            print("¿Es cantor?(s/n)")
            rta = str(input())
            if rta == "s":
                print("Ingrese canto")
                canto = str(input())
                a.pajaro_cantor(True,canto)
        self.mascotas.append(a)

        self.inicial()

    def Baja(self):
        print("Ingrese Nombre")
        Nombre = str(input())
        print("Ingrese Dueno")
        Dueno = str(input())

        for a in self.mascotas:
            if a.Nombre == Nombre:
                if a.Dueno == Dueno:
                    self.mascotas.remove(a)
        self.inicial()

    def Modif(self):
        print("Ingrese Nombre")
        Nombre = str(input())
        print("Ingrese Dueno")
        Dueno = str(input())

        for a in self.mascotas:
            if a.Nombre == Nombre:
                if a.Dueno == Dueno:
                    print("Ingrese nuevo Nombre")
                    new_Nombre = str(input())
                    print("Ingrese nuevo Dueno")
                    new_Dueno = str(input())
                    a.modificar(new_Nombre,new_Dueno)
        self.inicial()






