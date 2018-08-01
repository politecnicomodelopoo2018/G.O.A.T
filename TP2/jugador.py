from persona import persona
from Equipo import equipo
from DB import db
class jugador(persona):
    posicion = None

    def __init__(self,d,n,a,s,f,na,e,p):
        persona.__init__(self,d,n,a,s,f,na,e)
        self.posicion=p

    def Leer(self, equipo):
        a = db.connect("select * from Jugador",(equipo))
        lista = []
        listaEquipos = equipo.Leer()
        for b in a:
            for c in listaEquipos:
                if c.id_equipo == b['Equipo']:
                    j = jugador(b['Dni'],b['Nombre'],b['Apellido'],b['Sueldo'],b['Fecha_nac'],b['Nacionalidad']
                                ,b['Posicion'])

                    lista.append(j)
        return lista
    def Borrar(self):
        a = db.connect("delete from Jugador where Dni = %s ;" % self.dni)

    def Actualizar(self):
        a = db.connect("update Jugador set  Nombre = '%s' , Apellido = '%s' , Posicion = '%s' , Sueldo = %s , "
                       "Fecha_nac = '%s' , Nacionalidad = '%s', Equipo = %s where Dni = %s;" %
                       (self.nombre,self.apellido,self.posicion,self.sueldo,self.fecha_nac,
                       self.nacionalidad,self.equipo,self.dni))