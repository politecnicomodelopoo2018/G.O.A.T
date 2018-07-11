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


    def AllLigas(self):
        a = db.connect("select * from Liga")
        lista = []
        for b in a:
            L = liga(b['Id_Liga'],b['Nombre'],b['Pais'],b['Division'],b['Cant_descensos'])
            lista.append(L)

        return lista