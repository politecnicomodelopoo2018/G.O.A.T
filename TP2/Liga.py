from DB import db
class liga():

    id_liga = None
    nombre = None
    pais = None
    division = None
    cant_descensos = None

    def __init__(self,id,n,p,d,c):
        self.id_liga=id
        self.nombre=n
        self.pais=p
        self.division=d
        self.cant_descensos=c


    def Leer(self):
        a = db.connect("select * from Liga")
        lista = []
        for b in a:
            L = liga(b['Id_Liga'],b['Nombre'],b['Pais'],b['Division'],b['Cant_descensos'])
            lista.append(L)

        return lista

    def Borrar(self):
        a = db.connect("delete from Liga where Id_Liga = %s"% (self.id_liga))
        #if a = #algo :
         #   return 'Borrado con exito'

    def Actualizar(self):
        a = db.connect("update Liga set Pais = '%s' , Division = '%s' , Cant_descensos  = %s , Nombre = '%s' where Id_Liga = %s ; " % (self.pais,self.id_liga,self.division,self.cant_descensos,self.nombre,self.id_liga))


    def Insert(self):

        a = db.connect("INSERT INTO `mydb`.`Liga` (`Pais`, `Id_Liga`, `Division`, `Cant_descensos`, `Nombre`) VALUES ('%s',%s,'%s',%s,'%s')" % (self.pais,self.id_liga,self.division,self.cant_descensos,self.nombre))