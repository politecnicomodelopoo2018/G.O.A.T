from Liga import liga
from Equipo import equipo
from jugador import jugador
from DT import dt
from DB import db
from PIL import Image
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
        print('|5)       Sorpresa    |')
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

        elif a == 5:
            self.Sorpresa()
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
            self.MostrarLiga()
            b = int(input('Inserte el id de la liga'))

            ligas = liga.Leer()

            for c in ligas:
                if b == c.id_liga:
                    c.Borrar()
        if a == 2:
            self.MostrarEquipo()
            b = int(input('Inserte el id del Equipo'))

            equipos = equipo.Leer()

            for c in equipos:
                if b == c.id_equipo:
                    c.Borrar()
        if a == 3:
            self.MostrarJugador()

            b = int(input('Inserte el dni del Jogadore'))

            jugadores = jugador.Leer()

            for c in jugadores:
                if b == c.dni:
                    c.Borrar()
        if a == 4:
            self.MostrarDT()
            b = int(input('Inserte el dni del DT'))

            Dts = dt.Leer()
            for c in Dts:
                if b == c.dni:
                    c.Borrar()
        if a == 5 :
            a = db.connect('delete from Liga;')
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
                id_insertada = int(input('Inserte el id de la liga'))
                lista = liga.Leer()

                for y in lista:
                    if y.id_liga == id_insertada:
                        t.add_row([y.id_liga, y.nombre,y.pais,y.division,y.cant_descensos])

            elif op == 2:
                self.MostrarLiga()


        elif a == 2:
            print('---------MENU---------')
            print('|1)      Un Equipo   |')
            print('|2)      Todos       |')
            print('----------------------')

            op = int(input())
            t = PrettyTable(['id_equipo','liga','fundacion','nombre'])

            if op == 1:
                id_insertada = int(input('Inserte el id del equipo'))
                lista = equipo.Leer()
                for y in lista:
                    if y.id_equipo == id_insertada:
                        t.add_row([y.id_equipo,y.liga.nombre,y.fundacion,y.nombre])
            elif op == 2:
                self.MostrarEquipo()
        elif a == 3:
            print('---------MENU---------')
            print('|1)      Un Jugador  |')
            print('|2)      Todos       |')
            print('----------------------')

            op = int(input())
            t = PrettyTable(['dni','nombre','apellido','sueldo','fecha_nac','nacionalidad','equipo','posicion'])
            if op == 1:
                dni_insertado= int(input('Inserte el dni del jugador'))
                lista = jugador.Leer()

                for y in lista:
                    if y.dni == dni_insertado:
                        t.add_row([y.dni,y.nombre,y.apellido,'$'+y.sueldo,y.fecha_nac,y.nacionalidad,y.equipo.nombre,y.posicion])
            elif op == 2:
               self.MostrarJugador()


        elif a == 4:
            print('---------MENU---------')
            print('|1)      Un DT       |')
            print('|2)      Todos       |')
            print('----------------------')

            op = int(input())
            t = PrettyTable(['dni','nombre','apellido','sueldo','fecha_nac','nacionalidad','equipo'])
            if op == 1:
                lista = dt.Leer()
                dni_insertado = int(input('Inserte el dni del DT'))
                for y in lista:
                    if y.dni == dni_insertado:
                        t.add_row([y.dni, y.nombre, y.apellido,'$'+y.sueldo, y.fecha_nac, y.nacionalidad, y.equipo.nombre])

            elif op == 2:
                self.MostrarDT()
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
            self.MostrarLiga()
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
                    if nombre_liga is not 0:
                        c.nombre = nombre_liga
                    if pais_liga is not 0 :
                        c.pais = pais_liga
                    if division_liga is not 0:
                        c.division = division_liga
                    if cant_descensos_liga is not 0:
                        c.cant_descensos = cant_descensos_liga

                    c.Actualizar()
        if a == 2:
            equipos_leidos = equipo.Leer()
            self.MostrarEquipo()
            b = int(input('Inserte el id del Equipo a modificar'))

            for c in equipos_leidos:
                if b == c.id_equipo:

                    print('A continuacion los campos a modificar (0 = no modificar)')

                    id_equipo_equipo = int(input('Id'))
                    fundacion_equipo = str(input('fundacion'))
                    nombre_equipo = str(input('nombre'))



                    if id_equipo_equipo is not 0:
                        c.id_equipo = id_equipo_equipo

                    if fundacion_equipo is not '0':
                        c.fundacion = fundacion_equipo

                    if nombre_equipo is not '0':
                        c.nombre = nombre_equipo

                    c.Actualizar()
        if a == 3:
            jugadores_leidos = jugador.Leer()
            self.MostrarJugador()
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
                    if nombre_jugador is not 0:
                        c.nombre = nombre_jugador
                    if apellido_jugador is not 0:
                        c.apellido = apellido_jugador
                    if sueldo_jugador is not 0:
                        c.sueldo = sueldo_jugador
                    if fecha_nac_jugador is not 0:
                        c.fecha_nac = fecha_nac_jugador
                    if nacionalidad_jugador is not 0:
                        c.nacionalidad = nacionalidad_jugador
                    if equipo_jugador is not 0:
                        c.equipo = equipo_jugador
                    if posicion_jugador is not 0:
                        c.posicion = posicion_jugador

                    c.Actualizar()
        if a == 4:
            dts = dt.Leer()
            self.MostrarDT()
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
                        print('hola')
                        c.dni = dni_DT
                    if nombre_DT is not 0:
                        print('hola')
                        c.nombre = nombre_DT
                    if apellido_DT is not 0:
                        print('hola')
                        c.apellido = apellido_DT
                    if sueldo_DT is not 0:
                        print('hola')
                        c.sueldo = sueldo_DT
                    if fecha_nac_DT is not 0:
                        print('hola')
                        c.fecha_nac = fecha_nac_DT
                    if nacionalidad_DT is not 0:
                        print('hola')
                        c.nacionalidad = nacionalidad_DT
                    if equipo_DT is not 0:
                        print('hola')
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
            print('A continuacion los campos del equipo')
            id_equipo_equipo = int(input('Id'))
            liga_equipo = int(input('Liga(ID)'))
            fundacion_equipo = str(input('fundacion'))
            nombre_equipo = str(input('nombre'))

            new_equipo = equipo(id_equipo_equipo,liga_equipo,fundacion_equipo,nombre_equipo)
            new_equipo.Insert()
        if a == 3:
            print('A continuacion los campos del jugador')
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
            print('A continuacion los campos del DT')
            dni_DT = int(input('dni'))
            nombre_DT = str(input('nombre'))
            apellido_DT = str(input('apellido'))
            sueldo_DT = int(input('sueldo'))
            fecha_nac_DT = str(input('fecha de nacimiento'))
            nacionalidad_DT = str(input('nacionalidad'))
            equipo_DT = int(input('equipo'))

            new_dt = dt(dni_DT,nombre_DT,apellido_DT,sueldo_DT,fecha_nac_DT,nacionalidad_DT,equipo_DT)
            new_dt.Insert()
        self.MENU()
    def Sorpresa(self):
        imagen = Image.open("P.jpg")
        imagen.show()

    def MostrarLiga(self):
        ligas_leidas = liga.Leer()
        t = PrettyTable(['id_liga', 'nombre', 'pais', 'division', 'cant_descensos'])
        for y in ligas_leidas:
            t.add_row([y.id_liga, y.nombre, y.pais, y.division, y.cant_descensos])
        print(t)
        b = int(input('Inserte el id de la liga a modificar'))
    def MostrarEquipo(self):
        equipos_leidos = equipo.Leer()
        t = PrettyTable(['id_equipo', 'liga', 'fundacion', 'nombre'])
        for y in equipos_leidos:
            t.add_row([y.id_equipo, y.liga.nombre, y.fundacion, y.nombre])
        print(t)
    def MostrarJugador(self):
        t = PrettyTable(['dni', 'nombre', 'apellido', 'sueldo', 'fecha_nac', 'nacionalidad', 'equipo', 'posicion'])
        lista = jugador.Leer()
        for y in lista:
            t.add_row(
                [y.dni, y.nombre, y.apellido, '$' + y.sueldo, y.fecha_nac, y.nacionalidad, y.equipo.nombre,y.posicion])
        print(t)
    def MostrarDT(self):
        t = PrettyTable(['dni', 'nombre', 'apellido', 'sueldo', 'fecha_nac', 'nacionalidad', 'equipo'])
        lista = dt.Leer()
        for y in lista:
            if y.dni == dni_insertado:
                t.add_row(
                [y.dni, y.nombre, y.apellido, '$' + y.sueldo, y.fecha_nac, y.nacionalidad, y.equipo.nombre])
        print(t)