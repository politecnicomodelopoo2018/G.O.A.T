from datetime import datetime


import json
from Avion import avion
from Vuelo import Vuelo
from Pasajeros import pasajeros
from Tripulantes import tripulantes
class Arolinea(object):

    Nombre = 'FlyEmirates'

    Diccionario = {'1': [],
                   '2': [],
                   '3': [],
                   '4': [],
                   '5': [],
                   '6': [],
                   '7': []}



    def __init__(self):

        self.Aviones=[]
        self.Vuelos=[]

    def Ejerecicios(self):
        self.Ej_1()
        self.Ej_2()
        self.Ej_3()
        self.Ej_4()
        self.Ej_5()
        self.Ej_6()
        self.Ej_7()
        return self.Diccionario
    def Ej_1(self):
        for a in self.Vuelos:
            self.Diccionario['1'].append(a.Ej_1())

    def Ej_2(self):
        for a in self.Vuelos:
            self.Diccionario['2'].append(a.Ej_2())

    def Ej_3(self):
        for a in self.Vuelos:
            self.Diccionario['3'].append(a.Ej_3())

    def Ej_4(self):
        for a in self.Vuelos:
            self.Diccionario['4'].append(a.Ej_4())

    def Ej_5(self):
        for a in self.Vuelos:
            for b in self.Vuelos[1:]:
                if a != b:
                    if a.Fecha == b.Fecha:
                        for c in a.tripulantes:
                            for d in b.tripulantes:
                                if c.Dni == d.Dni:
                                    self.Diccionario['5'].append(c.Retornar())



    def Ej_6(self):
        for a in self.Vuelos:
            self.Diccionario['6'].append(a.Ej_6())

    def Ej_7(self):
        for a in self.Vuelos:
            self.Diccionario['7'].append(a.Ej_7())


    def JSON(self):
        self.JSON_Avion()
        self.JSON_Vuelos()
        self.JSON_Persona()
        self.JSON_Avion_en_Vuelos()

    def JSON_Avion(self):
        with open('datos.json', 'r') as f:
            aux1=f.read()

            aux2=json.loads(aux1)

            for a in aux2['Aviones']:
                UnAvion=avion()
                UnAvion.modelo=a['codigoUnico']
                UnAvion.cant_pasajeros_que_pueden_viajar = a['cantidadDePasajerosMaxima']
                UnAvion.Tripulacionecesaria = a['cantidadDeTripulaciónNecesaria']
                self.Aviones.append(UnAvion)


    def JSON_Vuelos(self):
        with open('datos.json', 'r') as f:
            aux1 = f.read()

            aux2 = json.loads(aux1)
            for a in aux2['Vuelos']:
                for b in self.Aviones:
                    if b.modelo == a['avion']:
                        UnVuelo=Vuelo(b,datetime.strptime(a['fecha'], '%Y-%m-%d'),a['hora'],a['origen'],a['destino'])
                        UnVuelo.pasajeros=a['pasajeros']
                        UnVuelo.tripulantes=a['tripulacion']
                        self.Vuelos.append(UnVuelo)

    def JSON_Avion_en_Vuelos(self):
        for a in self.Vuelos:
            for b in self.Aviones:
                if a.Avion == b.modelo:
                    a.Avion=b



    def JSON_Persona(self):
        self.Pasajeros = []
        self.Tripulantes = []
        with open('datos.json', 'r') as f:
            aux1 = f.read()

            aux2 = json.loads(aux1)
            for a in aux2['Personas']:
                if a['tipo'] == 'Pasajero':
                    if 'solicitudesEspeciales' in a:
                        UnPasaj=pasajeros(a['nombre'],a['apellido'],datetime.strptime(a['fechaNacimiento'], '%Y-%m-%d').date(),a['dni'],a['vip'],a['solicitudesEspeciales'])
                        self.Pasajeros.append(UnPasaj)
                    else:
                        UnPasaj = pasajeros(a['nombre'], a['apellido'],datetime.strptime(a['fechaNacimiento'], '%Y-%m-%d').date(), a['dni'], a['vip'],
                                            'Ninguna')
                        self.Pasajeros.append(UnPasaj)

                else :

                    if 'idiomas' in a:
                        UnTripu=tripulantes(a['nombre'],a['apellido'],datetime.strptime(a['fechaNacimiento'], '%Y-%m-%d').date(),a['dni'])
                        UnTripu.Modelos=a['avionesHabilitados']
                        UnTripu.Idiomas=a['idiomas']
                        self.Tripulantes.append(UnTripu)
                    else:
                        UnTripu = tripulantes(a['nombre'], a['apellido'],datetime.strptime(a['fechaNacimiento'], '%Y-%m-%d').date(), a['dni'])
                        UnTripu.Modelos = a['avionesHabilitados']
                        UnTripu.Idiomas =''
                        self.Tripulantes.append(UnTripu)

        self.JSON_Persona_parte_2(self.Pasajeros,self.Tripulantes)

    def JSON_Persona_parte_2(self,pasaj,tripu):
        for a in self.Vuelos:
            lista=[]
            for b in a.pasajeros:
                for c in pasaj:
                    if b == c.Dni:
                        lista.append(c)

            a.pasajeros=lista

        for a in self.Vuelos:
            lista=[]
            for b in a.tripulantes:
                for c in tripu:
                    if b == c.Dni:
                        lista.append(c)

            a.tripulantes=lista










