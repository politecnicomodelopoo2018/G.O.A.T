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
            self.Diccionario['1'].append(a.Dicc())

    def Ej_2(self):
        for a in self.Vuelos:
            self.Diccionario['2'].append(a.EJ_2)

    def Ej_3(self):
        for a in self.Vuelos:
            self.Diccionario['3'].append(a.EJ_3)

    def Ej_4(self):
        for a in self.Vuelos:
            self.Diccionario['4'].append(a.EJ_4)

    def Ej_5(self):
        for a in self.Vuelos:
            for b in self.Vuelos:
                if a.Fecha == b.Fecha:
                    for c in a.tripulantes:
                        for d in b.tripulantes:
                            if c.Dni == d.Dni:
                                self.Diccionario['5'].append(c.Retornar())


    def Ej_6(self):
        for a in self.Vuelos:
            self.Diccionario['6'].append(a.EJ_6)

    def Ej_7(self):
        for a in self.Vuelos:
            self.Diccionario['7'].append(a.EJ_7)


    def JSON(self):

        self.JSON_Vuelos()
        self.JSON_Persona()

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

                UnVuelo=Vuelo(a['avion'],a['fecha'],a['hora'],a['origen'],a['destino'])
                UnVuelo.pasajeros=a['pasajeros']
                UnVuelo.tripulantes=a['tripulacion']
                self.Vuelos.append(UnVuelo)

    def JSON_Persona(self):
        Pasajeros = []
        Tripulantes = []
        with open('datos.json', 'r') as f:
            aux1 = f.read()

            aux2 = json.loads(aux1)
            for a in aux2['Personas']:
                if a['tipo'] == 'Pasajero':
                    UnPasaj=pasajeros(a['nombre'],a['apellido'],a['fechaNacimiento'],a['dni'],a['vip'],a['solicitudesEspeciales'])
                    Pasajeros.append(UnPasaj)
                else :
                    UnTripu=tripulantes(a['nombre'],a['apellido'],a['fechaNacimiento'],a['dni'])
                    UnTripu.Modelos=a['avionesHabilitados']
                    UnTripu.Idiomas=a['idiomas']
                    Tripulantes.append(UnTripu)
        self.JSON_Persona_parte_2(Pasajeros,Tripulantes)

    def JSON_Persona_parte_2(self,pasaj,tripu):
        for a in self.Vuelos:
            for b in a.pasajeros:
                for c in pasaj:
                    if b == c.Dni:
                        a.pasajeros[b]=c

        for a in self.Vuelos:
            for b in a.tripulantes:
                for c in tripu:
                    if b == c.Dni:
                        a.tripulantes[b]=c








