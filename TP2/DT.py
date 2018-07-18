from persona import persona
from Equipo import equipo
from DB import db
class dt(persona):
    pass


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

    def Borrar(self,tabla,campo,contenido_campo):
        a = db.connect("delete from DT where Dni = %S",persona.dni)
     # if a = #algo :
      #      return 'Borrado con exito'

    def Actualizar(self):
        a = db.connect("update DT set Dni = %S ,Nombre = %S ,Apellido = %S ,Sueldo = %S,Fecha_nac = %S ,"
                       "Nacionalidad = %S ,Equipo = %S",
                       persona.dni,persona.nombre,persona.apellido,persona.sueldo,persona.fecha_nac,
                       persona.nacionalidad,persona.equipo)
