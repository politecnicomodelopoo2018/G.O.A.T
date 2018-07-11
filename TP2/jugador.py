from persona import persona
from Equipo import equipo
from DB import db
class jugador(persona):
    posicion = None

    def __init__(self,d,n,a,s,f,na,e,p):
        persona.__init__(d,n,a,s,f,na,e)
        self.posicion=p

    def AllJugadores(self,equipo):
        a = db.connect("select * from Jugador",(equipo))
        lista = []
        listaEquipos = equipo.AllEquipos()
        for b in a:
            for c in listaEquipos:
                if c.id_equipo == b['Equipo']:
                    j = jugador(b['Dni'],b['Nombre'],b['Apellido'],b['Sueldo'],b['Fecha_nac'],b['Nacionalidad']
                                ,b['Posicion'])

                    lista.append(j)
        return lista