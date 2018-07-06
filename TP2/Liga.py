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

    def insert(self):
        book =
        #db.connect("INSERT INTO Liga (Id_Liga,Pais, Division, Cant_descensos, Nombre) VALUES (" + str(self.id_liga) + ",'" + self.pais + "',"  + self.division + "'," + str(self.cant_descensos) + ","  + self.nombre +  ");")
        #db.connect("INSERT INTO Liga (Id_Liga,Pais, Division, Cant_descensos, Nombre) VALUES (%S,%S,%S,%S,%S);" ,(self.id_liga , self.pais , self.division , self.cant_descensos , self.nombre )

