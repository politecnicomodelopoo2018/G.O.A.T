from
class equipo():

    id_equipo = None
    liga = None
    fundacion = None


    def __init__(self,id,l,f):
        self.id_equipo=id
        self.liga=l
        self.fundacion=f

    def AllEquipos(self):
        a = db.connect("select * from Equipo")
        lista = []
        for b in a:

