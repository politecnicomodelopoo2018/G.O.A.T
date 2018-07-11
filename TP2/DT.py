from persona import persona
from Equipo import equipo
from DB import db
class dt(persona):
    pass


    def AllDT(self):
        a = db.connect("select * from DT")
        lista = []
        listaEquipos = equipo.AllEquipos()
        for b in a:
            for c in listaEquipos:
                if c.id_equipo == b['Equipo']:
                    DT = dt(b['Dni'], b['Nombre'], b['Apellido'], b['Sueldo'], b['Fecha_nac'], b['Nacionalidad'])

                    lista.append(DT)
        return lista