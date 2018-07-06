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


    def getLiga(self):
        a = db.connect("select * from Liga")
        for b in a :
            return b

    def

