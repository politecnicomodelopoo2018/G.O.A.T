from Liga import liga
from DB import db
class equipo():

    id_equipo = None
    liga = None
    fundacion = None
    nombre = None


    def __init__(self,id,l,f,n):
        self.id_equipo=id
        self.liga=l
        self.fundacion=f
        self.nombre=n

    def AllEquipos(self):
        a = db.connect("select * from Equipo")
        lista = []
        listaLiga = liga.AllLigas(self)
        for b in a:
            for c in listaLiga:
                if c.id_liga == b['Liga']:
                    E = equipo(b['Id_Equipo'],c,b['Fundacion'],b['Nombre'])
                    lista.append(E)
        return lista


