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

    def Leer(self):
        a = db.connect("select * from Equipo")
        lista = []
        listaLiga = liga.Leer(self)
        for b in a:
            for c in listaLiga:
                if c.id_liga == b['Liga']:
                    E = equipo(b['Id_Equipo'],c,b['Fundacion'],b['Nombre'])
                    lista.append(E)
        return lista


    def Borrar(self):
        a = db.connect("delete from Equipo where Id_Equipo = %s" % (self.id_equipo))
        #if a = #algo :
         #   return 'Borrado con exito'

    def Actualizar(self):
        a = db.connect("update Equipo set Id_Equipo  = %s and Liga = %s , Fundacion = %s , Nombre = %s ;" %
                       (self.id_equipo,self.liga,self.fundacion,self.nombre))

