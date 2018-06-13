import json
from Avion import avion
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


    def JSON_Avion(self):
        with open('datos.json', 'r') as f:
            aux1=f.read()

            aux2=json.loads(aux1)

            for a in aux2['Aviones']:
                UnAvion=avion()






