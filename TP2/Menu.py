from Liga import liga
from Equipo import equipo
from jugador import jugador
from DT import dt

class Menu(object):


    def __init__(self):


        self.MENU()

    def MENU(self):
        print('---------MENU---------')
        print('|1)       Delete      |')
        print('|2)       Insert      |')
        print('|3)       Update      |')
        print('|4)       Cargar      |')
        print('|5)       Crear       |')
        print('----------------------')

        a = int(input())

        if a == 1:
            self.MenuDelete()
        if a == 2:
            self.MenuInsert()
        if a == 3:
            self.MenuUpdate()
        if a == 4 :
            self.MenuCargar()


    def MenuDelete(self):

        print('---------MENU---------')
        print('|1)      Liga        |')
        print('|2)      Equipo      |')
        print('|3)      Jugador     |')
        print('|4)       DT         |')
        print('|5)       Todo       |')
        print('----------------------')

        a = int(input())

        if a == 1:
            b = input('Inserte el nombre de la liga')

            for c in self.ligas:
                if b == c.nombre:
                    c.Borrar()

        if a == 2:
            b = input('Inserte el nombre del Equipo')

            for c in self.Equipos:
                if b == c.nombre:
                    c.Borrar()

        if a == 3:
            b = input('Inserte el dni del Jogadore')
            for c in self.Jugadores:
                if b == c.dni:
                    c.Borrar()

        if a == 4:
            b = input('Inserte el dni del DT')
            for c in self.DTs:
                if b == c.dni:
                    c.Borrar()

        self.MENU()


    def MenuCargar(self):

        print('---------MENU---------')
        print('|1)      Liga        |')
        print('|2)      Equipo      |')
        print('|3)      Jugador     |')
        print('|4)       DT         |')
        print('|5)       Todo       |')
        print('----------------------')

        a = int(input())

        if a == 1 :
            self.ligas = liga.Leer()

        elif a == 2:

            self.Equipos = equipo.Leer()
        elif a == 3:
            self.Jugadores = jugador.Leer()
        elif a == 4:
            self.DTs = dt.Leer()

        elif a == 5:
            self.ligas = liga.Leer()
            self.Equipos = equipo.Leer()
            self.Jugadores = jugador.Leer()
            self.DTs = dt.Leer()

        self.MENU()
    def MenuUpdate(self):
        print('---------MENU---------')
        print('|1)      Liga        |')
        print('|2)      Equipo      |')
        print('|3)      Jugador     |')
        print('|4)       DT         |')
        print('----------------------')


        a = int(input())
        if a == 1:
            b = input('Inserte el nombre de la liga')

            for c in self.Ligas:
                if b == c.nombre:
                    c.Actualizar()

        if a == 2:
            b = input('Inserte el nombre del Equipo')

            for c in self.Equipos:
                if b == c.nombre:
                    c.Actualizar()

        if a == 3:
            b = input('Inserte el dni del Jogadore')
            for c in self.Jugadores:
                if b == c.dni:
                    c.Actualizar()

        if a == 4:
            b = input('Inserte el dni del DT')
            for c in self.DTs:
                if b == c.dni:
                    c.Actualizar()

        self.MENU()

    def MenuInsert(self):
        print('---------MENU---------')
        print('|1)      Liga        |')
        print('|2)      Equipo      |')
        print('|3)      Jugador     |')
        print('|4)       DT         |')
        print('----------------------')

        a = int(input())
        if a == 1:
            b = input('Inserte el nombre de la liga')

            for c in self.Ligas:
                if b == c.nombre:
                    c.Insert()

        if a == 2:
            b = input('Inserte el nombre del Equipo')

            for c in self.Equipos:
                if b == c.nombre:
                    c.Insert()

        if a == 3:
            b = input('Inserte el dni del Jogadore')
            for c in self.Jugadores:
                if b == c.dni:
                    c.Insert()

        if a == 4:
            b = input('Inserte el dni del DT')
            for c in self.DTs:
                if b == c.dni:
                    c.Insert()

        self.MENU()
