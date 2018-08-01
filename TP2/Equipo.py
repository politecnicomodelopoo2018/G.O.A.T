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

    def Actualizar(self):
        a = db.connect("update Equipo set  Liga = %s , Fundacion = '%s' , Nombre = '%s' where Id_Equipo = %s;" %
                       (self.liga,self.fundacion,self.nombre,self.id_equipo))


    def Insert(self):
        a = db.connect("INSERT INTO `mydb`.`Equipo` (`Id_Equipo`, `Liga`, `Fundacion`, `Nombre`) VALUES (%s,%s,'%s','%s')"
                       % (self.id_equipo,self.liga,self.fundacion,self.nombre))

