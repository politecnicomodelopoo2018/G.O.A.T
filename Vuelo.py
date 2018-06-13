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

    def Ej_1(self):
        diccionario = {'Vuelo': [{'Pasajero': []}]}
        for a in self.pasajeros:
            diccionario['Vuelo'['Pasajero']].append(a.Dicc())

    def Ej_2(self):

        Menor = self.pasajeros[0]

        for a in self.pasajeros:
            # Ver encapsulamiento Pruscino
            if a.GetFecha < Menor.GetFecha:

                Menor = a
        Dicc={'Nombre':Menor.Nombre,
              'Apellido':Menor.Apellido,
              'Fecha_nac':Menor.Fecha_nac,
              'Dni':Menor.Dni}
        return Dicc


    def Ej_3(self):
        if len(self.tripulantes) < self.Avion.cantidad_de_tripulación_necesaria_para_volar:
            self.dicc={'Avion':self.Avion,
                  'Fecha_hora':self.Fecha_hora,
                  'Origen':self.Origen,
                  'Destino':self.Destino}
        return self.dicc

    def Ej_4(self):
        for a in self.tripulantes:
            if self.Avion.modelo not in a.Modelos:
                self.dic={'Avion':self.Avion,
                  'Fecha_hora':self.Fecha_hora,
                  'Origen':self.Origen,
                  'Destino':self.Destino}
        return self.dic

    def Ej_6(self):
        diccionario = {'Vuelo': [{'Pasajero': []}]}
        for a in self.pasajeros:
            if a.vip is not 0 and a.necesidades is not 'None':
                for a in self.pasajeros:
                    diccionario['Vuelo'['Pasajero']].append(a.Dicc())
        return diccionario


    def Ej_7(self):
        lista=[]
        for a in self.tripulantes:
            for b in a.Idiomas:
                if b not in lista:
                    lista.append(b)
        return lista





