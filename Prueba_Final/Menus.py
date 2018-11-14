from Prueba_Final.Mascotas.Perro import *
from Prueba_Final.Mascotas.Pajaro_Cantor import *
from Prueba_Final.Mascotas.Pajaro import *
from Prueba_Final.Mascotas.Pez import *
from Prueba_Final.Mascotas.Gato import *
from Prueba_Final.Dueño import *

class menu(object):
    mascotas = []
    dueños = []
    @staticmethod
    def iniciar():
        gato = ("""\
                  |\---/|
                  | o_o |           
                   \_^_/ """)
        perro = ("""\
                       __      _
                     o'')}____//
                      `_/      )
                      (_(_/-(_/ """)
        print(gato+"\n"+perro)

        print("--------------------------")
        print("|       1) ABM           |")
        print("|       2) Saludar       |")
        print("|       3) Alimentarse   |")
        print("--------------------------")
        rta = int(input())

        if rta == 1:
            menu.ABM(menu)
        elif rta == 2:
            menu.Saludar(menu)
        elif rta == 3:
            menu.Alimentarse(menu)

    def ABM(self):
        print("--------------------------")
        print("|       1) Alta          |")
        print("|       2) Baja          |")
        print("|       3) Modif         |")
        print("--------------------------")
        rta = int(input())
        if rta == 1:
            self.Alta(menu)
        elif rta == 2:
            self.Baja(menu)
        elif rta == 3:
            self.Modif(menu)

    def Alta(self):
        print("--------------------------")
        print("|    Ingrese su nombre   |")
        print("--------------------------")
        Nombre_dueño = str(input())

        print("---------------------------------------")
        print("|   Ingrese el nombre de la mascota   |")
        print("---------------------------------------")
        Nombre_mascota = str(input())

        print("---------------------------------------")
        print("|     Ingrese el tipo de  mascota     |")
        print("---------------------------------------")
        Tipo_mascota = str(input())

        dueñoo = dueño(Nombre_dueño)
        if Tipo_mascota == "Perro":
            masc = perro(Nombre_mascota,dueñoo)
        elif Tipo_mascota == "Gato":
            masc = gato(Nombre_mascota,dueñoo)
        elif Tipo_mascota == "Pajaro":
            masc = pajaro(Nombre_mascota,dueñoo)
        elif Tipo_mascota == "Pajaro cantor":

            print("---------------------------------------")
            print("|     Ingrese el canto                |")
            print("---------------------------------------")
            canto = str(input())

            masc = pajaro_cantor(Nombre_mascota,dueñoo,canto)

        elif Tipo_mascota == "Pez":
            masc = pez(Nombre_mascota,dueñoo)
        self.mascotas.append(masc)
        self.dueños.append(dueñoo)
        self.iniciar()

    def Baja(self):
        print("--------------------------")
        print("|       1) Dueño         |")
        print("|       2) Mascota       |")
        print("--------------------------")
        rta = int(input())

        if rta == 1:
            self.Baja_Dueño(menu)
        elif rta == 2:
            self.Baja_Mascota(menu)
        self.iniciar()

    def Baja_Dueño(self):
        print("--------------------------")
        print("|    Ingrese su nombre   |")
        print("--------------------------")
        Nombre = str(input())
        for a in self.dueños:
            if Nombre == a.get_nombre():
                self.dueños.remove(a)

    def Baja_Mascota(self):
        print("--------------------------")
        print("|    Ingrese su nombre   |")
        print("--------------------------")
        Nombre_dueño = str(input())

        print("----------------------------------------")
        print("|    Ingrese el nombre de la mascota   |")
        print("----------------------------------------")
        Nombre_mascota = str(input())

        for a in self.mascotas:
            if a.get_nombre() == Nombre_mascota:
                if a.get_dueño().nombre == Nombre_dueño:
                    self.mascotas.remove(a)
                    print("¡Mascota borrada!")
                else:
                    print("¡Usted no es el dueño regitrado!")
                    self.iniciar()

    def Modif(self):
        print("--------------------------")
        print("|       1) Dueño         |")
        print("|       2) Mascota       |")
        print("--------------------------")
        rta = int(input())
        if rta == 1:
            self.Modif_dueño(menu)
        elif rta == 2:
            self.Modif_mascota(menu)
        self.iniciar()

    def Modif_dueño(self):
        print("--------------------------")
        print("|    Ingrese su nombre   |")
        print("--------------------------")
        Nombre = str(input())

        print("--------------------------------")
        print("|    Ingrese su nuevo nombre   |")
        print("--------------------------------")
        Nuevo_nombre = str(input())

        for a in self.dueños:
            if a.get_nombre == Nombre:
                a.modif(Nuevo_nombre)
                print("¡Usuario actualizado con exito!")
            else:
                print("No se encuentra registrado")

    def Modif_mascota(self):
        print("--------------------------")
        print("|    Ingrese su nombre   |")
        print("--------------------------")
        Nombre_dueño = str(input())

        print("----------------------------------------")
        print("|    Ingrese el nombre de la mascota   |")
        print("----------------------------------------")
        Nombre_mascota = str(input())

        for a in self.mascotas:
            if a.get_nombre() == Nombre_mascota:
                if a.get_dueño().nombre == Nombre_dueño:

                        print("-----------------------------------")
                        print("|       1) Cambiar dueño          |")
                        print("|       2) Modif mascota          |")
                        print("-----------------------------------")
                        rta = int(input())

                        if rta == 1:
                            print("--------------------------")
                            print("|    Ingrese su nombre   |")
                            print("--------------------------")
                            Nombre_dueño = str(input())

                            for b in self.dueños:
                                if b.get_nombre()==Nombre_dueño:
                                    a.mod_dueño(b)
                                else:
                                    print("Usted no esta registrado")
                                    self.iniciar()
                        elif rta == 2:
                            print("----------------------------------------------")
                            print("|    Ingrese el nuevo nombre de la mascota   |")
                            print("----------------------------------------------")
                            Nombre_mascota = str(input())
                            a.mod_nombre(Nombre_mascota)
                            print("¡Nombre modificado con exito!")

    def Saludar(self):

        print("--------------------------")
        print("|    Ingrese su nombre   |")
        print("--------------------------")
        Nombre_dueño = str(input())

        print("----------------------------------------")
        print("|    Ingrese el nombre de la mascota   |")
        print("----------------------------------------")
        Nombre_mascota = str(input())

        for a in self.mascotas:
            if a.get_nombre() ==  Nombre_mascota:
                print(a.saludar(Nombre_dueño))
            if a.get_nombre_dueño() is not Nombre_dueño:
                if a.nombre_clase() == "pez":
                    if a.muerto():
                        print("Se murió")
                        self.mascotas.remove(a)
            a.entristeser()
        self.iniciar()

    def Alimentarse(self):
        print("----------------------------------------")
        print("|    Ingrese el nombre de la mascota   |")
        print("----------------------------------------")
        Nombre_mascota = str(input())

        for a in self.mascotas:
            if a.get_nombre() == Nombre_mascota:
                a.alimentarse()
        self.iniciar()





















