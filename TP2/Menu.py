from Liga import liga
from Equipo import equipo
from jugador import jugador
from DT import dt
from prettytable import PrettyTable
class Menu(object):


    def __init__(self):


        self.MENU()
    def MENU(self):
        print('---------MENU---------')
        print('|1)       Delete      |')
        print('|2)       Insert      |')
        print('|3)       Modificar   |')
        print('|4)       Mostrar     |')
        print('|5)       Crear       |')
        print('----------------------')

        a = int(input())

        if a == 1:
            self.MenuDelete()
        elif a == 2:
            self.MenuInsert()
        elif a == 3:
            self.MenuModificar()
        elif a == 4 :
            self.MenuMostrar()
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
    def MenuMostrar(self):

        print('---------MENU---------')
        print('|1)      Liga        |')
        print('|2)      Equipo      |')
        print('|3)      Jugador     |')
        print('|4)       DT         |')
        print('----------------------')

        a = int(input())

        if a == 1 :

            print('---------MENU---------')
            print('|1)      Una Liga    |')
            print('|2)      Todas       |')
            print('----------------------')

            op = int(input())
            t = PrettyTable(['id_liga', 'nombre', 'pais', 'division', 'cant_descensos'])
            if op == 1:
                id_insertada = input('Inserte el id de la liga')
                lista = liga.Leer()

                for y in lista:
                    if y.id_liga == id_insertada:
                        t.add_row([y.id_liga, y.nombre,y.pais,y.division,y.cant_descensos])

            elif op == 2:
                lista = liga.Leer()

                for y in lista:
                        t.add_row([y.id_liga, y.nombre, y.pais, y.division, y.cant_descensos])
            print(t)


        elif a == 2:
            print('---------MENU---------')
            print('|1)      Un Equipo   |')
            print('|2)      Todos       |')
            print('----------------------')

            op = int(input())
            t = PrettyTable(['id_equipo','liga','fundacion','nombre'])

            if op == 1:
                id_insertada = input('Inserte el id del equipo')
                lista = equipo.Leer()
                for y in lista:
                    if y.id_equipo == id_insertada:
                        t.add_row([y.id_equipo,y.liga,y.fundacion,y.nombre])
            elif op == 2:
                lista = equipo.Leer()
                for y in lista:
                        t.add_row([y.id_equipo, y.liga, y.fundacion, y.nombre])
            print(t)
        elif a == 3:
            print('---------MENU---------')
            print('|1)      Un Jugador  |')
            print('|2)      Todos       |')
            print('----------------------')

            op = input()
            t = PrettyTable(['dni','nombre','apellido','sueldo','fecha_nac','nacionalidad','equipo','posicion'])
            if op == 1:
                dni_insertado= input('Inserte el dni del jugador')
                lista = jugador.Leer()

                for y in lista:
                    if y.dni == dni_insertado:
                        t.add_row([y.dni,y.nombre,y.apellido,y.sueldo,y.fecha_nac,y.nacionalidad,y.equipo,y.posicion])
            elif op == 2:
                lista = jugador.Leer()

                for y in lista:
                        t.add_row([y.dni, y.nombre, y.apellido, y.sueldo, y.fecha_nac, y.nacionalidad, y.equipo, y.posicion])
            print(t)


        elif a == 4:
            print('---------MENU---------')
            print('|1)      Un DT       |')
            print('|2)      Todos       |')
            print('----------------------')

            op = input()
            t = PrettyTable(['dni','nombre','apellido','sueldo','fecha_nac','nacionalidad','equipo'])
            if op == 1:
                lista = dt.Leer()
                dni_insertado = input('Inserte el dni del DT')
                for y in lista:
                    if y.dni == dni_insertado:
                        t.add_row([y.dni, y.nombre, y.apellido, y.sueldo, y.fecha_nac, y.nacionalidad, y.equipo])

            elif op == 2:
                lista = dt.Leer()
                for y in lista:
                        t.add_row([y.dni, y.nombre, y.apellido, y.sueldo, y.fecha_nac, y.nacionalidad, y.equipo])
            print(t)

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
            ligas_leidas = liga.Leer()

            b = int(input('Inserte el id de la liga a modificar'))

            for c in ligas_leidas:
                if b == c.id_liga:
                    print('A continuacion los campos a modificar (0 = no modificar)')
                    id_liga_liga = int(input('Id de la liga'))
                    nombre_liga = str(input('nombre'))
                    pais_liga = str(input('pais'))
                    division_liga = str(input('division'))
                    cant_descensos_liga = int(input('cant de descensos'))

                    if id_liga_liga is not 0:
                        c.id_liga = id_liga_liga
                    elif nombre_liga is not 0:
                        c.nombre = nombre_liga
                    elif pais_liga is not 0 :
                        c.pais = pais_liga
                    elif division_liga is not 0:
                        c.division = division_liga
                    elif cant_descensos_liga is not 0:
                        c.cant_descensos = cant_descensos_liga

                    c.Actualizar()
        if a == 2:
            equipos_leidos = equipo.Leer()
            b = int(input('Inserte el id del Equipo a modificar'))

            for c in equipos_leidos:
                if b == c.id_equipo:

                    print('A continuacion los campos a modificar (0 = no modificar)')

                    id_equipo_equipo = int(input('Id'))
                    fundacion_equipo = str(input('fundacion'))
                    nombre_equipo = str(input('nombre'))



                    if id_equipo_equipo is not 0:
                        c.id_equipo = id_equipo_equipo
                    elif fundacion_equipo is not 0:
                        c.fundacion = fundacion_equipo
                    elif nombre_equipo is not 0:
                        c.nombre = nombre_equipo

                    c.Actualizar()
        if a == 3:
            jugadores_leidos = jugador.Leer()
            b = int(input('Inserte el dni del Jogadore a modificar'))

            for c in jugadores_leidos:
                if b == c.dni:
                    print('Acontinuacion los campos a modificar (0 = no modificar)')

                    dni_jugador = int(input('dni'))
                    nombre_jugador = str(input('nombre'))
                    apellido_jugador = str(input('apellido'))
                    sueldo_jugador = int(input('sueldo'))
                    fecha_nac_jugador = str(input('fecha de nacimiento'))
                    nacionalidad_jugador = str(input('nacionalidad'))
                    equipo_jugador = int(input('equipo'))
                    posicion_jugador = str(input('Posicion'))

                    if dni_jugador is not 0:
                        c.dni = dni_jugador
                    elif nombre_jugador is not 0:
                        c.nombre = nombre_jugador
                    elif apellido_jugador is not 0:
                        c.apellido = apellido_jugador
                    elif sueldo_jugador is not 0:
                        c.sueldo = sueldo_jugador
                    elif fecha_nac_jugador is not 0:
                        c.fecha_nac = fecha_nac_jugador
                    elif nacionalidad_jugador is not 0:
                        c.nacionalidad = nacionalidad_jugador
                    elif equipo_jugador is not 0:
                        c.equipo = equipo_jugador
                    elif posicion_jugador is not 0:
                        c.posicion = posicion_jugador

                    c.Actualizar()
        if a == 4:
            dts = dt.Leer()
            b = int(input('Inserte el dni del DT a modificar'))
            for c in dts:
                if b == c.dni:

                    print('Acontinuacion los campos a modificar (0 = no modificar)')

                    dni_DT = int(input('dni'))
                    nombre_DT = str(input('nombre'))
                    apellido_DT = str(input('apellido'))
                    sueldo_DT = int(input('sueldo'))
                    fecha_nac_DT = str(input('fecha de nacimiento'))
                    nacionalidad_DT = str(input('nacionalidad'))
                    equipo_DT = int(input('equipo'))

                    if dni_DT is not 0:
                        c.dni = dni_DT
                    elif nombre_DT is not 0:
                        c.nombre = nombre_DT
                    elif apellido_DT is not 0:
                        c.apellido = apellido_DT
                    elif sueldo_DT is not 0:
                        c.sueldo = sueldo_DT
                    elif fecha_nac_DT is not 0:
                        c.fecha_nac = fecha_nac_DT
                    elif nacionalidad_DT is not 0:
                        c.nacionalidad = nacionalidad_DT
                    elif equipo_DT is not 0:
                        c.equipo = equipo_DT

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
            print('A continuacion los campos de la liga' )
            id_liga_liga = int(input('Id de la liga'))
            nombre_liga = str(input('nombre'))
            pais_liga = str(input('pais'))
            division_liga = str(input('division'))
            cant_descensos_liga = int(input('cant de descensos'))

            new_liga = liga(id_liga_liga,nombre_liga,pais_liga,division_liga,cant_descensos_liga)
            new_liga.Insert()
        if a == 2:
            id_equipo_equipo = int(input('Id'))
            fundacion_equipo = str(input('fundacion'))
            nombre_equipo = str(input('nombre'))

            new_equipo = equipo(id_equipo_equipo,fundacion_equipo,nombre_equipo)
            new_equipo.Insert()
        if a == 3:
            dni_jugador = int(input('dni'))
            nombre_jugador = str(input('nombre'))
            apellido_jugador = str(input('apellido'))
            sueldo_jugador = int(input('sueldo'))
            fecha_nac_jugador = str(input('fecha de nacimiento'))
            nacionalidad_jugador = str(input('nacionalidad'))
            equipo_jugador = int(input('equipo'))
            posicion_jugador = str(input('Posicion'))

            new_jugador = jugador(dni_jugador,nombre_jugador,apellido_jugador,sueldo_jugador,fecha_nac_jugador,nacionalidad_jugador,equipo_jugador,posicion_jugador)
            new_jugador.Insert()
        if a == 4:
            dni_DT = int(input('dni'))
            nombre_DT = str(input('nombre'))
            apellido_DT = str(input('apellido'))
            sueldo_DT = int(input('sueldo'))
            fecha_nac_DT = str(input('fecha de nacimiento'))
            nacionalidad_DT = str(input('nacionalidad'))
            equipo_DT = int(input('equipo'))

            new_dt = dt(dni_DT,nombre_DT,apellido_DT,sueldo_DT,fecha_nac_DT,nacionalidad_DT,equipo_DT)

        self.MENU()
