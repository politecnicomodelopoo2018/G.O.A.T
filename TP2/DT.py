from persona import persona
from Equipo import equipo
from DB import db
class dt(persona):



    def Leer(self):
        a = db.connect("select * from DT")
        lista = []
        listaEquipos = equipo.Leer()
        for b in a:
            for c in listaEquipos:
                if c.id_equipo == b['Equipo']:
                    DT = dt(b['Dni'], b['Nombre'], b['Apellido'], b['Sueldo'], b['Fecha_nac'], b['Nacionalidad'])

                    lista.append(DT)
        return lista

    def Borrar(self):
        a = db.connect("delete from DT where Dni = %s" % self.dni)

    def Actualizar(self):
        a = db.connect("update DT set Nombre = '%s' ,Apellido = '%s' ,Sueldo = %s ,Fecha_nac = %s ,"
                       "Nacionalidad = '%s' ,Equipo = %s where Dni = %s;" %
                       (self.nombre,self.apellido,self.sueldo,self.fecha_nac,
                       self.nacionalidad,self.equipo,self.dni))
