class Vuelo(object):
    Avion = None
    Fecha= None
    Hora=None
    Origen = None
    Destino = None

    def __init__(self, Avion, Fecha,hora, Origen, Destino):
        self.Avion = Avion
        self.Fecha = Fecha
        self.Hora=hora
        self.Origen = Origen
        self.Destino = Destino
        self.pasajeros = []
        self.tripulantes = []
        self.dik={}
        self.dic={}

    def Ej_1(self):
        diccionario = {'Vuelo': [{'Pasajero': []}]}
        for a in self.pasajeros:
            diccionario['Vuelo'][0]['Pasajero'].append(a.Dicc())
        return diccionario

    def Ej_2(self):

        Menor = self.pasajeros[0]

        for a in self.pasajeros:

            if a.Fecha_nac > Menor.Fecha_nac:

                Menor = a
        Dicc={'Nombre':Menor.Nombre,
              'Apellido':Menor.Apellido,
              'Fecha_nac':str(Menor.Fecha_nac),
              'Dni':Menor.Dni}
        return Dicc


    def Ej_3(self):

        if len(self.tripulantes) < self.Avion.Tripulacionecesaria:
            self.dik={'Avion':self.Avion.modelo,
                  'Fecha':str(self.Fecha),
                  'Hora':self.Hora,
                  'Origen':self.Origen,
                  'Destino':self.Destino}
        return self.dik

    def Ej_4(self):
        for a in self.tripulantes:
            if self.Avion.modelo not in a.Modelos:
                self.dic={'Avion':self.Avion.modelo,
                  'Fecha':str(self.Fecha),
                  'Hora':self.Hora,
                  'Origen':self.Origen,
                  'Destino':self.Destino}
        return self.dic

    def Ej_6(self):
        diccionario = {'Vuelo': [{'Pasajero': []}]}
        for a in self.pasajeros:
            if a.vip is not 0 and a.necesidades is not 'Ninguna':
                for a in self.pasajeros:
                    diccionario['Vuelo'][0]['Pasajero'].append(a.Dicc())
        return diccionario


    def Ej_7(self):
        lista=[]
        dic={'Origen':self.Origen,
             'Destino':self.Destino,
             'Idiomas':[]}
        for a in self.tripulantes:
            for b in a.Idiomas:
                if b not in lista and b:
                    dic['Idiomas'].append(b)
                    lista.append(b)
        return dic





