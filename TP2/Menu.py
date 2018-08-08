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
        print('|3)       Modificar   |')
        print('|4)       Cargar      |')
        print('|5)       Crear       |')
        print('----------------------')

        a = int(input())

        if a == 1:
            self.MenuDelete()
        if a == 2:
            self.MenuInsert()
        if a == 3:
            self.MenuModificar()
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

            ligas = liga.Leer()

            for c in ligas:
                if b == c.nombre:
                    c.Borrar()

        if a == 2:
            b = input('Inserte el nombre del Equipo')

            equipos = equipo.Leer()

            for c in equipos:
                if b == c.nombre:
                    c.Borrar()

        if a == 3:

            b = input('Inserte el dni del Jogadore')

            jugadores = jugador.Leer()

            for c in jugadores:
                if b == c.dni:
                    c.Borrar()


        if a == 4:
            b = input('Inserte el dni del DT')

            Dts = dt.Leer()
            for c in Dts:
                if b == c.dni:
                    c.Borrar()

        self.MENU()


    def MenuCargar(self):

        print('---------MENU---------')
        print('|1)      Liga        |')
        print('|2)      Equipo      |')
        print('|3)      Jugador     |')
        print('|4)       DT         |')
        print('----------------------')

        a = int(input())

        if a == 1 :
            b = liga.Leer()

            for c in b :
                print(c.nombre)


        elif a == 2:

            b = equipo.Leer()

            for c in b:
                print(c.nombre)

        elif a == 3:
            b = jugador.Leer()

            for c in b:
                print(c.nombre)
        elif a == 4:
            b = dt.Leer()

            for c in b:
                print(c.nombre)


        self.MENU()
    def MenuModificar(self):
        print('---------MENU---------')
        print('|1)      Liga        |')
        print('|2)      Equipo      |')
        print('|3)      Jugador     |')
        print('|4)       DT         |')
        print('----------------------')


        a = int(input())
        if a == 1:
            ligas = liga.Leer()

            b = int(input('Inserte el id de la liga a modificar'))

            for c in ligas:
                if b == c.id_liga:
                    print('A continuacion los campos a modificar (0 = no modificar)')
                    id_liga = int(input('Id de la liga'))
                    nombre = str(input('nombre'))
                    pais = str(input('pais'))
                    division = str(input('division'))
                    cant_descensos = int(input('cant de descensos'))

                    if id_liga is not 0:
                        c.id_liga = id_liga
                    elif nombre is not 0:
                        c.nombre = nombre
                    elif pais is not 0 :
                        c.pais = pais
                    elif division is not 0:
                        c.cant_descensos = cant_descensos
                    c.Actualizar()




        if a == 2:
            equipos = equipo.Leer()
            b = int(input('Inserte el id del Equipo a modificar'))

            for c in equipos:
                if b == c.id_equipo:

                    print('A continuacion los campos a modificar (0 = no modificar)')

                    id_equipo = int(input('Id'))
                    fundacionin = str(input('fundacion'))
                    nombrein = str(input('nombre'))



                    if id_equipo is not 0:
                        c.id_equipo = id_equipo
                    elif fundacionin is not 0:
                        c.fundacion = fundacionin
                    elif nombrein is not 0:
                        c.nombre = nombrein

                    c.Actualizar()


        if a == 3:
            jugadores = jugador.Leer()
            b = int(input('Inserte el dni del Jogadore a modificar'))
            for c in jugadores:
                if b == c.dni:
                    print('Acontinuacion los campos a modificar (0 = no modificar)')

                    dni = input('dni')
                    nombre = input('nombre')
                    apellido = input('apellido')
                    sueldo = input('sueldo')
                    fecha_nac = input('fecha de nacimiento')
                    nacionalidad = input('nacionalidad')
                    equipoIN = input('equipo')
                    posicion = input('Posicion')

                    if dni is not 0:
                        c.dni = dni
                    elif nombre is not 0:
                        c.nombre = nombre
                    elif apellido is not 0:
                        c.apellido = apellido
                    elif sueldo is not 0:
                        c.sueldo = sueldo
                    elif fecha_nac is not 0:
                        c.fecha_nac = fecha_nac
                    elif nacionalidad is not 0:
                        c.nacionalidad = nacionalidad
                    elif equipoIN is not 0:
                        c.equipo = equipoIN
                    elif posicion is not 0:
                        c.posicion = posicion

                    c.Actualizar()


        if a == 4:
            dts = dt.Leer()
            b = int(input('Inserte el dni del DT a modificar'))
            for c in dts:
                if b == c.dni:

                    print('Acontinuacion los campos a modificar (0 = no modificar)')

                    dni = input('dni')
                    nombre = input('nombre')
                    apellido = input('apellido')
                    sueldo = input('sueldo')
                    fecha_nac = input('fecha de nacimiento')
                    nacionalidad = input('nacionalidad')
                    equipoIN = input('equipo')

                    if dni is not 0:
                        c.dni = dni
                    elif nombre is not 0:
                        c.nombre = nombre
                    elif apellido is not 0:
                        c.apellido = apellido
                    elif sueldo is not 0:
                        c.sueldo = sueldo
                    elif fecha_nac is not 0:
                        c.fecha_nac = fecha_nac
                    elif nacionalidad is not 0:
                        c.nacionalidad = nacionalidad
                    elif equipoIN is not 0:
                        c.equipo = equipoIN

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
